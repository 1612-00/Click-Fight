# Kế hoạch nâng cấp giao diện

## Mục tiêu

Giảm cảm giác “dashboard web” nhưng vẫn giữ ưu điểm của clicker: người chơi nhìn thấy ngay nhân vật, chỉ số, bài tập và thao tác chính. Hướng đã chọn: **sổ tập / bảng thiết bị phòng gym** — gợi đúng chủ đề, không biến UI thành giả da, bảng gỗ hay đồ skeuomorphic.

Giao diện cần bổ trợ phong cách anime hiện có trong [PROMPTS.md](../assets/PROMPTS.md), thay vì tạo một phong cách hình ảnh cạnh tranh với nhân vật và nền.

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

### 3. Rà nút, thông báo và popup

- Kiểm kê từng loại thông báo, hộp xác nhận và popup đang có.
- Giữ hộp xác nhận cho thao tác phá hủy hoặc có hậu quả đáng kể; chuyển thông tin nhẹ sang nhãn trong màn hoặc thông báo ngắn không chặn chơi khi phù hợp.
- Thiết kế rõ trạng thái thường, hover/focus, nhấn, bị khóa và hành động vừa hoàn thành.
- Không đổi ý nghĩa hoặc bỏ thao tác hiện có nếu chưa duyệt riêng.

### 4. Mở rộng hệ thống

- Áp dụng ngôn ngữ thị giác đã duyệt cho văn phòng, nhà, tab thi đấu, thành tựu, nhiệm vụ, lên đời và cài đặt.
- Bảo đảm popup hướng dẫn và đấu trường vẫn có sắc thái riêng nhưng cùng hệ thống chữ, màu và điều khiển.
- Chỉ bổ sung asset khi mẫu CSS không giải quyết được nhu cầu; cập nhật prompt, nguồn gốc và bản build asset theo quy ước hiện tại.

### 5. Kiểm tra và hoàn thiện

- Kiểm tra tại 1024×768, 768×1024 và 375×812; xem cả tiếng Việt lẫn tiếng Anh, màn ít và nhiều nội dung.
- Không để chữ/nút bị cắt, chồng lấp hoặc tràn ngang; vùng chạm chính tối thiểu khoảng 44 px.
- Kiểm tra tương phản, focus bằng bàn phím, trạng thái khóa và phương án dự phòng khi thiếu ảnh.
- Chạy các bài test UI liên quan trong [TEST_PLAN.md](./TEST_PLAN.md); khi đổi giao diện, cập nhật mô tả và quay lại video theo [CRAZYGAMES.md](./CRAZYGAMES.md).

## Phạm vi không đổi

- Một file game `index.html`, JavaScript/CSS thuần, không thêm thư viện hay bước build ứng dụng.
- Không đổi luật chơi, cân bằng, tiến trình, lưu game hoặc SDK CrazyGames trong lượt thiết kế giao diện.
- Không tạo hoặc thay hàng loạt ảnh trước khi mẫu thị giác được duyệt.

## Trạng thái

Đã chốt hướng “sổ tập / bảng thiết bị phòng gym”. Mẫu đầu tiên ở tab Bài tập đã dựng: tiêu đề song ngữ, mặt giấy ấm, hàng bài phẳng và nhấn riêng bài kế tiếp. Đã kiểm tra ở 1024×768 và 375×812, đổi được ngôn ngữ và chế độ mua, không tràn ngang; danh sách trên điện thoại cuộn bên trong bảng. Mẫu vẫn chờ chủ dự án duyệt trước khi áp dụng ngôn ngữ thị giác này sang màn khác.
