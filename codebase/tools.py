"""Công cụ truy xuất transcript có dấu vết cho Smart Video Concept Seek."""

import json
import re
import unicodedata
from pathlib import Path

from tracing import TOOLS, tool  # noqa: F401

_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "lecture_transcripts.json"

_STOP_WORDS = frozenset({
    "ai", "agent", "an", "anh", "ba", "bai", "ban", "bao", "bi", "biet",
    "bo", "bon", "cac", "cach", "can", "cau", "chi", "cho", "chuan", "chua",
    "chay", "co", "component", "con", "cong", "context", "cua", "cung",
    "da", "dang", "dap", "dau", "de", "den", "di", "dinh", "do", "doan",
    "du", "dung", "duoc", "em", "file", "gan", "gi", "gia", "giai", "giang",
    "giup", "go", "hai", "hay", "he", "hien", "hieu", "hoac", "hoc", "hoi",
    "hook", "huong", "khai", "khac", "khi", "khong", "kiem", "ky", "la",
    "lai", "lam", "len", "loai", "loi", "luc", "ma", "may", "minh", "mo",
    "moc", "model", "moi", "mot", "muc", "muon", "nam", "nao", "nay", "nen",
    "neu", "ngay", "nghia", "nghiem", "ngoai", "ngu", "nhanh", "nhau", "nhat",
    "nhieu", "nhu", "nhung", "noi", "nuoc", "phan", "phut", "pre", "qua",
    "quyen", "ra", "react", "reactjs", "roi", "sai", "sao", "sau", "se",
    "so", "state", "su", "sua", "tai", "tao", "ten", "thay", "the", "them",
    "thi", "thich", "thong", "thoi", "thu", "thuat", "tieng", "tim", "toan",
    "token", "toi", "tra", "trac", "trong", "truoc", "tu", "tuy", "va",
    "vai", "vao", "ve", "vi", "video", "viec", "vien", "voi", "vua", "xem",
    "xin", "xu",
})


def _normalize(text: str) -> str:
    """Chuyển chữ thường và bỏ dấu tiếng Việt để so khớp ổn định."""
    text = text.replace("đ", "d").replace("Đ", "d").lower()
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def _tokens(norm_text: str) -> set[str]:
    """Tách token chữ/số có ý nghĩa, loại bỏ từ dừng và token quá ngắn."""
    raw = re.findall(r"[a-z0-9_^-]+", norm_text)
    cleaned: set[str] = set()
    for tok in raw:
        for part in [tok, *tok.split("-")]:
            if len(part) >= 2 and part not in _STOP_WORDS:
                cleaned.add(part)
    return cleaned


def _keyword_in_query(norm_kw: str, norm_query: str) -> bool:
    """Kiểm tra từ khoá có xuất hiện nguyên vẹn theo ranh giới ký tự trong query."""
    pattern = rf"(?<![a-z0-9]){re.escape(norm_kw)}(?![a-z0-9])"
    return re.search(pattern, norm_query) is not None


def load_videos() -> list[dict]:
    """Đọc danh sách video và phân đoạn transcript từ data/lecture_transcripts.json."""
    with _DATA_PATH.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload.get("videos", [])


demo_origin = ""


def _passage_link(video, seconds):
    if demo_origin:
        return f"{demo_origin}/videos/{video['video_id']}?t={seconds}"
    source = _DATA_PATH.parents[1] / video["source_file"]
    if source.is_file():
        return f"{source.as_uri()}?t={seconds}#t={seconds}"
    base = video["video_url"]
    return f"{base}?t={seconds}"


@tool
def search_transcript(query: str, top_k: int = 3) -> list:
    """search_transcript | Input: query (str), top_k (int) | Output: danh sách phân đoạn video khớp (video_id, video_title, code, start, end, seconds, topic, text, link) | Tác động ra ngoài: Không (chỉ đọc data/lecture_transcripts.json)."""
    norm_q = _normalize(query)
    q_tokens = _tokens(norm_q)
    if not q_tokens and not norm_q.strip():
        return []

    scored: list[tuple[int, dict]] = []
    for video in load_videos():
        video_id = video.get("video_id", "")
        video_title = video.get("title", "")
        for seg in video.get("segments", []):
            score = 0
            for kw in seg.get("keywords", []):
                norm_kw = _normalize(kw)
                if _keyword_in_query(norm_kw, norm_q):
                    score += 14 if (" " in norm_kw or any(ch in norm_kw for ch in "-_^&.")) else 10

            topic_tokens = _tokens(_normalize(seg.get("topic", "")))
            text_tokens = _tokens(_normalize(seg.get("text", "")))
            score += 2 * len(q_tokens & topic_tokens)
            score += len(q_tokens & text_tokens)

            if score >= 6:
                scored.append((
                    score,
                    {
                        "video_id": video_id,
                        "video_title": video_title,
                        "code": seg["code"],
                        "start": seg["start"],
                        "end": seg["end"],
                        "seconds": seg["seconds"],
                        "topic": seg["topic"],
                        "text": seg["text"],
                        "link": _passage_link(video, seg["seconds"]),
                        "score": score,
                    },
                ))

    scored.sort(key=lambda item: (-item[0], item[1]["video_id"], item[1]["seconds"]))
    return [item[1] for item in scored[:top_k]]


@tool
def list_video_topics(video_id: str = "") -> list:
    """list_video_topics | Input: video_id (str, mặc định rỗng để lấy cả 3 video) | Output: danh sách chủ đề & mốc thời gian theo video | Tác động ra ngoài: Không (chỉ đọc data/lecture_transcripts.json)."""
    target = video_id.strip().upper()
    topics: list[dict] = []
    for video in load_videos():
        vid = video.get("video_id", "")
        if target and vid.upper() != target:
            continue
        for seg in video.get("segments", []):
            topics.append({
                "video_id": vid,
                "video_title": video.get("title", ""),
                "code": seg["code"],
                "start": seg["start"],
                "end": seg["end"],
                "seconds": seg["seconds"],
                "topic": seg["topic"],
                "link": _passage_link(video, seg["seconds"]),
            })
    return topics
