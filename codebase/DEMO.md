# Đúng đoạn — bàn giao phần của Phạm Trấn Quốc

Chạy `python run.py` từ thư mục gốc, mở địa chỉ **Giao diện demo** và giữ terminal mở. Demo dùng thư viện chuẩn Python, ba video trong `data/video/` và 35 đoạn trong `data/lecture_transcripts.json`. Điền MODEL_PROVIDER=groq, MODEL_NAME=openai/gpt-oss-20b và API_KEY trong .env riêng trên máy. Đổi MODEL_PROVIDER thành fake để chạy ngoại tuyến.

## Trình diễn trong phòng

1. Dán “Vì sao Transformer cần biết thứ tự các từ?”. Bấm **Tìm đoạn cần ôn**. Đối chiếu chủ đề, mã V3-S03, đoạn 03:53–06:53 và nội dung trong bản ghi. Bấm **Xem từ 03:53**. Chi tiết lượt chạy hiển thị model cùng số token do API trả về.
2. Thử “Mình quên context trong bài nào rồi”. Chọn một chủ đề trong các đề xuất. Nếu kết quả chưa đúng ý, bấm **Chưa đúng ý**, bổ sung một chi tiết và tìm lại. Câu hỏi ban đầu được giữ trên màn hình.
3. Bấm một bài trong thư viện để giới hạn tìm kiếm. Có thể quay về “Tất cả bài giảng”. Ngoài nguồn, trợ giảng báo thiếu căn cứ. Khi học viên xin đáp án, trợ giảng chỉ về video để tự ôn.
4. Nếu mạng/API lỗi khi thi, dùng video dự phòng trong `slides/quoc-demo-30s.mp4`.

## Dữ liệu và kết quả

Ảnh bìa được trích tại giây 90 của từng MP4. Dòng nội dung hiển thị lấy nguyên từ bản ghi đoạn của nhóm, là tóm tắt có nguồn, không tuyên bố nguyên văn lời giảng. Model chỉ chọn một mã từ tập ứng viên; code kiểm mã và lấy thời gian từ bản ghi. Dữ liệu BTC về hành vi pre-class phục vụ nghiên cứu pain, không chứa kho lời giảng để phát lại. Trình duyệt chỉ gửi câu hỏi, bài đang chọn và phần làm rõ tới máy chủ cục bộ; máy chủ gửi câu hỏi và ứng viên tới Groq.

| Mốc | Bằng chứng của Quốc | Kiểm tra khi bàn giao |
|---|---|---|
| CP1 | TEAMS và canvas ghi nhiệm vụ tìm đoạn | Khung check đọc được bốn thành viên |
| CP2 | Luồng mock, nguồn transcript và sơ đồ trong spec §4 | Chạy cùng điểm vào python run.py |
| CP3 | Groq chọn mã đoạn; video dự phòng dài 30 giây; eval/run-1.csv và trace | Lượt 1 có 6 lỗi 429, giao Phong chấm x/N |
| CP4 | Thử lại có giới hạn khi 429, lần chạy thứ hai giãn nhịp; demo ca thường và ca khó | run-2.csv hoàn thành 30 câu không có lỗi kỹ thuật; chưa chấm pass |
| Khóa repo | Changelog, khai báo AI, ghi chép reflection | Quốc đọc lại reflection theo trải nghiệm thực tế trước khi nộp |

Lượt 1 trên main edcfcc0, không giãn nhịp: 24/30 có output. Lượt 2 sau cập nhật chính sách thử lại và giãn nhịp 3 giây: 30/30 có output. Hai thay đổi đồng thời nên không thể quy riêng hiệu quả cho retry. Phần xếp hạng theo cụm từ hiếm và frontend được hoàn thiện tiếp sau khi khởi chạy lượt 2. Kiểm thử bổ sung trên bản cuối bằng Edge với Groq thật cho câu không dấu, yêu cầu làm rõ, giới hạn nguồn và cấm chọn đáp án.

Phong chấm theo metric_spec trước khi score, sau đó chạy simulate với rate-from lượt 2. Tú xác nhận nguồn câu thử và bằng chứng người dùng, Minh kiểm slide và link video ở tab ẩn danh. Riêng số câu có output không dùng làm điểm đạt.
