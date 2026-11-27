"""Trang đọc transcript phục vụ trên loopback trong lúc chạy demo CLI."""

from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import parse_qs, urlsplit


def serve_passages(videos):
    passages = {
        (video["video_id"], str(segment["seconds"])): (video["title"], segment)
        for video in videos for segment in video["segments"]
    }

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            url = urlsplit(self.path)
            key = (url.path.removeprefix("/videos/"), parse_qs(url.query).get("t", [""])[0])
            if key not in passages or not url.path.startswith("/videos/"):
                self.send_error(404)
                return
            title, seg = passages[key]
            body = (
                '<!doctype html><html lang="vi"><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<title>{escape(seg["topic"])}</title><main><p>{escape(title)}</p>'
                f'<h1>{escape(seg["topic"])}</h1><p>{escape(seg["code"])} · '
                f'{escape(seg["start"])} – {escape(seg["end"])}</p>'
                f'<blockquote>{escape(seg["text"])}</blockquote>'
                '<p>Bản demo hiển thị transcript vì máy chưa có video gốc.</p></main></html>'
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    Thread(target=server.serve_forever, daemon=True).start()
    return server
