# Việc còn tồn

Xong việc nào thì xoá dòng đó. Phát hiện việc mới thì thêm vào đúng mục.

## Cần chủ dự án làm

- Tài khoản nhà phát triển CrazyGames và tải game lên. Mục Progress Save chọn "Yes, using the Data Module".

## Chưa kiểm tra trực tiếp

Mới chỉ có code, chưa từng chạy tới trên trình duyệt:

- Nước tăng lực (cần SDK CrazyGames thật).
- Game chạy thế nào khi SDK tải lỗi (đọc code thì an toàn: lỗi bị bắt, `CG = null`, lưu vào `localStorage`; chưa chạy thử).
- Lưu theo tài khoản CrazyGames: đăng nhập giữa chừng, chơi trên hai máy (TEST_PLAN A10, A11) chỉ thử được trên CrazyGames thật.
- Nhạc nền: mức âm lượng (`LOUD` = 0,05) đã được chủ dự án nghe và chốt; chưa thử trên điện thoại thật (iOS chặn tiếng khắt khe nhất); chưa thử nhạc tắt khi có quảng cáo thật.
- Bố cục điện thoại sau các thay đổi mở tính năng theo hạng.
- Khách ghé phòng tập: bấm thật trên điện thoại (khách có che nhân vật hay nút không), người chơi thật bấm được bao nhiêu phần trăm và có bỏ qua bánh không (sim giả định bấm hết).

## Lỗi và hạn chế đã biết

- Màn nhà trên điện thoại: nhân vật hiện nhưng nhỏ (khoảng 80px); số calo lớn bị ẩn ở màn này để lấy chỗ.
- Thanh hạng trên điện thoại xuống 3 dòng khi có cả mục tiêu nhóm cơ lẫn cân nặng.
- Người tập đều chạm sàn 65 kg quanh ngày 60 và mất thưởng +20% của vùng 68–72 kg.
- `tools/sim.py` giả định tối nào cũng ăn một món cố định; chưa mô phỏng thực đơn xoay vòng, cũng chưa mô phỏng lối "ăn vặt tới hạng 3 rồi siết cân".
- Số thập phân hiển thị dấu chấm (`84.8 kg`) cả ở tiếng Việt.

## Ý tưởng chưa làm

- Font chữ riêng đóng kèm game (cần tải file font).
- Nhân vật thứ 3 và 4 (chú bảo vệ, thực tập sinh): đã quyết định bỏ qua, ảnh chưa có.
- Thêm cách giảm cân hoặc nội dung cuối game sau hạng 6.
