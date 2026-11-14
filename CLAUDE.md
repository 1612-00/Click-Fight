# Gym God

Game clicker 2D chạy trên web, một file HTML duy nhất. Dân văn phòng yếu ớt đi tập, lên 6 hạng. Song ngữ vi/en, nhắm tới CrazyGames. Chủ dự án viết tiếng Việt: trả lời bằng tiếng Việt.

## Tài liệu

| File | Nội dung | Khi nào sửa |
|---|---|---|
| `CLAUDE.md` | Ngữ cảnh, quy ước làm việc (file này) | Khi đổi cách làm việc, cấu trúc file |
| [docs/GAME_DESIGN.md](docs/GAME_DESIGN.md) | Luật chơi và mọi con số hiện hành, kèm lý do | Mỗi lần đổi luật hoặc con số |
| [docs/BACKLOG.md](docs/BACKLOG.md) | Việc còn tồn, phần chưa kiểm tra, ý tưởng | Khi phát hiện/xong một việc |
| [assets/PROMPTS.md](assets/PROMPTS.md) | Prompt tạo ảnh, giữ phong cách thống nhất | Khi cần ảnh mới |

Con số nằm ở ba nơi và **phải đổi cùng lúc**: `index.html` (đúng nhất khi lệch nhau), `G` trong `tools/sim.py`, và `docs/GAME_DESIGN.md`.

## Cấu trúc

- `index.html`: toàn bộ game (CSS, HTML, JS thuần). Không build, không thư viện. Script chia mục bằng chú thích `// ============ Tên mục ============`: Dữ liệu, Trạng thái + lưu, Công thức, Hiển thị, Âm thanh, Thao tác, Một ngày, Khởi động + vòng lặp.
- `assets/original/*.png`: ảnh gốc do chủ dự án tạo. `assets/*.webp`: ảnh game dùng, sinh ra bởi `assets/build.py`, không sửa tay.
- `tools/sim.py`: mô phỏng nhịp chơi theo ngày để cân bằng.
- `prototype/`: bản thử ban đầu, không còn dùng.
- `.claude/launch.json`: server xem thử tên `game`, cổng 8766.

## Lệnh

```bash
python assets/build.py
```

```bash
python tools/sim.py
```

Xem thử: mở server `game` (preview) rồi vào `http://localhost:8766/?v=N`, tăng `N` mỗi lần để tránh cache.

## Kiến trúc trong `index.html`

- **Trạng thái**: một object `s`, mặc định từ `fresh()`. Lưu bằng `save()` qua `store()` (CrazyGames `SDK.data` nếu có, không thì `localStorage`), khoá `gymgod-save`. `load()` chỉ nhận từng trường hợp lệ. Thêm trường mới thì thêm vào cả `fresh()` và `load()`.
- **Vòng lặp**: tick 100 ms cộng calo theo thời gian thực rồi gọi `ui()`. Tự lưu mỗi 5 giây.
- **Hiển thị**: `buildTexts()` dựng lại HTML khi đổi ngôn ngữ; `drawDay()` phần đổi theo ngày/màn; `ui()` chỉ cập nhật số mỗi tick.
- **Chữ**: mọi chuỗi hiển thị nằm trong `T = {vi, en}`, lấy bằng `tr(key)`. Thêm chuỗi phải thêm cả hai ngôn ngữ.
- **Màn**: `s.scene` = `office | gym | home`, đổi bằng `go(scene)`. `endDay()` kết thúc ngày.
- **Hạng**: `s.rk`, chỉ tăng trong `syncRank()`. Tính năng mở theo `unl()` (hạng cao nhất từng đạt).
- **Hộp xác nhận**: dùng `ask(text, yes)`. Không dùng `confirm()`/`alert()` vì bị chặn trong iframe của cổng game.
- **SDK**: `CG` là `null` khi không có CrazyGames; mọi lời gọi SDK phải chịu được `CG === null`.

## Quy ước khi sửa

- Giữ một file, JS thuần, không thêm thư viện hay bước build.
- Sau mỗi lần sửa script: tách script ra file tạm rồi `node --check`.
- Đổi con số cân bằng: chạy lại `python tools/sim.py` và so với mục tiêu trong GAME_DESIGN.md.
- Chỉ làm game cùng thể loại, nội dung và hình ảnh gốc. Không sao chép tên, nhân vật, hình của game khác.

## Kiểm tra trên trình duyệt: các bẫy đã dính

- **Đợi game tải xong** trước khi đụng trạng thái: `while (!ready) await ...`. Bản lưu tải bất đồng bộ (SDK có thể mất tới 4 giây).
- **Bản lưu trên tab xem thử là bản lưu thật của chủ dự án.** Trước khi thử: `const keep = JSON.stringify(s)`. Thử xong, trong `finally`: `s = Object.assign(fresh(), JSON.parse(keep)); shown = -1; syncRank(true); buildTexts(); go(s.scene); save();`. Làm trọn trong một lần gọi JS đồng bộ (không `await` giữa chừng), kẻo tự lưu 5 giây ghi trạng thái thử đè lên.
- Chủ dự án có thể đang chơi trên cùng tab: không để trạng thái thử tồn tại qua nhiều lần gọi.
- Bấm nhân vật cần cú bấm thật (`ev.isTrusted`, tối đa 20 lần/giây); `$('hero').click()` bị bỏ qua. Các nút khác bấm bằng `.click()` được.
- Thử cả khung máy tính và điện thoại (375×812) khi đổi bố cục.
- 404 của `assets/bg3.webp`, `assets/food-*.webp` là bình thường khi chưa có ảnh (game dùng nền màu và emoji).
