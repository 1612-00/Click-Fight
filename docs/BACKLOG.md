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
- Hiệu ứng âm thanh đợt 1 (bộ nén, tiếng bấm 2 lớp, combo PERFECT tăng cao độ, ba tầng thưởng, nhạc nhỏ lại khi lên hạng, lọc nhạc khi mở bảng, nhạc nhanh 5 giây cuối trận, rung): đã kiểm tra chạy không lỗi bằng code, **chưa nghe bằng tai** để chốt độ to từng tiếng (TEST_PLAN M11–M17); chưa thử rung trên điện thoại thật; nhạc nhanh cuối trận chưa thử trong trận thật.
- Nhạc đợt 2 (`gym2`, `gym3`, `rankup`, `win`, `lose`): đã kiểm tra tải, cân âm lượng và phát không lỗi bằng code; **chưa nghe bằng tai** độ to đoạn thưởng (hằng `STING` = 0,08) và chỗ nối khi lặp của `gym2`/`gym3` (TEST_PLAN M4, M19–M20).
- Âm thanh khách ghé (còi và giọng PT, giọng Crush, kèn bánh, tiếng gắng sức khi PERFECT, vút/tích của vòng): đã vào game, kiểm tra tải đủ 22 file và phát không lỗi bằng code; **chưa nghe bằng tai** độ to (hằng `VOXL` = 0,06) và mật độ khi chơi lâu (TEST_PLAN M22–M26).
- `tools/sim.py` chưa mô phỏng ngày tập một phần (mỗi ngày hoặc tập đủ hoặc nghỉ hẳn), nên ngưỡng `REST` = 20% không ảnh hưởng kết quả mô phỏng.
- Rep hoàn hảo: canh nhịp trên điện thoại thật (độ trễ cảm ứng), khoảng ±110 ms có quá khó hay quá dễ không; người chơi thật bắt được bao nhiêu phần trăm (sim giả định 50%).
- Khách ghé phòng tập: bấm thật trên điện thoại (khách có che nhân vật hay nút không), người chơi thật bấm được bao nhiêu phần trăm và có bỏ qua bánh không (sim giả định bấm hết).

## Lỗi và hạn chế đã biết

- `tools/sim.py` giả định tối nào cũng ăn một món cố định; chưa mô phỏng thực đơn xoay vòng, cũng chưa mô phỏng lối "ăn vặt tới hạng 3 rồi siết cân".

## Ý tưởng chưa làm

- Bấm đối thủ đã hạ trong tab Thi đấu để xem lại thoại.

- Mở rộng ngoài Trái Đất: hạng 10+ và các giải phản diện vũ trụ (Mặt Trăng, Sao Hỏa…), nối tiếp sau Hắc Vương Lõi Đất.

- Font chữ riêng đóng kèm game (cần tải file font).
- Nhân vật thứ 3 và 4 (chú bảo vệ, thực tập sinh): đã quyết định bỏ qua, ảnh chưa có.
- Thêm cách giảm cân hoặc nội dung cuối game sau hạng 6 (đã có kỹ năng Sao và 4 thử thách; xem người chơi thật có làm hết không).
- Sim chưa mô phỏng kỹ năng Sao và nhiều đời liên tiếp; độ dài thử thách mới đo bằng cách nhân hệ số x4,5 cho đời 2.
- Cần QA bản upload trên CrazyGames và quay video xem trước theo [UI_REDESIGN_PLAN.md](./UI_REDESIGN_PLAN.md); chủ dự án cần tạo tài khoản và tải game lên trước.
