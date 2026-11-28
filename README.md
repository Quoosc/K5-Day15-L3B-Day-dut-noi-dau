# Đúng đoạn · Day dứt nỗi đau
Học viên dán câu quiz vừa làm sai, đọc gợi ý có trích transcript rồi mở video tại giây cần ôn. Bản thử có 35 đoạn từ 3 video.

## Chạy trong 3 phút
Từ thư mục gốc, dùng Python 3.10 trở lên. Tạo file .env từ .env.example nếu chưa có. Điền MODEL_PROVIDER=groq, MODEL_NAME và API_KEY trên máy demo. Hai lượt đánh giá đã lưu dùng openai/gpt-oss-20b.

    python run.py check
    python run.py

Mở địa chỉ giao diện trong terminal. Thử hỏi “Transformer dùng Positional Embedding ở đoạn nào?” rồi chọn xem từ 03:53. Với câu chỉ nhớ từ “context”, chọn chủ đề trước khi mở video. [Hướng dẫn chạy](codebase/DEMO.md)

## Bản trình bày
[Slide nộp CP4](demo-slides.pdf) · [PowerPoint chỉnh sửa](slides/demo-slides.pptx) · [Video demo dự phòng](slides/quoc-demo-30s.mp4) · [Slide CP4 trên Drive của nhóm (10 trang)](https://drive.google.com/drive/folders/1fiKwkegMBMq5WnrTEIoN_0LrvhwNksK2?usp=drive_link)

## Bằng chứng và kết quả
- [Canvas](canvas.md), [thiết kế và ngưỡng CP2](spec.md), [nguồn và giới hạn bằng chứng](evidence/summary.md). Truy được 4 trích dẫn trong các biên bản.
- [Hai lượt đánh giá](eval/report.md). Groq chạy thật trên 30 câu do nhóm viết. Lượt 1 đạt 24/30, lượt 2 đạt 30/30. Kiểm lại bằng python run.py score eval/run-2.csv.
- [Chi phí](cost/cost-estimate.md). 50 phiên đo token bằng Ollama, tỷ lệ đạt lấy từ lượt 2, chi phí tính theo đơn giá kịch bản. Lệnh tái lập mô phỏng: python run.py simulate --rate-from eval/run-2.csv.
- [Kiểm thử thao tác](validation/log.md). Số lần nhấn hiện đo bằng kiểm thử kỹ thuật nội bộ. Cần đo thêm với người ngoài nhóm.
- [Phân công](TEAMS.md) · [Nhật ký dùng AI](docs/ai-usage.md) · [Phân vai thuyết trình](slides/outline.md).