# Tóm tắt mô phỏng simulate-1@20261127-232307

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 10 | 1 | 290 | 10 | 0.7 | 1.1 |
| dung_vua | 17 | 2 | 557 | 24 | 1.3 | 2.5 |
| dung_nhieu | 23 | 3 | 919 | 41 | 2.1 | 3.5 |

Tỉ lệ đạt dùng để tính: 30/30 (100%) — lượt run-2@20261127-191649

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from). ⚠️ Lượt này chạy bằng openai/gpt-oss-20b, mô phỏng đo trên qwen2.5:3b — khác model.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (143 người) | Chi phí / tháng — cơ sở (436 người) | Chi phí / tháng — cao (700 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00021 (≈ 5 ₫) | $0.00021 (≈ 5 ₫) | $0.000093 (≈ 2 ₫) | $0.1397 (≈ 3.493 ₫) | $0.4260 (≈ 10.649 ₫) | $0.6839 (≈ 17.098 ₫) | $0.00098 (≈ 24 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0012 (≈ 31 ₫) | $0.0012 (≈ 31 ₫) | $0.00054 (≈ 14 ₫) | $0.8093 (≈ 20.231 ₫) | $2.47 (≈ 61.685 ₫) | $3.96 (≈ 99.035 ₫) | $0.0057 (≈ 141 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.3) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: qwen2.5:3b. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.000 ₫ ((tự ước tính) tỷ giá quy đổi tham khảo 1 USD = 25.000 VND).
