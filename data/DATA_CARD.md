# Data card — dữ liệu bản chạy thử

## Dataset 1 · Đoạn bài mẫu cho trợ giảng có căn cứ

| | |
|---|---|
| Dùng để làm gì | Dữ liệu đọc thử cho `search_lesson`/bản demo trợ giảng; nguồn để viết câu hỏi thường, câu mơ hồ và câu ngoài bài trong benchmark. |
| Từ đâu | Nhóm tự viết nội dung khái niệm cơ bản về AI/LLM; không sao chép transcript hoặc tài liệu khoá. |
| Xử lý những bước gì | Soạn thủ công thành các đoạn độc lập, gắn mã `L01`–`L08`; không có dữ liệu người học, không cần ẩn danh hay lọc. |
| Số dòng / số đoạn | 8 đoạn; xem `data/lesson_passages.csv`. |
| Phiên bản / ngày lấy | v1 · 27/11/2026. |
| Nhãn | `synthetic` — nội dung do nhóm tự biên soạn để chạy thử, không phải tài liệu chính thức của khoá. |
| Giới hạn | Chỉ có 8 khái niệm hẹp, không phủ toàn bộ giáo trình; không dùng để kết luận mức độ hiểu bài hay pain. Nhóm chưa có người kiểm chuyên môn ghi nhận. |

**Cách tạo và kiểm:** viết thủ công theo chủ đề AI/LLM, không dùng sinh tự động nên seed không áp dụng. Tự rà đủ 8 mã, trường và nội dung; chưa có kiểm tra viên độc lập. Bộ này chỉ để thử tra cứu và hành vi từ chối khi không thấy căn cứ, không làm bằng chứng pain.

## Dataset 2 · Nhật ký hành vi pre-class đã ẩn danh

| | |
|---|---|
| Dùng để làm gì | Đếm lượt hỏi trợ giảng và cờ `missing_context` do hệ thống ghi; tham khảo ở `evidence/data-mining.md`. |
| Từ đâu | Data BTC cấp: `K5-L3-Day15-AI-Product-Hackathon/data/preclass/chat.csv` và `events.csv`. |
| Xử lý những bước gì | Đọc CSV UTF-8, lấy `chat.kind=question`, nối `chat.id` với `events.ref_id` của `agent_replied`, đọc JSON `data.missing_context`; chỉ lưu số tổng hợp và vài mã dòng đã ẩn danh có trong data BTC. Không sao chép CSV gốc. |
| Số dòng / số đoạn | 1.091 câu hỏi; 98 có cờ `missing_context=true`. |
| Phiên bản / ngày lấy | Bản BTC trong repo đề, dữ liệu 05–25/11/2026; kiểm đếm lại 27/11/2026. |
| Nhãn | Nhật ký hành vi đã ẩn danh do BTC cung cấp; cờ là nhãn hệ thống, chưa được kiểm chứng là lỗi hay trải nghiệm đau của người học. |
| Giới hạn | Không có nội dung câu hỏi/trả lời; cờ `missing_context` không chứng minh câu trả lời sai hoặc người học không giải quyết được việc. Chỉ phản ánh 143 người có ít nhất một câu hỏi, không đại diện toàn bộ 436 người hoạt động hay 721 tài khoản. |

Chỉ dùng dữ liệu BTC tại nguồn được cấp để chạy script; không đưa nguyên file vào repo nhóm. Cách đếm và ví dụ tổng hợp: `evidence/data-mining.md`, script: `evidence/count_preclass.py`.
