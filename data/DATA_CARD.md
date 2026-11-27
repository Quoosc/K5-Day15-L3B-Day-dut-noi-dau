# Thẻ dữ liệu (DATA_CARD) — Smart Video Concept Seek (Track A1)

## 1. Dữ liệu tri thức bài giảng (Transcript Grounding Store)
- **File:** `data/lecture_transcripts.json`; video nguồn nằm trong `data/video/`.
- **Nhãn nguồn:** `thật` (trích xuất trực tiếp nội dung và mốc thời gian từ 3 video `.mp4` do nhóm cung cấp; cả ba video nguồn được lưu và theo dõi trong repo tại `data/video/`).
- **Quy mô:** 3 video bài giảng · 35 phân đoạn có mã định danh (`[V1-S01]`–`[V1-S06]`, `[V2-S01]`–`[V2-S17]`, `[V3-S01]`–`[V3-S12]`), tổng thời lượng bài giảng ~80 phút:
  1. `VID-01` — *Tìm hiểu về thuật ngữ Mounted & Unmounted* (F8 Official, `05:36`, 6 đoạn `V1-S01`..`V1-S06`)
  2. `VID-02` — *Tất cả những gì bạn cần biết về Harness Engineering* (Việt Nguyễn AI, `38:56`, 17 đoạn `V2-S01`..`V2-S17`)
  3. `VID-03` — *Tất cả những gì bạn cần biết về Transformer trong 35 phút* (Việt Nguyễn AI, `35:52` nội dung chính / `38:33` tổng file, 12 đoạn `V3-S01`..`V3-S12`)
- **Cấu trúc mỗi phân đoạn:** `code` (`Vx-Syy`), `start` (`MM:SS`), `end` (`MM:SS`), `seconds` (số nguyên giây để gắn tham số `?t=<seconds>`), `topic`, `keywords`, `text`.
- **Vị trí và cách lưu:** Bản nộp có cả ba video `.mp4` tại `data/video/` và transcript có cấu trúc tại `data/lecture_transcripts.json`; `source_file` trong JSON trỏ tới file video tương ứng. Thư mục `my-doc/` bị `.gitignore` bỏ qua và không phải vị trí dữ liệu của bản nộp hiện tại.
- **Giới hạn:** Video nguồn là tệp nhị phân trong repo; không có dữ liệu cá nhân (PII) hay thông tin nhận diện học viên thật trong transcript đã nộp.

## 2. Dữ liệu bộ câu thử đánh giá (Benchmark)
- **File:** `eval/benchmark.csv`
- **Quy mô:** 30 câu thử trải đều 3 nhóm theo yêu cầu đường dài (`20–30` câu ở CP3):
  - `thuong`: **14 câu** (`B01`–`B14`) — phủ cả 3 video (3 câu ReactJS Mounted/Unmounted, 6 câu Harness Engineering, 5 câu Transformer).
  - `kho`: **11 câu** (`B15`–`B25`) — gồm 3 câu đối chiếu khái niệm sâu đa đoạn (`B15`–`B17`), 4 câu cụt lủn/mơ hồ/hỏi chung bài kích hoạt quy tắc hỏi lại G10 (`B18`–`B21`), và **4 câu ngoài phạm vi / bẫy từ khoá** không có trong 3 video (`B22`–`B25`: `useEffect` + Redux Toolkit, K-Means + Logistic Regression, Kubernetes Helm + Nginx, và bẫy từ khoá nấu phở Hà Nội đối chiếu với ẩn dụ quán phở ở `VID-02`).
  - `tu_choi`: **5 câu** (`B26`–`B30`), trong đó có **3 câu tấn công** (`B28`–`B30`) giả danh giảng viên đòi đáp án và ép bịa mốc `99:00`, ép đóng vai bạn cùng lớp nhắc bài, và đòi bỏ qua quy tắc để giải thích BPTT LSTM + bịa mã `[V3-S99]` tại `45:00`.
- **Nguồn ở mốc CP2:** `30/30` câu gắn nhãn `tu_viet:...` (nhóm tự soạn dựa trên nội dung 3 video trong `data/video/` và bảng 4 lớp chỗ khó trong `spec.md §5`); hiện có `0/30` câu có nguồn `nguoi_dung:` hoặc `data_that:` theo quy tắc của `run.py check`.
- **Trạng thái nguồn thật:** Chưa đạt mốc CP3: cần bổ sung ít nhất 10 câu hỏi trắc nghiệm / câu hỏi vấp có nguồn `nguoi_dung` / `data_that` để đạt ≥ 1/3 bộ 30 câu. Không lấy câu tự soạn rồi đổi nhãn nguồn.
- **Quy định ẩn danh:** Không lưu họ tên thật, email hay mã sinh viên vào `eval/benchmark.csv`; dùng ký hiệu ẩn danh nếu trích từ người học (`P1`, `P2`...).

## Dữ liệu bổ sung cho bằng chứng pain (CP2)

### Đoạn bài mẫu cho trợ giảng có căn cứ

| | |
|---|---|
| Dùng để làm gì | Dữ liệu đọc thử cho `search_lesson` và bản demo trợ giảng; hỗ trợ thử câu hỏi thường, câu mơ hồ và câu ngoài bài. |
| Nguồn và nhãn | Nhóm tự biên soạn các khái niệm AI/LLM; `synthetic`, không phải tài liệu chính thức của khoá. |
| Xử lý và quy mô | Soạn thủ công thành 8 đoạn độc lập mã `L01`–`L08`, lưu tại `data/lesson_passages.csv`; không có dữ liệu người học. |
| Phiên bản | v1 · 27/11/2026. |
| Giới hạn | Phạm vi hẹp, chưa có kiểm tra viên chuyên môn độc lập; chỉ dùng thử tra cứu và từ chối khi không có căn cứ, không dùng làm bằng chứng pain. |

### Nhật ký hành vi pre-class đã ẩn danh

| | |
|---|---|
| Dùng để làm gì | Đếm lượt hỏi trợ giảng và cờ `missing_context` do hệ thống ghi; chi tiết ở `evidence/data-mining.md`. |
| Nguồn | Data BTC cấp: `K5-L3-Day15-AI-Product-Hackathon/data/preclass/chat.csv` và `events.csv`; dữ liệu 05–25/11/2026. |
| Xử lý | Đếm `chat.kind=question`, nối `chat.id` với `events.ref_id` của `agent_replied`, đọc `data.missing_context`; script chạy lại: `evidence/count_preclass.py`. Không lưu CSV gốc trong repo. |
| Kết quả | 1.091 câu hỏi; 98 có cờ `missing_context=true`. 7 câu trả lời quiz video lần đầu từ 2 người; 2 sai của cùng một người, không có seek cùng video trong 15 phút tiếp theo. |
| Giới hạn | Cờ hệ thống chưa được kiểm chứng là lỗi hay trải nghiệm đau; không có nội dung hỏi/đáp. Chỉ phản ánh 143 người có ít nhất một câu hỏi, không đại diện toàn bộ lớp. Phép đếm sau câu sai chỉ có 2 trường hợp từ 1 người và `session_id` trống; không thể khái quát hay kết luận quan hệ nhân quả. |
