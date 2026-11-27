# Reflection — Phạm Trấn Quốc

1. **Phần phụ trách.** Phần của Quốc gồm tra transcript, gọi Groq, kiểm mã đoạn và giao diện demo. Hai commit 81c6aef và 2cd3fd4 ghi nhận bước nối model và bản web đầu tiên. Bản Đúng đoạn bổ sung lọc theo bài, căn cứ từ transcript và thao tác sửa gợi ý.
2. **Sử dụng AI.** Codex hỗ trợ viết và rà code, thực hiện các lượt chạy kiểm tra, ghi hình trên Edge. Trong lần kiểm tra mobile đầu, trang rộng quá khung màn hình. Sau điều chỉnh CSS, chiều rộng nội dung đo được là 390 px trên viewport 390 px.
3. **Một trường hợp trượt.** B16 ở lượt 1 không có câu trả lời vì Groq trả HTTP 429. Khi thử lại có giới hạn và giãn nhịp, B16 nhận được kết quả ở lượt 2. Lỗi gọi dịch vụ cần được tách khỏi lỗi chọn sai kiến thức; người chấm vẫn phải đối chiếu nội dung trước khi tính phần trăm đạt.
