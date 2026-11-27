# Nhật ký sử dụng AI (`docs/ai-usage.md`)

Tài liệu ghi nhận minh bạch các phần có sự hỗ trợ của công cụ AI trong quá trình hoàn thiện mốc CP2 (Smart Video Concept Seek · Track A1):

| Hạng mục | Nội dung AI hỗ trợ | Người kiểm tra & xác nhận |
|---|---|---|
| Trích xuất cấu trúc transcript từ 3 video `.mp4` | Xem toàn bộ 3 video trong `data/video/`, bóc tách chính xác 35 phân đoạn (`V1-S01`..`V3-S12`), mốc thời gian `MM:SS` và số giây `?t=seconds` vào `data/lecture_transcripts.json`. | Trương Văn Phong đối chiếu lại các mốc thời gian trên từng video `.mp4`. |
| Thiết kế kiến trúc 4 lớp & bản chạy thử (`codebase/tools.py`, `codebase/agent.py`) | Xây dựng công cụ `search_transcript` và `list_video_topics` tìm kiếm đa video với bộ lọc từ dừng, cùng tiền kiểm Lớp 2 (G10) / Lớp 3 (chống gian lận) và hậu kiểm Lớp 1 trong `codebase/agent.py`. | Cả nhóm kiểm tra logic, chạy `python run.py check`, `python run.py eval --fake` và kiểm thử CLI `python run.py`. |
| Bộ câu thử & tiêu chuẩn đánh giá (`eval/benchmark.csv`, `eval/metric_spec.yaml`, `data/DATA_CARD.md`) | Đề xuất 30 câu thử chi tiết bám sát 3 video (14 `thuong`, 11 `kho`, 5 `tu_choi` với 3 tấn công và câu bẫy từ khoá) và 4 metric đo đạc; toàn bộ gắn nhãn trung thực `tu_viet:...`. | Nhóm rà soát nội dung từng câu thử và giữ nguyên chuẩn "đạt" trong `spec.md §7` trước hạn 19:30 Thứ Sáu. |

> Quy tắc minh bạch: Không tự bịa người được phỏng vấn (`P1`, `P2`...), không giả mạo dữ liệu BTC và không chạy đánh giá thật khi chưa chuyển `MODEL_PROVIDER` sang model thật ở CP3.

### Phần triển khai của Quốc — CP3 và chuẩn bị CP4
Codex hỗ trợ viết frontend Đúng đoạn, tích hợp Groq, rà hành vi thiếu căn cứ, xử lý 429 và ghi video từ lượt chạy thật. Các kiểm tra kỹ thuật và giới hạn được ghi trong codebase/DEMO.md. Việc chấm nội dung theo benchmark thuộc bước rà soát riêng của nhóm.

### Phần triển khai của Phong — CP3 và chuẩn bị CP4
Antigravity hỗ trợ thêm nhánh chạy Ollama cục bộ (`qwen2.5:3b`) trong `codebase/ai.py`, rà soát và điền nháp cột `pass`/`ghi_chu` cho `eval/run-1.csv` và `eval/run-2.csv`, cấu hình `cost/personas.yaml` theo số liệu `evidence/`, chạy `python run.py simulate` 50 phiên và tổng hợp `eval/report.md`, `cost/cost-estimate.md`. Toàn bộ điểm chấm `pass`, nguồn giả định `(tự ước tính)` và ghi chú sai khác model (`qwen2.5:3b` vs `openai/gpt-oss-20b`) được Phong kiểm tra trực tiếp trước khi hoàn tất; các mục cần người thật (chấm chéo 2 người, thử nghiệm người dùng `validation/log.md`) giữ nguyên chờ thực hiện thực tế.
