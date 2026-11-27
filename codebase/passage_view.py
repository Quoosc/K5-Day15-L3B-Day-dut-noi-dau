"""Trang đọc transcript phục vụ trên loopback trong lúc chạy demo CLI."""

import re
from pathlib import Path
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import parse_qs, urlsplit


def serve_passages(videos):
    root = Path(__file__).resolve().parents[1]
    media = {f"/media/{v['video_id']}": root / v["source_file"] for v in videos}
    passages = {
        (video["video_id"], str(segment["seconds"])): (video["title"], segment)
        for video in videos for segment in video["segments"]
    }

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            url = urlsplit(self.path)
            if url.path in media:
                self.send_video(media[url.path])
                return
            key = (url.path.removeprefix("/videos/"), parse_qs(url.query).get("t", [""])[0])
            if key not in passages or not url.path.startswith("/videos/"):
                self.send_error(404)
                return
            title, seg = passages[key]
            media_path = "/media/" + key[0]
            player = (
                f'<video controls preload="auto" style="width:100%;max-width:52rem" '
                f'src="{media_path}#t={seg["seconds"]}"></video>'
                if media[media_path].is_file()
                else '<p>Bản demo hiển thị transcript vì máy chưa có video gốc.</p>'
            )
            body = (
                '<!doctype html><html lang="vi"><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<title>{escape(seg["topic"])}</title><main><p>{escape(title)}</p>'
                f'<h1>{escape(seg["topic"])}</h1><p>{escape(seg["code"])} · '
                f'{escape(seg["start"])} – {escape(seg["end"])}</p>'
                f'<blockquote>{escape(seg["text"])}</blockquote>'
                f'{player}</main></html>'
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def send_video(self, path):
            if not path.is_file():
                self.send_error(404)
                return
            size = path.stat().st_size
            start, end = 0, size - 1
            requested = self.headers.get("Range")
            if requested:
                match = re.fullmatch(r"bytes=(\d*)-(\d*)", requested)
                if match and any(match.groups()):
                    first, last = match.groups()
                    if first:
                        start = int(first)
                        end = min(end, int(last)) if last else end
                    else:
                        start = max(0, size - int(last))
                else:
                    start = size
                if start > end:
                    self.send_response(416)
                    self.send_header("Content-Range", f"bytes */{size}")
                    self.end_headers()
                    return
            self.send_response(206 if requested else 200)
            self.send_header("Content-Type", "video/mp4")
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Content-Length", str(end - start + 1))
            if requested:
                self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
            self.end_headers()
            with path.open("rb") as video:
                video.seek(start)
                remaining = end - start + 1
                try:
                    while remaining:
                        block = video.read(min(remaining, 65536))
                        if not block:
                            break
                        self.wfile.write(block)
                        remaining -= len(block)
                except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                    pass  # The player cancelled this range to seek elsewhere.

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    Thread(target=server.serve_forever, daemon=True).start()
    return server
