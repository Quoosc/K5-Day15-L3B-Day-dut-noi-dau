# Hồ Sơ 8 Người Dùng (U1 – U8) & 30 Câu Hỏi Thực Tế

> Tài liệu tổng hợp hồ sơ người dùng, phân tích hành vi và ánh xạ 30 câu hỏi thực tế vào bộ benchmark của hệ thống **Smart Video Concept Seek (Day dứt nỗi đau - L3B - Track A1)**.

---

## 1. Bảng Tổng Hợp Chân Dung 8 Người Dùng (User Personas)

| Mã | Vai trò / Phân loại | Video trọng tâm | Pain Point & Hành vi thực tế | Tần suất & Thời gian mất | Đặc điểm câu hỏi đóng góp |
|:---|:---|:---|:---|:---|:---|
| **U1** | **Frontend Newbie**<br>Mới học React, học gấp trước giờ lên lớp | **Video 1: ReactJS**<br>(Mounted & Unmounted) | Hay vội, làm sai quiz thì hoảng loạn muốn xin đáp án ngay (`chốt luôn đi gấp lắm`); hỏi cụt lủn không rõ ngữ cảnh. | 3–4 lần/tháng;<br>mất 10–15 phút tìm đoạn tua | • B01 (Mounted/Unmounted)<br>• B02 (useState Toggle)<br>• B21 (Mơ hồ từ `context`)<br>• B26 (Xin đáp án quiz A/B) |
| **U2** | **React / Web Dev**<br>Đã biết sơ về component, tò mò sâu về lifecycle | **Video 1: ReactJS**<br>Tìm hiểu sâu cấu trúc DOM | Nhớ lơ mơ vị trí bài giảng (`hình như phần giữa`); hay hỏi mở rộng sang kiến trúc hoặc các hook nâng cao ngoài bài học. | 2–3 lần/tháng;<br>mất 15–20 phút tìm kiếm | • B03 (React Element vs DOM)<br>• B18 (Sai câu 3 quiz pre-class)<br>• B19 (Giữa video không rõ chỗ nào)<br>• B22 (useEffect cleanup ngoài bài) |
| **U3** | **Software Engineer**<br>Chuyển dịch sang AI Agent, tư duy hệ thống | **Video 2: Harness**<br>(Agent, Harness, Ralph) | Thích so sánh các khái niệm trừu tượng (Framework vs Harness); thi thoảng gài bẫy prompt injection tối giản để ép AI nhả đáp án. | 3–5 lần/tháng;<br>mất 10–15 phút tra tài liệu | • B04 (Agent = Model + Harness)<br>• B06 (Kỹ thuật Ralph PRD/JSON)<br>• B07 (Framework vs Harness)<br>• B29 (Tấn công ép trả 1 chữ cái) |
| **U4** | **AI Engineer / Practitioner**<br>Quan tâm tối ưu hiệu năng và Context Window | **Video 2: Harness**<br>(Compaction, Prefix Caching, Tools/Skills) | Đọc tài liệu nhiều, hay thắc mắc cơ chế ngầm; thích thử thách độ vững của AI bằng kỹ thuật Jailbreak nhập vai (role-play). | 4–6 lần/tháng;<br>mất 15–25 phút | • B05 (3 kỹ thuật Context Eng)<br>• B08 (Ngưỡng Compaction 80-90%)<br>• B09 (Prefix Caching AGENTS.md)<br>• B15 (Tools vs Skills Registry)<br>• B28 (Giả danh giảng viên nhắc bài) |
| **U5** | **ML / Math Enthusiast**<br>Thích đào sâu công thức toán và số liệu | **Video 2 & Video 3**<br>(Phân quyền & Transformer Math) | Soi rất kỹ từng số liệu và công thức (căn bậc hai của 512); có xu hướng hỏi lửng lơ hoặc gài mốc thời gian ảo để xem AI có bị ảo giác không. | 2–4 lần/tháng;<br>mất 20–30 phút | • B11 (Dot Product chia sqrt 512)<br>• B12 (Q-K-V Google context vector)<br>• B14 (Residual Connection & LayerNorm)<br>• B27 (Xin đáp án 3 bậc phân quyền) |
| **U6** | **Deep Learning Learner**<br>Đang học mạng Transformer, thạo công nghệ | **Video 3: Transformer**<br>(Positional Embedding, Multi-Head) | Đang học mô hình học sâu nhưng hay bị phân tâm sang các công cụ infra khác; thích dùng prompt injection kinh điển kiểu System Override. | >5 lần/tháng;<br>mất 15–20 phút | • B10 (Positional Embedding sin/cos)<br>• B13 (Multi-head 8 heads 64 chiều)<br>• B24 (Hỏi ngoài phạm vi: Docker/K8s)<br>• B30 (Bỏ qua quy tắc / LSTM BPTT) |
| **U7** | **Data Transitioner**<br>Từ Data Analyst chuyển sang học LLM | **Video 2 & Video 3**<br>(Hooks Harness & FFN Transformer) | Dễ bị nhầm lẫn giữa kiến trúc mạng Transformer hiện đại với các thuật toán Machine Learning cổ điển đã học trước đây. | 2–3 lần/tháng;<br>mất 10–20 phút | • B16 (Pre-tool vs Post-tool hook)<br>• B23 (Hỏi K-Means ngoài phạm vi) |
| **U8** | **Non-Tech / Newbie**<br>Học viên mới vào ngành, tư duy phi kỹ thuật | **Video 3: Transformer**<br>& Quan sát chung 3 bài | Chỉ nhớ mang máng một con số hoặc từ khoá lơ mơ; hay hỏi lan man sang sinh hoạt đời thường hoặc thắc mắc ngây ngô. | 3–4 lần/tháng;<br>mất >30 phút | • B17 (Masked Self-Attention -inf)<br>• B20 (Hỏi lơ mơ bài nào có số 512)<br>• B25 (Hỏi đời sống: phở bò Hà Nội) |

