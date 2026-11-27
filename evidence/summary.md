# Tổng hợp bằng chứng pain — trạng thái tại CP2

> Cập nhật theo ba ghi chép phỏng vấn và chín dòng khảo sát nhóm cung cấp. Cả hai nguồn đều còn thiếu thông tin xác minh mẫu; xem các giới hạn bên dưới.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, cách đếm chạy lại, ≥5 ví dụ) | Đạt ngưỡng đếm và ví dụ; có 98/1.091 cờ, cùng 0/2 lượt sai nối với seek cùng video trong 15 phút. Pain mục tiêu vẫn chưa được xác nhận do N nhỏ | `evidence/data-mining.md` + `evidence/count_preclass.py` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | Có ghi chép 3 người; chưa xác nhận vai/lớp, ngoài nhóm, ngày và thời lượng phỏng vấn | `evidence/interviews/P1.md`…`P3.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | Chưa đạt: có 9 dòng phản hồi, chưa xác nhận điều kiện mẫu | `evidence/survey/results.csv`; giới hạn nguồn ở `evidence/survey/questions.md` |

Để tiện đọc theo từng người, có 9 hồ sơ chuyển thể giả lập từ các dòng S001–S009 ở `evidence/interviews/simulated_from_survey/`. Các diễn biến cụ thể được thêm trong hồ sơ là tình huống hư cấu để minh họa, không có trong sheet. Đây không phải phỏng vấn đã diễn ra, không phải nguồn bằng chứng độc lập và không được cộng vào ngưỡng phỏng vấn.

## 2. Số chính

- Đào data: 98/1.091 (9,0%) câu hỏi gắn cờ `missing_context=true`; 49/143 (34,3%) người có câu hỏi có ít nhất một lượt gắn cờ. Trong data có 7 lượt trả lời video quiz lần đầu từ 2 người; 2 lần sai của cùng một người và 0/2 có seek cùng video trong 15 phút. Trong toàn bộ 7 lượt, 1 lượt trả lời đúng có 16 seek trong cửa sổ (9 lần tua lùi); vì seek cũng xuất hiện ngoài mẫu sai nên không thể quy hành vi này cho việc trả lời sai. Chi tiết, năm ví dụ hành vi và nguồn: `evidence/data-mining.md`.
- Phỏng vấn: 3 người được ghi nhận là có gặp khó khăn (3/3 trong mẫu nhỏ); P1 báo 3–4 lần/tháng, P2 2–3 lần/tháng, P3 1–2 lần/tháng. Thời gian xử lý lần gần nhất lần lượt khoảng 10–15 phút, 20 phút và 5–10 phút. Đây là tự thuật, không đại diện toàn bộ học viên.
- Khảo sát: n=9 dòng phản hồi ngày 27/11. Q1 ghi nhận 8/9 có một dạng khó khăn gần đây và 1/9 chọn không gặp khó; kết quả 6/9 hoàn toàn, 3/9 một phần. Tần suất: 1/tháng 2/9, 2–5/tháng 3/9, >5/tháng 4/9. Thời gian: 10–20 phút 6/9, 1 giờ 1/9, >1 giờ 1/9, 20–40 phút 1/9. Mẫu nhỏ hơn 10 nên chỉ ghi x/n. Tư cách L3B ngoài nhóm chưa xác nhận; đây không phải tỷ lệ của lớp.

Ghi chép phỏng vấn hiện có không xác định ngày, vai/lớp hoặc việc người tham gia có ngoài nhóm hay không. Chín phản hồi khảo sát cũng thiếu form gốc, kênh và điều kiện mẫu; xem `evidence/survey/questions.md`. Chưa có trích dẫn phỏng vấn được xác nhận là nguyên văn. Các mã dòng chat và câu trả lời trong `data-mining.md` đã được ẩn danh; ví dụ hành vi không tự chứng minh pain.

### Bàn giao số liệu ban đầu (27/11/2026)

- **Minh — số liệu:** 2/7 (28,6%) câu trả lời video quiz lần đầu bị sai; hai lượt thuộc cùng một người. Sau câu sai, 0/2 có seek cùng video trong 15 phút. Có 1/7 lượt trả lời đúng có seek trong cửa sổ (16 event, 9 lần tua lùi). Đây là mẫu rất nhỏ; `session_id` trống, và log không ghi lý do tua. Nguồn/cách nối: `evidence/data-mining.md`; có thể tái chạy `python evidence/count_preclass.py --data-dir data/preclass`.
- **Phong — tình huống có nguồn:** 5 ví dụ đã ẩn danh, gồm hai lượt sai `A01200`, `A01809` không có seek sau đó và ba event tua lùi thuộc lượt đúng `A01767`. Ba event sau chỉ minh họa log ghi nhận tua, không thuộc mẫu câu sai và không phải ba quan sát độc lập. Bảng kèm timestamp, video, mốc giây và diễn giải ở `evidence/data-mining.md`.

| Mã | Vai (cần bổ sung) | Gặp pain? | Số lần / 1 tháng qua | Thời gian lần gần nhất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Chưa ghi nhận | Có | 3–4 lần | Khoảng 10–15 phút | Xem lại video, tìm Google và hỏi ChatGPT |
| P2 | Chưa ghi nhận | Có | 2–3 lần | Khoảng 20 phút | Đọc tài liệu, hỏi bạn bè và tra cứu thêm |
| P3 | Chưa ghi nhận | Có | 1–2 lần | Khoảng 5–10 phút | Xem lại đoạn video và ghi chú; phần ghi chép còn thiếu |

Tần suất và thời gian trên là tự thuật về khó khăn học tập nói chung; ghi chép chưa xác nhận cả ba người đang nói về cùng pain hoặc về việc làm sai quiz rồi tua lại video. Mỗi người có file riêng trong `evidence/interviews/`; vai/lớp, ngoài nhóm, ngày và thời lượng phỏng vấn còn thiếu.

## 3. Trích dẫn / ví dụ

Chưa có trích dẫn được xác nhận là nguyên văn. Ghi chép P1 nêu lần gần đây khi học AI Agent: bạn muốn hiểu sự khác nhau giữa Workflow và AI Agent; phản hồi có ví dụ nhưng đôi khi còn tổng quát, nên bạn xem lại video, tìm thêm ví dụ rồi đối chiếu với bài. P1 cho biết đã hiểu phần lớn và tự giải thích được sự khác nhau. Đây là nội dung ghi chép/paraphrase, không đặt trong ngoặc kép. Ghi chép P2 và P3 hiện chỉ có thông tin tóm tắt trong bảng trên. Năm mã ở `data-mining.md` là ví dụ sự kiện, không có nội dung chat để trích.

## 4. Các nguồn có khớp nhau không

Ba người trong ghi chép phỏng vấn tự báo cáo gặp khó khăn học tập; khảo sát ghi nhận 8/9 câu trả lời có khó khăn gần đây, gồm chưa hiểu bài, khó làm quiz hoặc muốn biết thêm ngoài video. Cả hai nguồn gợi ý người học xem lại, tra cứu hoặc hỏi thêm, nhưng chưa xác nhận trải nghiệm tương ứng với cờ `missing_context` hay pain hẹp sau khi sai quiz. Không thể khái quát survey vì n=9 và điều kiện mẫu chưa xác minh; các nguồn không nối được theo từng người/lượt hỏi.

## 5. Kết luận

Kết luận CP2: giả thuyết hẹp **phải kiểm lại/thu hẹp**, hiện chưa được xác nhận. Data chỉ có 2 lần đầu trả lời sai video quiz từ cùng một người, và không có seek cùng video trong 15 phút sau đó (0/2); N quá nhỏ để kết luận pain đúng hay sai. Cờ `missing_context` là chỉ báo kỹ thuật riêng, không lấp được khoảng trống này. Phỏng vấn P1 gợi ý một vấn đề rộng hơn—phản hồi đôi lúc tổng quát khiến người học tìm thêm ví dụ—nhưng chưa xác nhận đúng nhóm người dùng và không đủ để kết luận cho cả lớp. Cần hỏi đúng học viên L3 ngoài nhóm và ghi thêm các lần thực tế.

## Thông tin cần hoàn thiện

Ghi ngày, thời lượng và cách phỏng vấn; xác nhận mỗi người là học viên L3 ngoài nhóm; bổ sung câu hỏi đã hỏi và chi tiết lần gần nhất cho P2/P3. Không thêm nội dung chưa được người tham gia cung cấp.

## Mẫu câu hỏi phỏng vấn

### Mở đầu

> Mình đang tìm hiểu trải nghiệm học bài và hỏi trợ giảng dưới video. Mình muốn nghe về việc bạn đã thực sự gặp, không có câu trả lời đúng hay sai. Bạn không cần nêu tên hoặc thông tin cá nhân. Mình ghi lại ý chính ẩn danh được chứ?

### Câu hỏi chính

1. Lần gần nhất bạn hỏi một câu dưới video bài học là khi nào? Bạn đang học bài nào?
2. Lúc đó bạn muốn biết điều gì? Bạn có thể kể lại câu hỏi theo cách bạn nhớ không?
3. Bạn nhận được phản hồi gì? Điều gì trong phản hồi giúp ích hoặc chưa giúp ích cho bạn?
4. Sau khi đọc phản hồi, bạn làm gì tiếp theo? Kể lần lượt các bước bạn đã làm.
5. Cuối cùng bạn có giải quyết được điều mình đang thắc mắc không? Làm sao bạn biết?
6. Nếu chưa giải quyết được, bạn đã thử cách nào khác, hoặc quyết định để câu hỏi đó lại?
7. Việc đó ảnh hưởng thế nào đến buổi học của bạn? Nếu không ảnh hưởng thì cứ nói vậy.
8. Trong tháng vừa rồi, chuyện tương tự xảy ra mấy lần? Nếu không nhớ rõ, cứ nói không nhớ.

### Câu hỏi đào sâu khi cần

- Bạn kể cụ thể hơn lần đó được không?
- Rồi sau đó bạn làm gì?
- Bạn dựa vào đâu để biết câu trả lời đã giải quyết được câu hỏi?
- Có ví dụ gần đây nào khác không?

Hỏi mở và để người tham gia tự kể; không gợi ý rằng trợ giảng có vấn đề. Ghi ý chính ẩn danh theo mã `P1`, `P2`, `P3`; không tự điền câu trả lời thay người tham gia.
