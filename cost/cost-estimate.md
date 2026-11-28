# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu chia theo tần suất trong `evidence/survey/results.csv` (`n=9`), `turns_per_session` và mức `6` lượt/tháng của `dung_nhieu` ghi rõ *(tự ước tính)*:
  - `dung_it`: tỉ lệ `0.22` (`2/9`: S001, S004), `1` phiên/người/tháng, `1` lượt hỏi/phiên.
  - `dung_vua`: tỉ lệ `0.33` (`3/9`: S002, S005, S006; khớp P1–P2 `2–4` lần/tháng ở `evidence/summary.md`), `3` phiên/người/tháng, `2` lượt hỏi/phiên.
  - `dung_nhieu`: tỉ lệ `0.45` (`4/9`: S003, S007, S008, S009), `6` phiên/người/tháng, `3` lượt hỏi/phiên.
- **Số người dùng thật** 3 kịch bản: thấp `143` (học viên có câu hỏi trong data pre-class) · cơ sở `436` (học viên hoạt động trong data pre-class) · cao `700` (quy mô lớp L3 theo README hackathon, *(tự ước tính)* cho kịch bản cao). Nguồn: `evidence/data-mining.md` và README hackathon.
- **Giá** 2 mức model (bảng giá tham chiếu khung repo đề, `https://ai.google.dev/gemini-api/docs/pricing`, xem `25/11/2026`): `gemini-3.1-flash-lite` (vào `$0.25` · ra `$1.50` / 1M token) · `gemini-4-hydrogen` (vào `$1.50` · ra `$7.50` / 1M token). Tỷ giá tham khảo: `1 USD = 25.000 ₫` *(tự ước tính)*.
- **Tỉ lệ đạt** dùng để tính: `30/30 (100%)` — lượt `run-2@20261127-191649` (`eval/run-2.csv`, chạy bằng `openai/gpt-oss-20b`).
- Đo token trên model **`qwen2.5:3b`** (Ollama cục bộ), tỉ lệ đạt lấy từ `eval/run-2.csv` (**`openai/gpt-oss-20b`**), tính giá model **`gemini-3.1-flash-lite`** và **`gemini-4-hydrogen`**.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261127-232307` · `50` phiên · seed `42` · lỗi `0/50`

*(chép nguyên bảng từ `cost/simulate-1-summary.md`)*

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 10 | 1 | 290 | 10 | 0.7 | 1.1 |
| dung_vua | 17 | 2 | 557 | 24 | 1.3 | 2.5 |
| dung_nhieu | 23 | 3 | 919 | 41 | 2.1 | 3.5 |

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (143 người) | Chi phí / tháng — cơ sở (436 người) | Chi phí / tháng — cao (700 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00021 (≈ 5 ₫) | $0.00021 (≈ 5 ₫) | $0.000093 (≈ 2 ₫) | $0.1397 (≈ 3.493 ₫) | $0.4260 (≈ 10.649 ₫) | $0.6839 (≈ 17.098 ₫) | $0.00098 (≈ 24 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0012 (≈ 31 ₫) | $0.0012 (≈ 31 ₫) | $0.00054 (≈ 14 ₫) | $0.8093 (≈ 20.231 ₫) | $2.47 (≈ 61.685 ₫) | $3.96 (≈ 99.035 ₫) | $0.0057 (≈ 141 ₫) |

*(Ghi chú: tỉ lệ đạt lấy từ `eval/run-2.csv` (`openai/gpt-oss-20b`), khác model đo token `qwen2.5:3b`.)*

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): **Chưa định lượng đủ cho toàn lớp** (mẫu hành vi quiz-sai trong data BTC chỉ có `0/2` lượt từ 1 người). Tuy nhiên ở cấp tự thuật (`evidence/summary.md`, `evidence/survey/results.csv`), người học báo tốn khoảng `10–20 phút` cho lần gặp khó gần nhất (6/9 khảo sát) và tần suất `1–5+ lần/tháng`.
- Chi phí / người / tháng (cơ sở, model `gemini-3.1-flash-lite`): **`$0.00098` (`≈ 24 ₫`)** — tương đương **`$0.4260` (`≈ 10.649 ₫`) / tháng** cho cả `436` học viên (hoặc **`$2.47` (`≈ 61.685 ₫`) / tháng** nếu dùng `gemini-4-hydrogen`).
- **Kết luận một dòng — đáng làm không:** **Đáng làm về mặt chi phí token** nếu triển khai với model nhẹ (`≈ 24 ₫/người/tháng`, ~`5 ₫/phiên`), miễn là xác nhận thêm bằng chứng pain thực tế ở người dùng L3B ngoài nhóm và kiểm chứng tiết kiệm thời gian qua thử nghiệm thật.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- **Cần gạt tiết kiệm chi phí đã có sẵn trong kiến trúc:**
  1. Tiền kiểm quy tắc cho G10 và câu ngoài phạm vi (`search_transcript` trả rỗng) không gọi LLM (`0` token), giúp `dung_it` chỉ gọi model trung bình `0.7` lần/phiên.
  2. Prompt chỉ gửi tối đa 3 đoạn ứng viên rút gọn thay vì toàn bộ transcript 80 phút, giữ trung bình chỉ `~290–919` token vào mỗi phiên.
  3. Dùng model nhẹ (`gemini-3.1-flash-lite`) rẻ hơn ~`5,8x` so với `gemini-4-hydrogen` cho bài toán phân loại/chọn mã đoạn JSON ngắn (`10–41` token ra/phiên).
- **Chi phí ngoài model:** máy chủ web nhỏ (hoặc chạy cục bộ bằng Ollama `0 đ` phí API), lưu trữ 3 file video `.mp4` và công biên tập/cập nhật chỉ mục transcript khi thêm bài giảng mới.
