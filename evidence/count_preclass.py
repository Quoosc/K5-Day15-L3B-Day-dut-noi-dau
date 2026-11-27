"""Đếm chỉ báo thiếu ngữ cảnh từ data pre-class BTC đã ẩn danh.

Chạy từ thư mục repo nhóm:
  python evidence/count_preclass.py --data-dir ../K5-L3-Day15-AI-Product-Hackathon/data/preclass

Script chỉ in tổng hợp và tối đa 5 mã ví dụ; không chép nội dung data vào repo.
"""
import argparse
import csv
import json
from pathlib import Path
import sys


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True,
                        help="Thư mục data/preclass BTC; không phải thư mục data của repo nhóm")
    args = parser.parse_args()

    chats = read_csv(args.data_dir / "chat.csv")
    events = read_csv(args.data_dir / "events.csv")
    questions = [row for row in chats if row.get("kind") == "question"]
    replies = {}
    for row in events:
        if row.get("type") != "agent_replied":
            continue
        try:
            replies[row.get("ref_id", "")] = json.loads(row.get("data") or "{}")
        except json.JSONDecodeError:
            continue

    flagged = [row for row in questions
               if replies.get(row.get("id", ""), {}).get("missing_context") is True]
    users = {row.get("hv") for row in questions if row.get("hv")}
    flagged_users = {row.get("hv") for row in flagged if row.get("hv")}

    print("Câu hỏi: {}/{} ({:.1f}%)".format(len(flagged), len(questions),
                                               100 * len(flagged) / len(questions) if questions else 0))
    print("Người có câu hỏi: {}".format(len(users)))
    print("Người có ít nhất một cờ: {}/{} ({:.1f}%)".format(
        len(flagged_users), len(users), 100 * len(flagged_users) / len(users) if users else 0))
    print("Ví dụ mã dòng đã ẩn danh (tối đa 5):")
    for row in flagged[:5]:
        print("  {} · {}".format(row.get("id", ""), row.get("transcript", "")))
    print("Lưu ý: cờ hệ thống là chỉ báo cần kiểm chứng, không đồng nghĩa câu trả lời sai hay người học gặp pain.")


if __name__ == "__main__":
    main()
