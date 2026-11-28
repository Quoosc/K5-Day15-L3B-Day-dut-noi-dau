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
| Lượt trả lời lần đầu có ít nhất một seek cùng video sau câu trả lời (đúng hoặc sai) | 1 / 7 | 14,3% | Lượt `A01767` là trả lời đúng; 16 event seek trong 15 phút, gồm 9 lần tua lùi. Không tính đây là hành vi sau câu sai. |

### Hành vi sau lần đầu trả lời sai quiz trong video

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| Lần trả lời sai có ít nhất một `video_seeked` cùng video trong 15 phút | 0 / 2 | 0,0% | Hai lần sai từ cùng một học viên; `session_id` trống nên ghép bằng học viên + bài + video + cửa sổ thời gian. |
| Trong đó có tua lùi (`to < from`) | 0 / 2 | 0,0% | Đây là proxy cho hành vi tua lại, không chứng minh đã xem đúng đoạn giải thích. |
| Học viên duy nhất có ít nhất một lần tua lùi sau câu sai | 0 / 1 | 0,0% | N chỉ là một người có lần trả lời sai; không khái quát được. |
| Lần sai nối được `answer_submitted` và câu quiz để xác định video | 2 / 2 | 100% | Không có trường hợp bị loại khỏi mẫu phân tích. |

## 4. Ví dụ cụ thể và bàn giao

Năm ví dụ hành vi dưới đây dùng mã dòng đã ẩn danh trong `answers.csv`. Hai dòng đầu là toàn bộ mẫu câu trả lời sai; ba dòng sau minh hoạ event tua trong một lượt trả lời đúng để cho thấy log ghi nhận hành vi, nhưng không được gộp vào mẫu số sau câu sai. `events.csv` không có ID riêng cho event; các dòng seek được nhận diện bằng mã câu trả lời liên quan, video và `occurred_at`.

| # | Nguồn / mã dòng | Hành vi ghi nhận | Cách diễn giải |
|---|---|---|---|
| 1 | `answers.csv` `A01200`; `answer_submitted` lúc `2026-11-25T00:16:28.826933Z`; video `d13-r1-v01` | Trả lời sai lần đầu; không có `video_seeked` cùng video trong 15 phút sau đó. | Một trong hai lượt sai trong mẫu; không biết người học đã làm gì ngoài event được ghi. |
| 2 | `answers.csv` `A01809`; `answer_submitted` lúc `2026-11-25T01:08:32.894732Z`; video `d13-r1-v03` | Trả lời sai lần đầu; không có `video_seeked` cùng video trong 15 phút sau đó. | Lượt sai thứ hai, cùng một mã học viên ẩn danh với dòng 1. |
| 3 | `answers.csv` `A01767` (đúng); `video_seeked` `2026-11-25T06:02:22.607000+00:00`; `d13-r1-v01` | Tua từ 283,7 giây về 189,4 giây, khoảng 94,3 giây lùi. | Ví dụ đối chiếu ngoài mẫu sai; event không cho biết lý do tua. |
| 4 | `answers.csv` `A01767` (đúng); `video_seeked` `2026-11-25T06:02:25.153000+00:00`; `d13-r1-v01` | Tua tiếp từ 189,4 giây về 114,8 giây, khoảng 74,6 giây lùi. | Cùng lượt trả lời và video ở dòng 3; không phải một người/lần độc lập. |
| 5 | `answers.csv` `A01767` (đúng); `video_seeked` `2026-11-25T06:02:35.801000+00:00`; `d13-r1-v01` | Tua tiếp từ 114,8 giây về 84,2 giây, khoảng 30,6 giây lùi. | Cùng chuỗi seek trong khoảng 13 giây; không suy ra mục đích hay nội dung đã xem. |

Nguồn: `answers.csv` và `events.csv` trong data pack BTC; tái tạo mẫu số bằng `python evidence/count_preclass.py --data-dir data/preclass`. Năm mã chat dưới đây là ví dụ riêng cho phép đếm cờ, không phải bằng chứng hành vi tua:

Các mã chat đã được BTC thay mới; chỉ minh hoạ bản ghi có cờ, không có nội dung hỏi/đáp để đánh giá chất lượng:

1. `C00983` — transcript `Day01/d01-r1-v05.txt` — `missing_context=true`.
2. `C00676` — transcript `Day01/d01-r1-v01.txt` — `missing_context=true`.
3. `C00998` — transcript `Day02/d02-r2-v01.txt` — `missing_context=true`.
4. `C00837` — transcript `Day02/d02-r2-v01.txt` — `missing_context=true`.
5. `C00523` — transcript `Day02/d02-r2-v03.txt` — `missing_context=true`.

Hai mã answer sai đều từ một người; `A01767` là câu trả lời đúng và chỉ làm ví dụ cho chuỗi tua. Không có nội dung câu hỏi/đáp để trích. Mã và thời gian không nhận diện trực tiếp người thật.

## 5. Giới hạn của data

Đây là cờ vận hành do hệ thống ghi; không có rubric/kiểm định độ chính xác của cờ trong gói này. 98/1.091 chỉ nói rằng phản hồi bị đánh dấu thiếu ngữ cảnh, không chứng minh pain, mức sai hoặc hậu quả. Data chỉ có 1.091/1.260 lượt chat là câu hỏi, và người hỏi có thể khác nhóm người dùng mục tiêu. Chỉ có 7 lần trả lời quiz trong video lần đầu từ 2 người trong toàn bộ khoảng dữ liệu; hai lần sai thuộc cùng một người. Không thấy seek cùng video trong 15 phút sau hai lần đó, nhưng N quá nhỏ để kết luận học viên thường không tua lại. Một câu trả lời đúng khác có 16 seek trong cửa sổ (9 lần tua lùi); điều này cho thấy seek cũng xảy ra ngoài tình huống sai, nhưng không cho biết vì sao học viên tua. `session_id` trống ở event quiz nên cách ghép theo người/bài/video và thời gian có thể còn nhầm phiên. Event tua lùi, nếu có, cũng không chứng minh người học đã xem đúng đoạn cần thiết hay việc trả lời sai gây ra hành vi đó.

→ Bản tổng hợp CP2 nhắc ba ghi chép chưa xác minh. Hồ sơ P1–P9 hiện là giả lập từ khảo sát. Cần hỏi người học thật về lần sai quiz gần nhất để kiểm tra giả thuyết.