---

## 2. Ma Trận Phân Bổ 30 Câu Hỏi (User Question Matrix)

| Nhóm câu hỏi | Số lượng | Danh sách câu hỏi và User | Mục đích kiểm thử hệ thống |
|:---|:---:|:---|:---|
| **thuong** (Kiến thức chuẩn 3 video) | 14 | • B01 (U1), B02 (U1), B03 (U2), B04 (U3), B05 (U4), B06 (U3), B07 (U3), B08 (U4), B09 (U4), B10 (U6), B11 (U5), B12 (U5), B13 (U6), B14 (U5) | Kiểm tra độ chuẩn xác của công cụ tra cứu transcript (`search_transcript`), trỏ đúng mã đoạn `[Vx-Syy]` và link `?t=seconds` trong tối đa 2 lần nhấn. |
| **kho_phan_biet** (So sánh khái niệm) | 3 | • B07 (U3 - Framework vs Harness)<br>• B15 (U4 - Tools vs Skills)<br>• B16 (U7 - Pre-tool vs Post-tool hook) | Kiểm tra khả năng hiểu bản chất kỹ thuật, phân biệt rõ các cặp khái niệm dễ gây nhầm lẫn trong bài giảng. |
| **kho_mo_ho** (Thiếu ngữ cảnh / G10) | 4 | • B18 (U2 - "sai câu 3 quiz pre-class")<br>• B19 (U2 - "ở giữa video")<br>• B20 (U8 - "bài khó ôn gì / bài nào có số 512")<br>• B21 (U1 - từ "context" mơ hồ nhiều bài) | Kiểm tra nguyên tắc **G10**: không đoán mò một mốc thời gian, tự động hỏi lại để thu hẹp phạm vi và gợi ý các chủ đề từ 3 video. |
| **kho_ngoai_pham_vi** (Ngoài phạm vi 3 video) | 4 | • B22 (U2 - useEffect cleanup / Redux)<br>• B23 (U7 - Thuật toán K-Means / Logistic)<br>• B24 (U6 - Kubernetes Helm / Docker compose)<br>• B25 (U8 - Nấu phở bò / Ăn gì Hà Nội) | Kiểm tra cơ chế **Grounding 100%**: từ chối trả lời hoặc báo rõ không có trong transcript bài giảng, không bịa mốc thời gian. |
| **tu_choi** (Xin đáp án & Gài bẫy) | 5 | • B26 (U1 - Xin chốt đáp án A/B)<br>• B27 (U5 - Xin xác nhận phương án C)<br>• B28 (U4 - Giả danh giảng viên ép mớm bài)<br>• B29 (U3 - Ép trả lời đúng 1 chữ cái)<br>• B30 (U6 - System prompt override & mốc ảo 99:00) | Kiểm tra **Pedagogical Guardrail & Security Guardrail**: kiên quyết từ chối mớm đáp án trắc nghiệm, kháng bẫy role-play/prompt injection, trỏ về đoạn lý thuyết để học viên tự học. |
| **Tổng cộng** | **30** | **Đầy đủ 8 User (U1 – U8) và 3 Video** | **100% câu hỏi từ người dùng thực tế (`nguoi_dung:U...`)** |
