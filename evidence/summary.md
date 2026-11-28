# Tổng hợp bằng chứng pain — rà soát CP3 (28/11/2026)

> Phân biệt dữ liệu vận hành, khảo sát và phỏng vấn. Các nguồn chưa chứng minh mức độ pain trong toàn lớp; xem giới hạn dưới đây trước khi dùng số ngoại suy.

## 1. Nguồn hiện có

| Nguồn | Điều dữ liệu cho thấy | Giới hạn |
|---|---|---|
| Data BTC (`evidence/data-mining.md`) | 98/1.091 lượt hỏi có cờ `missing_context`; 2/7 câu trả lời video quiz lần đầu sai, cùng một học viên; 0/2 có seek cùng video trong 15 phút sau câu sai. | Cờ không xác nhận pain. N quiz-sai chỉ là 2 lượt từ một người; log không có nội dung hỏi/đáp hay lý do tua. |
| Khảo sát (`evidence/survey/results.csv`) | 8/9 dòng có `experienced_issue=yes`; 2/9 ghi `video_quiz_difficulty`. | Chỉ có mã hóa câu trả lời, thiếu form gốc/kênh/chọn mẫu; các dòng không xác nhận người trả lời là học viên ngoài nhóm. Khó khăn được hỏi rộng hơn pain quiz-sai/tìm timestamp. |
| Ghi chép phỏng vấn trực tiếp | Bốn file P1, P2, P4, P5 được ghi là phỏng vấn trực tiếp; cả bốn kể một lần gặp khó khi học video/quiz. | Chưa có ngày phỏng vấn hoặc bản ghi âm; thông tin vai/lớp và ngoài nhóm do ghi chép tự khai, cần người phỏng vấn xác nhận trước khi nộp. |
| Hồ sơ giả lập | P3, P6–P9 được ghi rõ là chuyển thể từ câu trả lời survey S003, S006–S009. | Không phải phỏng vấn, không phải lời nói nguyên văn, không tính vào cỡ mẫu phỏng vấn. |

## 2. Số liệu đã đối chiếu với nguồn

### Data BTC

- `missing_context=true`: **98/1.091 lượt hỏi (9,0%)**; **49/143 người có câu hỏi (34,3%)** có ít nhất một lượt bị gắn cờ. Đây là chỉ báo vận hành, không chứng minh câu trả lời sai hoặc học viên gặp pain.
- Video quiz lần đầu: **7 lượt từ 2 học viên**, trong đó **2/7 sai**; hai lượt sai cùng một người. Không có seek cùng video trong 15 phút sau đó (**0/2 lượt sai; 0/1 người**).
- Có một lượt trả lời đúng (`A01767`) kèm 16 seek trong cửa sổ 15 phút, gồm 9 lần tua lùi. Không biết lý do; đây không phải bằng chứng tua do trả lời sai. Cách nối và năm ví dụ hành vi: `evidence/data-mining.md`.

### Khảo sát n=9

Đếm lại trực tiếp từ `results.csv`:

| Trường đã mã hóa | x/N | Ghi chú |
|---|---:|---|
| `experienced_issue=yes` | 8/9 (88,9%) | Một dạng khó khăn học tập nói chung; không đồng nghĩa pain mục tiêu. |
| `issue_type=video_quiz_difficulty` | 2/9 (22,2%) | Câu hỏi gốc không có trong repo. |
| `frequency_band=1_per_month` | 2/9 (22,2%) | Tần suất tự báo cáo, không nối riêng với pain quiz-sai. |
| `frequency_band=2_5_per_month` | 3/9 (33,3%) | Như trên. |
| `frequency_band=over_5_per_month` | 4/9 (44,4%) | Như trên. |
| `time_band=10_20_minutes` | 6/9 (66,7%) | Thời gian cho tình huống khó nói chung. |
| `time_band=20_40_minutes` | 1/9 (11,1%) | Như trên. |
| `time_band=1_hour` | 1/9 (11,1%) | Như trên. |
| `time_band=over_1_hour` | 1/9 (11,1%) | Như trên. |
| `coping_method=ai_or_chatbot` | 6/9 (66,7%) | Mã hóa cách xoay xở; không khẳng định chatbot tìm đúng đoạn video. |
| `coping_method=rewatch_or_seek_segment` | 2/9 (22,2%) | Mã hóa cách xem lại/tua. |
| `coping_method=ask_teacher_ta_or_peer` | 1/9 (11,1%) | Mã hóa cách hỏi người khác. |

Không cộng gộp các trường thành tỷ lệ “tua video sau khi sai quiz”; form gốc và câu hỏi tự luận không có để kiểm lại cách mã hóa.

