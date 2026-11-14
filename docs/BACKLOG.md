# Việc còn tồn

Xong việc nào thì xoá dòng đó. Phát hiện việc mới thì thêm vào đúng mục.

## Cần chủ dự án làm

- Tạo 4 ảnh: `bg3.png` (nền nhà), `food-healthy.png`, `food-protein.png`, `food-junk.png`. Prompt ở cuối `assets/PROMPTS.md`. Thả vào `assets/original/` rồi chạy `python assets/build.py`. Hiện game dùng nền màu và emoji.
- Quyết định: mỗi món một ảnh (9 ảnh) hay mỗi nhóm một ảnh (3 ảnh, như hiện tại).
- Tài khoản nhà phát triển CrazyGames và tải game lên. Mục Progress Save chọn "Yes, using the Data Module".

## Chưa kiểm tra trực tiếp

Mới chỉ có code, chưa từng chạy tới trên trình duyệt:

- Chủ nhật: đấu miễn phí thể lực, thưởng x2.
- Mục tiêu tuần và thưởng +10% tuần sau.
- Cân kiểm tra ngày 30.
- Bắt buộc nghỉ khi mệt mỏi 100.
- Vắng mặt hơn 24 giờ tính là ngày nghỉ.
- Nước tăng lực (cần SDK CrazyGames thật).
- Thắng một trận trong màn đấu mới.
- Ăn Yến mạch chuối / Mì tôm trứng để xem mệt mỏi giảm.
- Game chạy thế nào khi SDK tải lỗi.
- Bố cục điện thoại sau các thay đổi mở tính năng theo hạng.

## Lỗi và hạn chế đã biết

- Màn nhà trên điện thoại không còn chỗ hiện nhân vật.
- Người tập đều chạm sàn 65 kg quanh ngày 60 và mất thưởng +20% của vùng 68–72 kg.
- `tools/sim.py` giả định tối nào cũng ăn một món cố định; chưa mô phỏng thực đơn xoay vòng, cũng chưa mô phỏng lối "ăn vặt tới hạng 3 rồi siết cân".
- Số thập phân hiển thị dấu chấm (`84.8 kg`) cả ở tiếng Việt.
- Chưa dùng git: không có lịch sử thay đổi, không quay lại được bản cũ.

## Ý tưởng chưa làm

- Font chữ riêng đóng kèm game (cần tải file font).
- Nhân vật thứ 3 và 4 (chú bảo vệ, thực tập sinh): đã quyết định bỏ qua, ảnh chưa có.
- Thêm cách giảm cân hoặc nội dung cuối game sau hạng 6.
