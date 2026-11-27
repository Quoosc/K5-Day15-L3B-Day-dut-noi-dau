# Đào data — cờ thiếu ngữ cảnh và hành vi sau quiz sai

> Phân tích dữ liệu BTC đã ẩn danh; không lưu bản sao dữ liệu nguồn trong repo nhóm.

## 1. Cách đếm — định nghĩa trước khi đọc kết quả

- Data dùng: `data/preclass/chat.csv` và `data/preclass/events.csv` của repo đề, giai đoạn 05–25/11/2026.
- Đếm gì: số câu hỏi có phản hồi mà `events.data.missing_context=true`; mẫu số là các dòng `chat.csv` có `kind=question` (không tính reply/mention). Ghép phản hồi bằng `chat.id = events.ref_id` trên dòng `type=agent_replied`.
- Mẫu số: lượt câu hỏi, không phải số tài khoản hay toàn bộ học viên. Tập này có 1.091 câu hỏi từ 143 tài khoản khác nhau; không khái quát sang toàn khoá.
- Script: `python evidence/count_preclass.py --data-dir data/preclass` (bản data cục bộ, không commit); với data pack ở vị trí khác, truyền đường dẫn thư mục `preclass` tương ứng.

### Đếm hành vi sau lần đầu trả lời sai quiz trong video — định nghĩa trước khi chạy

- Data dùng: `answers.csv` và `events.csv`, cùng giai đoạn 05–25/11/2026. Đã đọc README, từ điển cột và định nghĩa event trước khi chọn phép đếm.
- Tập mẫu / mẫu số: mỗi dòng `answers.csv` thỏa `nguon=video_quiz`, `lan_thu=1`, `was_correct=False`, có event `answer_submitted` nối bằng `events.ref_id = answers.id`. Đếm thêm số dòng không nối được để báo thiếu dữ liệu; không lấy chat, quiz cuối module hay lần thử lại làm mẫu số.
- Dấu hiệu theo dõi: nối event sai với `quiz_item_opened` đứng trước đó bằng cùng `hv`, `lesson_id` và `question_id` trong JSON; lấy video từ `video_opened` gần nhất trước câu quiz, cùng học viên/bài. Trong 15 phút sau event trả lời sai, tìm event `video_seeked` do learner thực hiện, cùng `hv`, `lesson_id` và video đó. `session_id` bị trống ở các event quiz này nên không dùng được làm khóa nối. Cửa sổ 15 phút sau câu sai là lựa chọn phân tích *(tự ước tính)* để giới hạn hành vi gần thời điểm sai, không phải ngưỡng do BTC quy định.
- Kết quả chính: số lần trả lời sai có ít nhất một lần tua lùi `to < from`, chia cho số lần trả lời sai ở mẫu số; đếm riêng số lần có bất kỳ `video_seeked` và số học viên duy nhất. Một lần tua lùi là dấu hiệu hành vi, không chứng minh học viên đã xem lại đúng phần giải thích hoặc việc sai quiz gây ra lần tua.
- Script: cùng `evidence/count_preclass.py`; chạy lại bằng data pack tương ứng. Ví dụ được chọn theo thứ tự thời gian từ các trường hợp có tua lùi, không đại diện cho toàn bộ mẫu.

## 2. Đọc trước, đếm sau

Đã xem README data pack, từ điển cột, định nghĩa event và cấu trúc hai bảng liên quan. `missing_context` là cờ trong JSON của sự kiện phản hồi, không có nội dung hội thoại để đọc. Vì vậy không thể kết luận câu hỏi thiếu thông tin thật, câu trả lời sai, hay người học không giải quyết được việc.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| Câu hỏi có `missing_context=true` | 98 / 1.091 | 9,0% | N là lượt `kind=question`; cờ được nối với phản hồi trợ giảng theo ID. |
| Người có ≥1 câu hỏi bị gắn cờ | 49 / 143 | 34,3% | N là người có câu hỏi trong data, không phải 436 người hoạt động. |
| Trả lời sai lần đầu trong video quiz | 2 / 7 | 28,6% | 7 lượt trả lời lần đầu từ 2 học viên; cả 2 lần sai của cùng 1 học viên. Mẫu rất nhỏ. |

