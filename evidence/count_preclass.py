"""Đếm chỉ báo và hành vi học tập từ data pre-class BTC đã ẩn danh.

Chạy từ thư mục repo nhóm:
  python evidence/count_preclass.py --data-dir ../K5-L3-Day15-AI-Product-Hackathon/data/preclass

Script chỉ in tổng hợp và mã ví dụ đã ẩn danh; không chép nội dung data vào repo.
Đặt data pack ở thư mục cục bộ bị gitignore hoặc truyền đúng đường dẫn ngoài repo.
"""
import argparse
import csv
from datetime import datetime, timedelta
import json
from pathlib import Path
import sys


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_data(row):
    try:
        return json.loads(row.get("data") or "{}")
    except json.JSONDecodeError:
        return {}


def parse_time(value):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError):
        return None


def pct(numerator, denominator):
    return 100 * numerator / denominator if denominator else 0


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
    answers = read_csv(args.data_dir / "answers.csv")
    questions = [row for row in chats if row.get("kind") == "question"]
    replies = {}
    for row in events:
        if row.get("type") != "agent_replied":
            continue
        replies[row.get("ref_id", "")] = parse_data(row)

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

    answer_events = {}
    quiz_opens = []
    video_opens = []
    seeks = []
    for event in events:
        if event.get("type") == "answer_submitted":
            answer_events.setdefault(event.get("ref_id", ""), []).append(event)
        elif event.get("type") == "quiz_item_opened":
            event = dict(event)
            event["parsed_data"] = parse_data(event)
            event["parsed_time"] = parse_time(event.get("occurred_at", ""))
            quiz_opens.append(event)
        elif event.get("type") == "video_opened":
            event = dict(event)
            event["parsed_time"] = parse_time(event.get("occurred_at", ""))
            video_opens.append(event)
        elif event.get("type") == "video_seeked" and event.get("actor") == "learner":
            data = parse_data(event)
            try:
                data["from"] = float(data["from"])
                data["to"] = float(data["to"])
            except (KeyError, TypeError, ValueError):
                continue
            event = dict(event)
            event["parsed_data"] = data
            event["parsed_time"] = parse_time(event.get("occurred_at", ""))
            seeks.append(event)

    video_quiz_first = [row for row in answers
                        if row.get("nguon") == "video_quiz" and row.get("lan_thu") == "1"]
    wrong_first = [row for row in video_quiz_first
                   if row.get("was_correct", "").strip().lower() == "false"]
    video_quiz_users = {row.get("hv") for row in video_quiz_first if row.get("hv")}
    wrong_video_quiz_users = {row.get("hv") for row in wrong_first if row.get("hv")}
    candidates = []
    unmatched = 0
    missing_quiz_link = 0
    for answer in wrong_first:
        linked = answer_events.get(answer.get("id", ""), [])
        linked = [event for event in linked if event.get("hv") == answer.get("hv")]
        if not linked:
            unmatched += 1
            continue
        anchor = min(linked, key=lambda event: event.get("occurred_at", ""))
        anchor_time = parse_time(anchor.get("occurred_at", ""))
        question_id = parse_data(anchor).get("question_id")
        preceding_quizzes = [event for event in quiz_opens
                             if event.get("hv") == answer.get("hv")
                             and event.get("lesson_id") == answer.get("lesson_id")
                             and event["parsed_data"].get("question_id") == question_id
                             and event.get("parsed_time") and anchor_time
                             and event["parsed_time"] <= anchor_time]
        if not anchor_time or not preceding_quizzes:
            missing_quiz_link += 1
            continue
        quiz_open = max(preceding_quizzes, key=lambda event: event["parsed_time"])
        preceding_videos = [event for event in video_opens
                            if event.get("hv") == answer.get("hv")
                            and event.get("lesson_id") == answer.get("lesson_id")
                            and event.get("video")
                            and event.get("parsed_time")
                            and event["parsed_time"] <= quiz_open["parsed_time"]]
        if not preceding_videos:
            missing_quiz_link += 1
            continue
        video_open = max(preceding_videos, key=lambda event: event["parsed_time"])
        video = video_open["video"]
        candidates.append((answer, anchor, anchor_time, video))

    window = timedelta(minutes=15)
    analyzed = []
    for answer, anchor, anchor_time, video in candidates:
        matching = []
        for seek in seeks:
            seek_time = seek.get("parsed_time")
            if not seek_time or seek_time <= anchor_time or seek_time > anchor_time + window:
                continue
            if any(seek.get(key) != value for key, value in (
                    ("hv", answer.get("hv")),
                    ("lesson_id", answer.get("lesson_id")),
                    ("video", video))):
                continue
            matching.append(seek)
        backward = [event for event in matching
                    if event["parsed_data"]["to"] < event["parsed_data"]["from"]]
        analyzed.append((answer, anchor, video, matching, backward))

    any_seek = [item for item in analyzed if item[3]]
    backward_seek = [item for item in analyzed if item[4]]
    analyzable_users = {answer.get("hv") for answer, _, _, _ in candidates if answer.get("hv")}
    any_seek_users = {item[0].get("hv") for item in any_seek if item[0].get("hv")}
    backward_users = {answer.get("hv") for answer, _, _, _, back in backward_seek
                      if back and answer.get("hv")}
    print("\nHành vi sau lần đầu trả lời sai quiz trong video (cửa sổ 15 phút):")
    print("  Tổng câu trả lời quiz trong video lần đầu: {}".format(len(video_quiz_first)))
    print("  Học viên có câu trả lời quiz lần đầu: {}".format(len(video_quiz_users)))
    print("  Trả lời sai: {}/{} ({:.1f}%), từ {} học viên".format(
        len(wrong_first), len(video_quiz_first), pct(len(wrong_first), len(video_quiz_first)),
        len(wrong_video_quiz_users)))
    print("  Không nối được event answer_submitted: {}".format(unmatched))
    print("  Không nối được câu hỏi quiz để xác định video: {}".format(missing_quiz_link))
    print("  Mẫu số phân tích được: {} lần trả lời từ {} học viên".format(
        len(candidates), len(analyzable_users)))
    print("  Có video_seeked sau câu sai: {}/{} ({:.1f}%)".format(
        len(any_seek), len(candidates), pct(len(any_seek), len(candidates))))
    print("  Học viên có ít nhất một video_seeked sau câu sai: {}/{} ({:.1f}%)".format(
        len(any_seek_users), len(analyzable_users), pct(len(any_seek_users), len(analyzable_users))))
    print("  Có tua lùi (to < from): {}/{} ({:.1f}%)".format(
        len(backward_seek), len(candidates), pct(len(backward_seek), len(candidates))))
    print("  Học viên có ít nhất một lần tua lùi: {}/{} ({:.1f}%)".format(
        len(backward_users), len(analyzable_users), pct(len(backward_users), len(analyzable_users))))
    print("  Ví dụ lần sai và số seek cùng video trong cửa sổ:")
    for answer, anchor, video, matching, backward in analyzed[:5]:
        suffix = ""
        if backward:
            data = backward[0]["parsed_data"]
            suffix = " · tua lùi {}→{} giây".format(int(data["from"]), int(data["to"]))
        print("    {} · {} · {} · {} seek cùng video{}".format(
            answer.get("id", ""), anchor.get("occurred_at", ""), video,
            len(matching), suffix))
    if not analyzed:
        print("    Không có lần sai nào đủ thông tin để phân tích.")
    print("Lưu ý: cờ hệ thống là chỉ báo cần kiểm chứng, không đồng nghĩa câu trả lời sai hay người học gặp pain.")
    print("Lưu ý: seek sau câu sai là liên hệ theo cùng phiên/bài/video và thời gian, không chứng minh quan hệ nhân quả hay xem lại đúng nội dung.")


if __name__ == "__main__":
    main()
