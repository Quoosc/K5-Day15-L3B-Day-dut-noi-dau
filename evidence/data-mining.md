# Đào data — cờ thiếu ngữ cảnh trong lượt hỏi trợ giảng

> Phân tích dữ liệu BTC đã ẩn danh; không lưu bản sao dữ liệu nguồn trong repo nhóm.

## 1. Cách đếm — định nghĩa trước khi đọc kết quả

- Data dùng: `data/preclass/chat.csv` và `data/preclass/events.csv` của repo đề, giai đoạn 05–25/11/2026.
- Đếm gì: số câu hỏi có phản hồi mà `events.data.missing_context=true`; mẫu số là các dòng `chat.csv` có `kind=question` (không tính reply/mention). Ghép phản hồi bằng `chat.id = events.ref_id` trên dòng `type=agent_replied`.
- Mẫu số: lượt câu hỏi, không phải số tài khoản hay toàn bộ học viên. Tập này có 1.091 câu hỏi từ 143 tài khoản khác nhau; không khái quát sang toàn khoá.
- Script: `python evidence/count_preclass.py --data-dir ../K5-L3-Day15-AI-Product-Hackathon/data/preclass`

## 2. Đọc trước, đếm sau

Đã xem README data pack, từ điển cột, định nghĩa event và cấu trúc hai bảng liên quan. `missing_context` là cờ trong JSON của sự kiện phản hồi, không có nội dung hội thoại để đọc. Vì vậy không thể kết luận câu hỏi thiếu thông tin thật, câu trả lời sai, hay người học không giải quyết được việc.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| Câu hỏi có `missing_context=true` | 98 / 1.091 | 9,0% | N là lượt `kind=question`; cờ được nối với phản hồi trợ giảng theo ID. |
| Người có ≥1 câu hỏi bị gắn cờ | 49 / 143 | 34,3% | N là người có câu hỏi trong data, không phải 436 người hoạt động. |

## 4. Ví dụ cụ thể

Các mã dưới đây là ID đã được BTC thay mới; chỉ minh hoạ bản ghi có cờ, không có nội dung hỏi/đáp để đánh giá chất lượng:

1. `C00983` — transcript `Day01/d01-r1-v05.txt` — `missing_context=true`.
2. `C00676` — transcript `Day01/d01-r1-v01.txt` — `missing_context=true`.
3. `C00998` — transcript `Day02/d02-r2-v01.txt` — `missing_context=true`.
4. `C00837` — transcript `Day02/d02-r2-v01.txt` — `missing_context=true`.
5. `C00523` — transcript `Day02/d02-r2-v03.txt` — `missing_context=true`.

## 5. Giới hạn của data

Đây là cờ vận hành do hệ thống ghi; không có rubric/kiểm định độ chính xác của cờ trong gói này. 98/1.091 chỉ nói rằng phản hồi bị đánh dấu thiếu ngữ cảnh, không chứng minh pain, mức sai hoặc hậu quả. Data chỉ có 1.091/1.260 lượt chat là câu hỏi, và người hỏi có thể khác nhóm người dùng mục tiêu.

→ Cần kiểm lại bằng phỏng vấn ≥3 học viên L3 đã hỏi trợ giảng: hỏi lần gần nhất họ không nhận được câu trả lời có căn cứ, cách họ phát hiện và việc họ làm tiếp. Chưa có phỏng vấn/khảo sát được ghi nhận trong repo.
