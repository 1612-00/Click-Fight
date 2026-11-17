# Kế hoạch nâng cấp giao diện

## Mục tiêu

Giảm cảm giác “dashboard web” nhưng vẫn giữ ưu điểm của clicker: người chơi nhìn thấy ngay nhân vật, chỉ số, bài tập và thao tác chính. Hướng đã chọn: **sổ tập / bảng thiết bị phòng gym** — gợi đúng chủ đề, không biến UI thành giả da, bảng gỗ hay đồ skeuomorphic.

Giao diện cần bổ trợ phong cách anime hiện có trong [PROMPTS.md](../assets/PROMPTS.md), thay vì tạo một phong cách hình ảnh cạnh tranh với nhân vật và nền. Bảng màu đã duyệt: **giấy kem ấm, xanh sage/olive và điểm nhấn hổ phách**; giữ đấu trường tối để tạo tương phản.

## Nguyên tắc

- Nhân vật và cảnh là trọng tâm; UI giải thích tiến trình và lựa chọn, không tranh sự chú ý.
- Bảng tập gợi một kế hoạch luyện tập: tên bài, mục tiêu, cấp và giá có thứ bậc rõ; hạn chế cảm giác danh sách thẻ mua hàng chung chung.
- Mỗi loại thao tác có một cấp nhấn riêng: hành động chính, hành động phụ, trạng thái bị khóa. Dùng màu, hình dạng và trạng thái tương tác có chủ đích; tránh viền sáng, gradient và bóng dày đồng loạt.
- Popup chỉ dành cho việc thật sự cần quyết định hoặc có hậu quả đáng kể. Thông báo ngắn và trạng thái thường ngày nên nằm trong màn chơi, không chặn thao tác.
- Chữ, biểu tượng và trạng thái phải đọc được ở cả tiếng Việt và tiếng Anh; không dùng màu sắc làm dấu hiệu duy nhất.
- Ưu tiên CSS/HTML hiện có trước. Chỉ làm ảnh hoặc icon mới sau khi duyệt được một mẫu giao diện trong game.

## Các giai đoạn

### 1. Chốt mẫu thị giác

- Chụp và ghi nhận hiện trạng ở văn phòng, phòng tập, nhà và đấu trường.
- Dựng một lát cắt mẫu tại phòng tập: HUD nhân vật, thanh chỉ số và bảng bài tập.
- Chốt vai trò màu, kiểu chữ, hình dạng bề mặt, icon và trạng thái nút dựa trên asset anime hiện có.
- Duyệt mẫu trước khi áp cùng hệ thống lên các màn còn lại.

### 2. Thiết kế lại phòng tập trước

- Làm bảng bài tập giống sổ/plan tập hơn là một dãy thẻ cửa hàng; vẫn giữ thông tin giá, cấp, mục tiêu và thao tác mua.
- Tạo phân cấp trực quan rõ giữa bài tập cần mua tiếp, bài thường và bài chưa mở.
- Giữ hành động bấm nhân vật là trọng tâm; giảm các khung chỉ số cạnh tranh với nhân vật.
- Giữ nguyên luật, số liệu và cách mua trong đợt giao diện đầu tiên.

### 3. Phân cấp nút và trạng thái tương tác — hoàn thành

- Kiểm kê nút hành động ở HUD, văn phòng/nhà, các bảng, cài đặt và đấu trường; phân nhóm: hành động chính, phụ, mua, điều hướng và nguy hiểm.
- Chốt trạng thái thường, đang chọn, hover, nhấn, focus bàn phím, bị khóa và vừa hoàn tất; không dùng màu làm dấu hiệu duy nhất.
- Bỏ nhịp phóng to lặp lại ở nút đi tập/ngủ; giữ nhắc mua lần đầu nhẹ hơn, không đổi rung hay phản hồi của luật chơi.
- Giữ nguyên sự kiện click, giá, điều kiện khóa và tiến trình; kiểm tra chuột, cảm ứng và bàn phím.

### 4. Phân loại thông báo và hộp thoại — hoàn thành

- Lập danh sách trạng thái hiện có: mua thành công/thiếu calo, lên hạng, hoàn thành nhiệm vụ, khách ghé, vắng mặt, sự kiện văn phòng, xác nhận và kết quả đấu.
- Giữ hộp chặn cho quyết định có hậu quả; thông tin ngắn chuyển thành phản hồi tại chỗ hoặc toast không chặn nếu không làm mất thông tin.
- Làm toast hiện có gọn như thông báo trong màn và đọc được bằng trình đọc màn hình; không đổi luồng vì kết quả nhẹ đã dùng toast, còn hộp xác nhận gắn với lựa chọn có hậu quả.

### 5. HUD và hướng dẫn người mới — hoàn thành

- Rà thanh hạng, calo, thể lực, mệt mỏi, cân nặng và nút hành động theo thứ tự ưu tiên; giảm cạnh tranh thị giác với nhân vật.
- Giới hạn chiều rộng lời nhắc trong màn chơi; giữ nút HUD 44 px và gọn dòng mục tiêu trên điện thoại.
- Kiểm tra tên hạng dài, mục tiêu và hướng dẫn cuộn được ở cả tiếng Việt/Anh, kể cả màn dọc.

### 6. Chuyển cảnh và cảm giác thao tác — hoàn thành

- Rà phản hồi khi bấm nhân vật, mua bài, mở tab, lên hạng, gọi bạn tập và kết thúc trận; chỉ thêm/chỉnh chuyển động nhẹ khi giúp người chơi hiểu kết quả.
- Tôn trọng `prefers-reduced-motion`: bỏ chuyển động trang trí, giữ các tín hiệu đổi màu và thời gian game độc lập với hoạt ảnh.
- Không đổi thời điểm, độ mạnh hoặc phần thưởng của hành động trong game.

### 7. Kiểm tra và hoàn thiện — cục bộ hoàn thành; CrazyGames chờ upload

- Kiểm tra HUD và hướng dẫn tại 1024×768, 768×1024 và 375×812 bằng tiếng Việt/Anh, gồm tên hạng dài và hướng dẫn nhiều mục.
- Không để chữ/nút bị cắt, chồng lấp hoặc tràn ngang; vùng chạm chính tối thiểu khoảng 44 px.
- Kiểm tra reduced motion, toast không chặn, huỷ xác nhận, focus bàn phím và trạng thái khóa trong trình duyệt cục bộ.
- QA trên cổng game và quay lại video theo [CRAZYGAMES.md](./CRAZYGAMES.md) sau khi có tài khoản và bản upload.

## Phạm vi không đổi

- Một file game `index.html`, JavaScript/CSS thuần, không thêm thư viện hay bước build ứng dụng.
- Không đổi luật chơi, cân bằng, tiến trình, lưu game hoặc SDK CrazyGames trong lượt thiết kế giao diện.
- Không tạo hoặc thay hàng loạt ảnh trước khi mẫu thị giác được duyệt.

## Trạng thái

Chủ dự án đã duyệt mẫu sổ tập và bảng màu giấy kem/sage; các giai đoạn 1–6 hoàn thành mà không đổi luật chơi hay tiến trình. Toast gọn và có ngữ nghĩa trạng thái; HUD điện thoại giữ mục tiêu trên một dòng, hướng dẫn cuộn trong khung, chuyển động tôn trọng `prefers-reduced-motion`. QA trình duyệt cô lập ở 1024×768, 768×1024 và 375×812, cả hai ngôn ngữ, xác nhận không tràn ngang và nút HUD 44 px. **QA cục bộ hoàn thành; chỉ còn QA CrazyGames và video sau khi chủ dự án upload bản game.**
