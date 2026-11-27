# Bằng chứng CP3 — học viên tìm lại đoạn giảng

**Kết luận:** Có tín hiệu nhu cầu xem lại bài trong khảo sát nhỏ. Chưa xác nhận mức độ phổ biến của việc phải tua video sau khi làm sai quiz.

## Nguồn có thể kiểm chứng

| Nguồn | Kết quả | Giới hạn |
|---|---|---|
| Nhật ký BTC | 7 lần trả lời video quiz lần đầu từ 2 người. Hai lần sai thuộc cùng một người; 0/2 có tua cùng video trong 15 phút. | Cửa sổ quan sát ngắn, mẫu nhỏ; không ghi mục đích tua. |
| Cờ thiếu ngữ cảnh | 98/1.091 câu hỏi có cờ; 49/143 người hỏi gặp ít nhất một lần. | Cờ vận hành không đo thời gian tìm đoạn hoặc mức độ hiểu bài. |
| Khảo sát | 9 phản hồi đã mã hóa. S002 ghi khó khăn với quiz, muốn được chỉ đến đoạn liên quan và chọn xem lại. S005 chọn mục tiêu tìm đoạn giải thích. | Không có câu tự luận gốc; chưa đủ 20 phản hồi hoặc xác nhận tư cách ngoài nhóm. |
| Phỏng vấn | Các file P1–P9 hiện ghi rõ là hồ sơ giả lập từ S001–S009. | Không tính là chín phỏng vấn. Bản tổng hợp CP2 nhắc ba ghi chép riêng; chưa có biên bản gốc kiểm chứng để dùng làm trích dẫn. |

## Năm ví dụ hành vi của BTC

| Bản ghi ẩn danh | Quan sát |
|---|---|
| A01200 | Trả lời sai lần đầu ở video d13-r1-v01; 0 lần tua cùng video trong 15 phút. |
| A01809 | Trả lời sai lần đầu ở video d13-r1-v03; 0 lần tua cùng video trong 15 phút. |
| A01767 · 06:02:22 UTC | Tua từ 283,7 về 189,4 giây sau câu trả lời đúng. |
| A01767 · 06:02:25 UTC | Tua từ 189,4 về 114,8 giây trong cùng chuỗi. |
| A01767 · 06:02:35 UTC | Tua từ 114,8 về 84,2 giây trong cùng chuỗi. |

Ba dòng cuối cùng thuộc một lượt trả lời đúng. Đây là ví dụ từ dữ liệu có thể truy nguyên; chưa có năm lời nói nguyên văn của người học. Chi tiết thời điểm, cách ghép và giới hạn có trong [phép đếm](data-mining.md). [Phản hồi khảo sát](survey/results.csv) chỉ giữ nhãn phân loại.

Từ gốc repo nhóm, khi hai repo đặt cạnh nhau, chạy:

```powershell
python evidence/count_preclass.py --data-dir ../K5-L3-Day15-AI-Product-Hackathon/data/preclass
```

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
