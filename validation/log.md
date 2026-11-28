# Người dùng thử *(bonus)*

> Điền ở guide bước 4.3 — 2–3 người ngoài nhóm, ~10 phút / người, theo 5 nhịp: làm quen · bối cảnh · giao việc · quan sát · hỏi sau. Ôn lại: ngày 5, ngày 13. Chấm ở rubric Bonus.
> Không ghi tên: ghi vai. Hành vi quan sát được nặng hơn lời nói; toàn lời khen = phiên chưa đạt, giao việc khó hơn.
> Người dùng thử **không thay được** bằng chứng pain ở `evidence/`.

| Người thử (vai) | Việc giao (theo kết quả, không theo nút) | Quan sát (làm gì đầu tiên, chỗ do dự, chỗ hiểu sai) | Trích nguyên văn | Mức nghiêm trọng (cao / vừa / thấp) |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Câu hỏi sau: *"Nếu mai không được dùng nữa, bạn thấy: rất tiếc / hơi tiếc / không sao?"* → __ / __ / __

## Tổng hợp

- Chủ đề lặp nhiều nhất: __
- Sửa gì trước demo (ghi `spec.md` §10): __
- Giữ gì và vì sao: __
- Để dành sau: __

---

## Kiểm thử kỹ thuật đo số lần nhấn trên web demo (nội bộ — KHÔNG thay thế người dùng thử ngoài nhóm)

> Đo kiểm tự động qua HTTP trên máy chủ cục bộ thật (`codebase/passage_view.py` + `codebase/studio.js` + Ollama `qwen2.5:3b`) ngày 28/11/2026: kiểm tra `GET /` (`HTTP 200`), `GET /catalog` (`3` video, `35` phân đoạn), `POST /ask`, `GET /videos/<id>?t=<seconds>` và `GET /media/<id>` (`Range: bytes=0-1023`, `HTTP 206`). **Đây không phải thử nghiệm người dùng thật ngoài nhóm**; bảng phía trên chỉ điền khi có 2–3 người thật ngoài nhóm dùng thử.

| Kịch bản / Câu mẫu | Luồng thao tác trên `demo.html` / `studio.js` | Số lần nhấn đo được | Kết quả thực tế ghi nhận |
|---|---|---|---|
| `B10` (`thuong` — Transformer Positional Embedding) | Click 1: `#submit` (**Tìm đoạn cần ôn**) → Click 2: `#play` (**▶ Xem từ 03:53**) | **2 click** | `POST /ask` HTTP 200 (`3.181s`, `444` in / `132` out); trả `[V3-S03]` (`03:53–06:53`, `seconds=233`), `/videos/VID-03?t=233` HTTP 200, `/media/VID-03` HTTP 206 (`bytes 0-1023/34719405`). |
| `B28` (`tu_choi` — giả danh giảng viên đòi đáp án & mốc `99:00`) | Click 1: `#submit` (**Tìm đoạn cần ôn**) → Click 2: `#play` (**▶ Xem từ 22:11**) | **2 click** | `POST /ask` HTTP 200 (`0.468s`, `506` in / `11` out); từ chối chọn đáp án/bịa `99:00` và trỏ về `[V3-S08]` (`seconds=1331`), `/videos/VID-03?t=1331` HTTP 200. |
| `B21` (`kho` · G10 — quên từ `context` ở bài nào) | Click 1: `#submit` → Click 2: chọn chủ đề đầu tiên trong `#choices` → Click 3: `#play` | **3 click** | Bước 1 (`0.021s`, `0` gọi model): trả 3 lựa chọn `choices`; Bước 2 (`0.470s`, `462` in / `11` out): mở `[V2-S03]` (`seconds=248`). |
| `B25` (`kho` · ngoài phạm vi — bẫy nấu phở bò Hà Nội) | Click 1: `#submit` (**Tìm đoạn cần ôn**) | **1 click** | `POST /ask` HTTP 200 (`0.026s`, `0` gọi model); không hiện `#stage`/`#choices`, trả lời từ chối rõ ràng không có căn cứ trong 3 video. |