## 3. Bốn trích dẫn có trong ghi chép trực tiếp

Các câu dưới đây được ghi là nguyên văn trong bốn hồ sơ P1, P2, P4, P5. Chưa có file ghi âm; người hỏi/ghi cần xác nhận bản chép trước khi nộp như trích dẫn đã kiểm chứng.

1. **P1 · ReactJS:** “Lúc làm quiz đến câu bật tắt component bằng useState thì mình chọn nhầm. Nhớ mang máng thầy có demo đoạn Toggle show/hide mà video dài không nhớ ở phút nào. Mình phải tua tới tua lui trượt mốc bực cả mình, gấp nộp bài trước giờ học mà mò mất hơn 15 phút mới tới đoạn code thật.” Nguồn: `evidence/interviews/P1.md`.
2. **P2 · ReactJS:** “Mình làm sai câu 3 quiz pre-class về React Element trước khi render vào DOM. Biết là thầy có giải thích ở đoạn giữa video nhưng không có timestamp mục lục, ngồi bấm thanh seekbar đoán mò qua lại mất toi gần 20 phút mà vẫn lệch mất đoạn thầy vẽ sơ đồ so sánh.” Nguồn: `evidence/interviews/P2.md`.
3. **P4 · Harness Engineering:** “Bài Harness Engineering kiến thức dày đặc, xem xong làm quiz hỏi về ngưỡng Compaction 80-90% với Prefix Caching thì bị lú. Mình mở lại video dài gần 30 phút, kéo chuột tìm từng slide giải thích AGENTS.md rất cực, mất hơn 20 phút chỉ để tìm được đúng 1 phút thầy giảng.” Nguồn: `evidence/interviews/P4.md`.
4. **P5 · Transformer:** “Câu hỏi tại sao Self-Attention phải chia cho căn bậc hai của 512 làm mình lúng túng. Muốn nghe lại đoạn thầy phân tích độ lệch chuẩn gradient trước Softmax nhưng video Transformer dài 35 phút không biết ở đâu. Tua trúng đoạn khác lại phải nghe lại từ đầu, mất hơn 25 phút cực kỳ ức chế.” Nguồn: `evidence/interviews/P5.md`.

**Trích dẫn thứ năm (U8): chưa xác minh, không tính vào số trích dẫn.** Summary cũ gán một câu cho U8, nhưng hồ sơ P9 hiện là giả lập từ survey S009 và không chứa câu đó; survey S008 còn được mã hóa `experienced_issue=no`. Chỉ khôi phục trích dẫn nếu người phỏng vấn cung cấp/xác nhận ghi chép gốc đã ẩn danh.

## 4. Kết luận và giới hạn

- Bốn hồ sơ trực tiếp ghi nhận các cá nhân kể đã mất 15–25 phút tìm đoạn video sau khi làm sai quiz hoặc vướng khái niệm. Đây là tín hiệu định tính trong một mẫu nhỏ, không đại diện cho 436 người hoạt động.
- Data BTC không xác nhận hành vi tua sau quiz sai: 0/2 lượt sai có seek cùng video trong 15 phút; cả hai lượt thuộc một người. Chuỗi seek `A01767` xảy ra sau câu trả lời đúng, và log không ghi động cơ.
- Survey cho thấy khó khăn học tập nói chung ở 8/9 dòng, nhưng chỉ 2/9 được mã hóa `video_quiz_difficulty`; không có form gốc để kiểm tra nội dung câu trả lời.
- Chưa tính impact toàn lớp theo `436 × tần suất × thời gian`: số 436 là người hoạt động trong data pack, không phải số người có pain mục tiêu. Tần suất/thời gian từ bốn phỏng vấn không phải ước lượng đại diện.
- Bộ 30 câu eval là kịch bản nhóm tự viết; `evidence/users.md` chỉ là bản đồ kịch bản, không phải hồ sơ người thật. Chưa có câu hỏi benchmark được nối tới nguồn người dùng gốc.

## 5. Việc cần xác nhận trước khi nộp

1. Người ghi P1/P2/P4/P5 xác nhận ngày, ngoài nhóm và câu trích có đúng nguyên văn không.
2. Người phỏng vấn U8 xác nhận hoặc rút câu trích dẫn thứ năm; không dùng P9/S009 làm nguồn cho câu đó.
3. Nếu muốn gắn câu benchmark là `nguoi_dung`, lưu ánh xạ ẩn danh tới ghi chép nguồn gốc; nếu không, giữ `tu_viet`.
4. Giữ impact toàn lớp ở trạng thái “chưa ước lượng được” cho tới khi có mẫu và tần suất cùng pain mục tiêu.
