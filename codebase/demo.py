"""Dùng chung cho CLI và web vì tracing chỉ ghi một phiên tại một thời điểm."""
from threading import Lock
import tracing
from agent import answer

_lock = Lock()


def ask(question):
    with _lock:
        tracing.begin("demo")
        try:
            result = answer(question)
        finally:
            stats, _ = tracing.end()
    return result, stats
