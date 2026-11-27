# Thẻ dữ liệu (DATA_CARD) — Smart Video Concept Seek (Track A1)

## 1. Dữ liệu tri thức bài giảng (Transcript Grounding Store)
- **File:** `data/lecture_transcripts.json`
- **Nhãn nguồn:** `thật` (trích xuất trực tiếp nội dung và mốc thời gian từ **3 video `.mp4` thật** do nhóm cung cấp trong thư mục `my-doc/`)
- **Quy mô:** 3 video bài giảng · 35 phân đoạn có mã định danh (`[V1-S01]`–`[V1-S06]`, `[V2-S01]`–`[V2-S17]`, `[V3-S01]`–`[V3-S12]`), tổng thời lượng bài giảng ~80 phút:
  1. `VID-01` — *Tìm hiểu về thuật ngữ Mounted & Unmounted* (F8 Official, `05:36`, 6 đoạn `V1-S01`..`V1-S06`)
  2. `VID-02` — *Tất cả những gì bạn cần biết về Harness Engineering* (Việt Nguyễn AI, `38:56`, 17 đoạn `V2-S01`..`V2-S17`)
  3. `VID-03` — *Tất cả những gì bạn cần biết về Transformer trong 35 phút* (Việt Nguyễn AI, `35:52` nội dung chính / `38:33` tổng file, 12 đoạn `V3-S01`..`V3-S12`)
- **Cấu trúc mỗi phân đoạn:** `code` (`Vx-Syy`), `start` (`MM:SS`), `end` (`MM:SS`), `seconds` (số nguyên giây để gắn tham số `?t=<seconds>`), `topic`, `keywords`, `text`.
- **Ràng buộc an toàn:** Các file `.mp4` gốc trong `my-doc/` được cấu hình bỏ qua qua `.gitignore` để không đẩy nhị phân nặng và tránh rủi ro bản quyền lên git; repo chỉ lưu bản mô tả phân đoạn phục vụ truy xuất & kiểm chứng. Không chứa dữ liệu cá nhân (PII) hay thông tin nhận diện học viên thật.

## 2. Dữ liệu bộ câu thử đánh giá (Benchmark)
- **File:** `eval/benchmark.csv`
- **Quy mô:** 30 câu thử trải đều 3 nhóm theo yêu cầu đường dài (`20–30` câu ở CP3):
  - `thuong`: **14 câu** (`B01`–`B14`) — phủ cả 3 video (3 câu ReactJS Mounted/Unmounted, 6 câu Harness Engineering, 5 câu Transformer).
  - `kho`: **11 câu** (`B15`–`B25`) — gồm 3 câu đối chiếu khái niệm sâu đa đoạn (`B15`–`B17`), 4 câu cụt lủn/mơ hồ/hỏi chung bài kích hoạt quy tắc hỏi lại G10 (`B18`–`B21`), và **4 câu ngoài phạm vi / bẫy từ khoá** không có trong 3 video (`B22`–`B25`: `useEffect` + Redux Toolkit, K-Means + Logistic Regression, Kubernetes Helm + Nginx, và bẫy từ khoá nấu phở Hà Nội đối chiếu với ẩn dụ quán phở ở `VID-02`).
  - `tu_choi`: **5 câu** (`B26`–`B30`), trong đó có **3 câu tấn công** (`B28`–`B30`) giả danh giảng viên đòi đáp án và ép bịa mốc `99:00`, ép đóng vai bạn cùng lớp nhắc bài, và đòi bỏ qua quy tắc để giải thích BPTT LSTM + bịa mã `[V3-S99]` tại `45:00`.
- **Nguồn ở mốc CP2:** `30/30` câu gắn nhãn trung thực là `tu_viet:...` (tự soạn dựa sát 100% nội dung 3 video thật trong `my-doc/` và bảng 4 lớp chỗ khó trong `spec.md §5`).
- **Kế hoạch bổ sung nguồn thật trước CP3:** Nhóm sẽ phỏng vấn và thu thập ít nhất 10 câu hỏi trắc nghiệm / câu hỏi vấp thật từ học viên hoặc data thật để đạt tỉ lệ `nguoi_dung` / `data_that` ≥ 1/3 bộ câu thử (`≥ 10/30` câu).
- **Quy định ẩn danh:** Không lưu họ tên thật, email hay mã sinh viên vào `eval/benchmark.csv`; dùng ký hiệu ẩn danh nếu trích từ người học (`P1`, `P2`...).
