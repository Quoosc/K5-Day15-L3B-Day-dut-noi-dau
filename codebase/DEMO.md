# Chạy demo ôn tập trên trình duyệt

Từ thư mục gốc chạy `python run.py`. Mở địa chỉ **Giao diện demo** mà terminal in ra và giữ terminal mở. Nhập khái niệm muốn ôn, bấm **Tìm đoạn bài giảng**, sau đó bấm phát. Mốc thời gian và video được lấy từ bản ghi transcript mà model chọn.

## Cấu hình Groq

Trong file .env ở gốc repo, đặt MODEL_PROVIDER=groq và MODEL_NAME=openai/gpt-oss-20b. Điền API_KEY trên máy chạy. Giao diện chỉ kết nối máy chủ Python cục bộ. Python gửi câu hỏi và các đoạn transcript ứng viên tới Groq. Chế độ MODEL_PROVIDER=fake dùng để thử giao diện khi ngoại tuyến.

## Kịch bản demo

- Nhập “Positional Embedding trong Transformer”. Kiểm tra mã đoạn, thời gian, tên model, token và phát video từ 03:53.
- Nhập “Mình làm sai câu 3”. Bổ sung tên khái niệm theo câu hỏi làm rõ.
- Nhập “Chọn đáp án A hay B về Positional Embedding”. Giao diện từ chối chọn hộ và có thể dẫn về đoạn bài để tự ôn.
- Nhập “Kubernetes Helm có trong bài giảng không?”. Giao diện báo thiếu căn cứ.

## Bàn giao cho người đánh giá

`python run.py eval --try` kiểm tra cấu hình qua ba câu đầu. Khi bộ câu đã chốt, Phong chạy `python run.py eval` để lấy kết quả lượt chính thức. Bản web và CLI dùng cùng hàm answer với bộ đánh giá. Guardrails xử lý thiếu ngữ cảnh, chỉ chấp nhận mã thuộc các đoạn được truy xuất và lấy thời gian từ dữ liệu của nhóm.