### Hành vi sau lần đầu trả lời sai quiz trong video

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| Lần trả lời sai có ít nhất một `video_seeked` cùng video trong 15 phút | 0 / 2 | 0,0% | Hai lần sai từ cùng một học viên; `session_id` trống nên ghép bằng học viên + bài + video + cửa sổ thời gian. |
| Trong đó có tua lùi (`to < from`) | 0 / 2 | 0,0% | Đây là proxy cho hành vi tua lại, không chứng minh đã xem đúng đoạn giải thích. |
| Học viên duy nhất có ít nhất một lần tua lùi sau câu sai | 0 / 1 | 0,0% | N chỉ là một người có lần trả lời sai; không khái quát được. |
| Lần sai nối được `answer_submitted` và câu quiz để xác định video | 2 / 2 | 100% | Không có trường hợp bị loại khỏi mẫu phân tích. |

## 4. Ví dụ cụ thể

Các mã dưới đây là ID đã được BTC thay mới; chỉ minh hoạ bản ghi có cờ, không có nội dung hỏi/đáp để đánh giá chất lượng:

1. `C00983` — transcript `Day01/d01-r1-v05.txt` — `missing_context=true`.
2. `C00676` — transcript `Day01/d01-r1-v01.txt` — `missing_context=true`.
3. `C00998` — transcript `Day02/d02-r2-v01.txt` — `missing_context=true`.
4. `C00837` — transcript `Day02/d02-r2-v01.txt` — `missing_context=true`.
5. `C00523` — transcript `Day02/d02-r2-v03.txt` — `missing_context=true`.

6. `A01200` — câu video quiz đầu tiên trả lời sai ngày 25/11; không có `video_seeked` cùng video trong 15 phút kế tiếp.
7. `A01809` — một câu video quiz đầu tiên khác trả lời sai ngày 25/11 của cùng học viên đã mã hoá; không có `video_seeked` cùng video trong 15 phút kế tiếp.

Hai ví dụ câu sai đều từ một người; không có nội dung câu hỏi/đáp để trích. Các mã và thời gian được in lại bằng script; không ghi tên hay nội dung chat.

## 5. Giới hạn của data

Đây là cờ vận hành do hệ thống ghi; không có rubric/kiểm định độ chính xác của cờ trong gói này. 98/1.091 chỉ nói rằng phản hồi bị đánh dấu thiếu ngữ cảnh, không chứng minh pain, mức sai hoặc hậu quả. Data chỉ có 1.091/1.260 lượt chat là câu hỏi, và người hỏi có thể khác nhóm người dùng mục tiêu. Chỉ có 7 lần trả lời quiz trong video lần đầu từ 2 người trong toàn bộ khoảng dữ liệu; hai lần sai thuộc cùng một người. Không thấy seek cùng video trong 15 phút sau hai lần đó, nhưng N quá nhỏ để kết luận học viên thường không tua lại. `session_id` trống ở event quiz nên cách ghép theo người/bài/video và thời gian có thể còn nhầm phiên. Event tua lùi, nếu có, cũng không chứng minh người học đã xem đúng đoạn cần thiết hay việc trả lời sai gây ra hành vi đó.

→ Đã có ghi chép phỏng vấn 3 người ở `evidence/summary.md`, nhưng chưa xác nhận họ thuộc đúng nhóm học viên L3 ngoài nhóm; ghi chép cũng chưa nối được với các lượt có cờ. Cần hỏi thêm về lần làm sai quiz và việc xem lại video để kiểm tra lát cắt đã chọn; không dùng cờ này như bằng chứng thay thế cho trải nghiệm đó.
