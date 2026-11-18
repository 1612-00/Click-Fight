# Quy ước dự án Gym God

- Game web clicker dùng JavaScript, HTML và CSS thuần trong `index.html`. Playwright nằm trong `tools/qa/` và phục vụ kiểm thử cùng quay video. Phản hồi và tài liệu nội bộ dùng tiếng Việt. Thay đổi chuỗi trong game phải cập nhật cả `T.vi` và `T.en`.
- Đọc [kiến trúc và lệnh](CLAUDE.md), [thiết kế game](docs/GAME_DESIGN.md), [backlog](docs/BACKLOG.md) và [kế hoạch kiểm thử](docs/TEST_PLAN.md) theo phạm vi công việc. Cập nhật tài liệu liên quan khi đổi hành vi. Dùng nội dung và hình ảnh gốc của dự án.
- Khi đổi cân bằng, cập nhật cùng lúc `index.html`, số tương ứng trong `tools/sim.py`, `docs/GAME_DESIGN.md` và chữ hướng dẫn nếu có ghi số. Chạy `python tools/sim.py` và so kết quả với mục tiêu thiết kế.
- Tách cập nhật trạng thái khỏi hiển thị. Mọi thay đổi chạm tới lưu và tải bản lưu cần kiểm tra lại nhóm A trong kế hoạch. Dùng phiên trình duyệt riêng để bảo vệ tiến trình đang chơi.
- Sau khi sửa mã game, kiểm tra cú pháp và chạy `npm --prefix tools/qa test`. Trước khi nộp CrazyGames, tạo lại gói bằng `python tools/dist.py` và chạy `npm --prefix tools/qa run test:zip` theo [hướng dẫn kiểm thử](docs/TEST_PLAN.md#kiểm-tra-tự-động).
- Khi làm song song, giao một người sửa `index.html` cho mỗi đầu việc. Người viết test hoặc review làm trên worktree riêng nếu cần chỉnh file, và kiểm tra kết quả sau khi tích hợp.
