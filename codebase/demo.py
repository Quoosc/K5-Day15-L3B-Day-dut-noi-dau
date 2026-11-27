"""Dùng chung cho CLI và web vì tracing chỉ ghi một phiên tại một thời điểm."""
from threading import Lock
import tracing
from agent import answer

_lock = Lock()


def ask(question, video_id="", clarification=""):
    with _lock:
        tracing.begin("demo")
        try:
            result = answer(question, video_id, clarification)
        finally:
            stats, _ = tracing.end()
    return result, stats
