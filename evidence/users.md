# Nhóm kịch bản benchmark — không phải hồ sơ người tham gia

> Các nhãn `U1`–`U8` bên dưới chỉ là mã nhóm kịch bản do nhóm dùng để tổ chức câu thử. Chúng không đại diện cho tám người thật, không phải mã phỏng vấn, và không dùng làm bằng chứng pain.

## Nguồn và giới hạn

- 30 câu trong `eval/benchmark.csv` đã được soạn làm tình huống kiểm thử cho ba video. Bản ghi run 1 và run 2 dùng cùng input, expected, pass criterion và type; các nhãn nguồn đã được giữ là `tu_viet`.
- Bảng này chỉ ánh xạ mã kịch bản với chủ đề/câu thử để tiện rà bộ kiểm thử. Không gán tần suất, thời gian xử lý, hành vi hay lời nói cho người tham gia.
- Bốn ghi chép được đánh dấu phỏng vấn trực tiếp là `P1`, `P2`, `P4`, `P5`; xem từng file trong `evidence/interviews/`. `P3`, `P6`–`P9` là hồ sơ giả lập từ khảo sát, không phải phỏng vấn.
- Không có nguồn trong repo xác minh 30 câu benchmark là lời hỏi thật của học viên. Không đổi nguồn câu thử thành `nguoi_dung` nếu chưa có ghi chép gốc và ánh xạ được người hỏi/câu hỏi.

## Bản đồ kịch bản tự viết

| Mã kịch bản | Chủ đề kiểm thử | Câu benchmark |
|---|---|---|
| U1 | ReactJS: Mounted/Unmounted, useState, câu mơ hồ và từ chối đáp án | B01, B02, B21, B26 |
| U2 | ReactJS: React Element/DOM, câu mơ hồ và nội dung ngoài phạm vi | B03, B18, B19, B22 |
| U3 | Harness: Agent, Ralph, framework và tấn công nhập vai | B04, B06, B07, B29 |
| U4 | Harness: Context Engineering, Compaction, Prefix Caching, Tools/Skills và giả danh giảng viên | B05, B08, B09, B15, B28 |
| U5 | Transformer: công thức, Q-K-V, Residual/LayerNorm và xin đáp án | B11, B12, B14, B27 |
| U6 | Transformer: positional/multi-head, ngoài phạm vi và prompt injection | B10, B13, B24, B30 |
| U7 | Harness/Transformer: Hooks và câu ngoài phạm vi | B16, B23 |
| U8 | Transformer: Causal Mask, câu hỏi mơ hồ và bẫy nấu phở | B17, B20, B25 |

Các nhãn U trong bảng là nhãn kịch bản tự viết, không phải danh tính ẩn danh của học viên. Bất kỳ trích dẫn nào gán cho U8 cần được đối chiếu với ghi chép hoặc xác nhận của người phỏng vấn trước khi đưa vào bằng chứng.
