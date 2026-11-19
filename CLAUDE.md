@AGENTS.md

# Gym God

Game clicker 2D chạy trên web, một file HTML duy nhất. Dân văn phòng yếu ớt đi tập, lên 9 hạng. Song ngữ vi/en, nhắm tới CrazyGames.

## Tài liệu

| File | Nội dung | Khi nào sửa |
|---|---|---|
| [AGENTS.md](AGENTS.md) | Quy ước dùng chung cho các agent | Khi đổi cách làm việc |
| `CLAUDE.md` | Kiến trúc và lệnh của dự án (file này) | Khi đổi cấu trúc hoặc cách chạy |
| [docs/GAME_DESIGN.md](docs/GAME_DESIGN.md) | Luật chơi và mọi con số hiện hành, kèm lý do | Mỗi lần đổi luật hoặc con số |
| [docs/BACKLOG.md](docs/BACKLOG.md) | Việc còn tồn, phần chưa kiểm tra, ý tưởng | Khi phát hiện/xong một việc |
| [docs/TEST_PLAN.md](docs/TEST_PLAN.md) | Bộ test thủ công: bước làm và kết quả mong muốn | Mỗi lần đổi luật, con số hoặc thêm tính năng |
| [docs/MUSIC_PLAN.md](docs/MUSIC_PLAN.md) | Kế hoạch nhạc nền theo màn (chưa làm) | Khi chốt quyết định hoặc làm xong bước nào |
| [docs/ARENA_PLAN.md](docs/ARENA_PLAN.md) | Kế hoạch đấu trường riêng và lời thoại 30 đối thủ (chờ duyệt) | Khi chốt quyết định hoặc làm xong bước nào |
| [docs/TRANSITION_PLAN.md](docs/TRANSITION_PLAN.md) | Kế hoạch chuyển cảnh liền mạch thay cho màn chờ (bước 1–2 đã làm) | Khi chốt quyết định hoặc làm xong bước nào |
| [docs/DIALOG_PLAN.md](docs/DIALOG_PLAN.md) | Kế hoạch hộp thoại và thông báo ra dáng game (đã làm, còn vài phần trang trí) | Khi chốt quyết định hoặc làm xong bước nào |
| [docs/DAILY_GIFT_PLAN.md](docs/DAILY_GIFT_PLAN.md) | Kế hoạch quà mỗi ngày thật, vòng 7 ngày (đã làm) | Khi chốt quyết định hoặc làm xong bước nào |
| [docs/SPAR_PLAN.md](docs/SPAR_PLAN.md) | Kế hoạch Võ đài hằng ngày với đối thủ đã hạ (đã duyệt, chưa làm) | Khi chốt quyết định hoặc làm xong bước nào |
| [docs/UI_REDESIGN_PLAN.md](docs/UI_REDESIGN_PLAN.md) | Kế hoạch nâng cấp giao diện theo hướng sổ tập/phòng gym | Khi chốt mẫu thị giác hoặc hoàn thành một giai đoạn |
| [docs/CRAZYGAMES.md](docs/CRAZYGAMES.md) | Mô tả, điều khiển, hướng dẫn (tiếng Anh) để nộp CrazyGames; file ảnh bìa, video; cách quay lại video | Khi thêm tính năng hoặc đổi giao diện |
| [assets/PROMPTS.md](assets/PROMPTS.md) | Prompt tạo ảnh, nhạc, hiệu ứng âm thanh; giữ phong cách thống nhất | Khi cần ảnh hoặc âm thanh mới |

Khi đối chiếu cân bằng, lấy `index.html` làm nguồn cho hành vi đang chạy. Ngưỡng cân, thời gian đấu và thưởng thắng lấy từ hằng số khi hiển thị. Một số chi tiết trong `T.vi.g` và `T.en.g` ghi số trực tiếp, như mệt mỏi 40/70/100, ±0,3 kg, 40 thể lực và 68–72 kg.

## Cấu trúc

- `index.html`: toàn bộ game (CSS, HTML, JS thuần). Không build, không thư viện. Script chia mục bằng chú thích `// ============ Tên mục ============`: Dữ liệu, Trạng thái + lưu, Công thức, Hiển thị, Âm thanh, Thao tác, Một ngày, Khởi động + vòng lặp.
- `assets/original/<nhóm>/*.png`: ảnh gốc do chủ dự án tạo. `assets/<nhóm>/*.webp`: ảnh game dùng, sinh ra bởi `assets/build.py`, không sửa tay. Nhóm: `char` (nhân vật theo hạng), `bg` (nền), `icon` (bài tập), `pet`, `rival`, `food`, `scene` (màn chờ), `ui` (icon giao diện `ui-*`, `tab-*`). Nhạc: `assets/music/*.mp3` game dùng; file gốc WAV (nếu có) ở `assets/original/music/`, đổi sang MP3 bằng ffmpeg (`ffmpeg -i original/music/x.wav -b:a 192k music/x.mp3`), không qua `build.py`. Tiếng khách và giọng: gốc ở `assets/original/sfx/`, game dùng `assets/sfx/*.mp3` (cắt khoảng lặng hai đầu, mono 96 kbps: `ffmpeg -i original/sfx/x.wav -af "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse" -ac 1 -b:a 96k sfx/x.mp3`). `original/store` (ảnh bìa, logo, video xem trước cho CrazyGames) không build và không nằm trong game.
- `tools/sim.py`: mô phỏng nhịp chơi theo ngày để cân bằng.
- `tools/dist.py`: đóng gói bản upload vào `dist/` (không đưa vào git). Server xem thử `dist`, cổng 8767.
- `tools/qa/`: kiểm thử Playwright trên mã nguồn hoặc gói ZIP, xem lệnh trong [kế hoạch kiểm thử](docs/TEST_PLAN.md#kiểm-tra-tự-động).
- `tools/video/`: quay bằng Playwright (`record.js`) và dựng (`build.py`) trailer CrazyGames cùng clip mạng xã hội. Đoạn quay thô ở `tools/video/raw/`, không đưa vào git.
- `prototype/`: bản thử ban đầu, không còn dùng.
- `.claude/launch.json`: server xem thử tên `game`, cổng 8766.

## Lệnh

Game không có bước build ứng dụng: mở `index.html` qua server local để chạy (không nên mở trực tiếp bằng `file://`). Mở terminal tại thư mục gốc dự án rồi chạy:

```powershell
python -m http.server 8766 --bind 127.0.0.1
```

Mở `http://localhost:8766/` trên trình duyệt. Dừng server bằng `Ctrl+C`. Trong VS Code cũng có thể chạy cấu hình `game` trong `.claude/launch.json`.

Chỉ cần build lại ảnh khi có ảnh gốc mới hoặc ảnh gốc đã thay đổi:

```bash
python assets/build.py
```

Lệnh trên chỉ build ảnh mới hoặc ảnh gốc mới sửa (so thời gian sửa file). Đổi code nén trong `build.py` thì build lại tất cả: `python assets/build.py --all`.

Mô phỏng cân bằng:

```bash
python tools/sim.py
```

Đóng gói bản upload CrazyGames với `index.html` và ảnh/nhạc đã build vào `dist/gym-god.zip`.

```bash
python tools/dist.py
```

Xem thử: mở server `game` (preview) rồi vào `http://localhost:8766/?v=N`, tăng `N` mỗi lần để tránh cache.

Chế độ thử: `http://localhost:8766/?test` nhân 100 calo mỗi cú bấm (hằng `TEST`), hiện nhãn đỏ "TEST x100". Chỉ có tác dụng trên localhost. Tiến trình vẫn lưu vào bản lưu thật.

## Kiến trúc trong `index.html`

- **Trạng thái**: một object `s`, mặc định từ `fresh()`. Lưu bằng `save()` qua `store()` (CrazyGames `SDK.data` nếu có, không thì `localStorage`), khoá `gymgod-save`. `load()` chỉ nhận từng trường hợp lệ. Thêm trường mới thì thêm vào cả `fresh()` và `load()`.
- **An toàn bản lưu** (tiến trình là thứ quan trọng nhất của game): `gymgod-save-bak` là bản dự phòng ghi mỗi sáng và trước khi lên đời; bản chính hỏng hoặc mất thì `load()` dùng bản dự phòng. `gymgod-save-old` giữ trạng thái ngay trước khi xoá tiến trình. Không lưu gì trước khi `ready`. Đăng nhập CrazyGames giữa chừng thì ngừng lưu (trang sẽ tự tải lại với dữ liệu tài khoản). Chờ SDK tối đa 15 giây để không rơi sang bộ nhớ máy. Mọi thay đổi chạm tới `save`/`load` phải chạy lại nhóm A trong TEST_PLAN.
- **Vòng lặp**: tick 100 ms cộng calo theo thời gian thực, cập nhật tiến trình và phần hiển thị cần thiết qua `refresh(false)`. Tự lưu mỗi 5 giây.
- **Hiển thị**: `buildTexts()` dựng lại HTML khi đổi ngôn ngữ; `drawDay()` phần đổi theo ngày/màn; `refresh()` cập nhật tiến trình trước khi vẽ; vòng lặp gọi `refresh(false)` để chỉ cập nhật HUD và phần động của tab đang mở. `ui()` chỉ hiển thị.
- **Chữ**: mọi chuỗi hiển thị nằm trong `T = {vi, en}`, lấy bằng `tr(key)`. Thêm chuỗi phải thêm cả hai ngôn ngữ.
- **Icon**: chuỗi vẫn viết emoji; `rich(text)` đổi các emoji trong bảng `ICO` thành ảnh `assets/ui/*.webp`. Chỗ cập nhật mỗi tick dùng `put(el, text)` thay cho `textContent`. Thêm icon mới: thêm ảnh vào `original/ui` và một dòng vào `ICO`.
- **Màn**: `s.scene` = `office | gym | home`, đổi bằng `go(scene)`. Người chơi chuyển màn qua `door(nơi, mid)`: cửa khép, gọi `mid` (thường là `go`) lúc cửa kín, rồi mở; trong lúc đó cờ `moving` chặn khách ghé và hướng dẫn, xong thì `sceneTips()`. Đi ngủ là `sleepNight()`: cảnh đêm tại nhà, `commitMorning()` đổi ngày và lưu cả ngày mới lẫn màn văn phòng lúc trời tối, rồi `door('office', …, true)` gọi `arrive()`. `endDay()` = `arrive(nextDay())` không hoạt ảnh (vắng hơn 24 giờ). Hoạt ảnh chuyển cảnh chạy qua `play()` để chạm tua x6 được. Thi đấu là lớp `#arena` che cả khung (không đổi `s.scene`): `startDuel()` → VS → `talk()` → `countdown()` → `fight()` → `duelEnd()`; `stopDuel()` đóng lại. Thoại ở `T.*.rv`.
- **Hạng**: `updateRank()` thay đổi `s.rk` và được gọi khi đồng bộ hạng hoặc khi lưu buổi sáng. Tính năng mở theo `unl()` (hạng cao nhất từng đạt).
- **Âm thanh**: hiệu ứng tạo bằng code: `beep` (nốt), `noise` (tiếng ồn lọc: thịch, va chạm, vút), gộp trong `sfx`, đi qua bộ nén `ac.fx`, tối đa 16 tiếng cùng lúc. Ba tầng thưởng: tiếng nhỏ (`buy`, `eat`, `pick`) < `ding`/`coin` < `up` (chỉ dành cho lên hạng, thắng trận, lên đời). Rung bằng `buzz(ms)`; nhạc nền là `assets/music/<tên>.mp3`, phát qua `music(name)`, và `tune()` chọn bài theo màn (`office`, `home`; phòng tập theo hạng: `gym` hạng 1–3, `gym2` 4–6, `gym3` 7–9), `duel` khi đấu, `sleep` khi ngủ. Đoạn nhạc thưởng `rankup`, `win`, `lose` phát qua `sting(name, fb)` theo nấc Âm thanh, tải sẵn ở cú chạm đầu; chưa tải xong hoặc thiếu file thì dùng tiếng bíp `fb`. Giọng và tiếng khách (`assets/sfx/`) phát qua `vox(loại)`, chọn ngẫu nhiên trong số biến thể ghi ở bảng `VOX`; thêm biến thể = thêm file và sửa số trong `VOX`. Nhạc chỉ bắt đầu sau cú chạm đầu tiên. Âm lượng `s.vm` (nhạc) và `s.vs` (hiệu ứng), 0–10 nấc, mặc định 5 và 7, chỉnh trong khung cài đặt ⚙️ (`#setBox`, `drawSet()`), đổi ra độ lợi trong `setVol()`. Khung cài đặt cũng chứa nút ngôn ngữ.
- **Hướng dẫn**: danh sách mục `GUIDE` (kèm hạng cần để mở), chữ trong `T.*.g`. `guide(keys)` mở khung; `coach(...keys)` hiện mục lần đầu người chơi gặp và ghi vào `s.tips`. Thêm tính năng mới thì thêm một mục và gọi `coach` ở chỗ người chơi gặp nó lần đầu.
- **Hộp và thông báo**: quyết định dùng `ask({title, text, yes, ok, no, lose, keep})` (`no: null` = một nút); việc nhỏ dùng `twice(nút, việc)` (bấm hai lần). Thông báo: `toast()` dải nhỏ, `banner()` băng rôn lớn, `later(f)` chờ cửa/hướng dẫn/hộp khác đóng rồi mới chạy. Không dùng `confirm()`/`alert()` vì bị chặn trong iframe của cổng game.
- **SDK**: `CG` là `null` khi không có CrazyGames; mọi lời gọi SDK phải chịu được `CG === null`.

## Kiểm tra trên trình duyệt: các bẫy đã dính

- **Đợi game tải xong** trước khi đụng trạng thái: `while (!ready) await ...`. Bản lưu tải bất đồng bộ (SDK có thể mất tới 4 giây).
- **Bản lưu trên tab xem thử là bản lưu thật của chủ dự án.** Trước khi thử: `const keep = JSON.stringify(s)`. Thử xong, trong `finally`: `s = Object.assign(fresh(), JSON.parse(keep)); shown = -1; syncRank(true); buildTexts(); go(s.scene); save();`. Làm trọn trong một lần gọi JS đồng bộ (không `await` giữa chừng), kẻo tự lưu 5 giây ghi trạng thái thử đè lên.
- Chủ dự án có thể đang chơi trên cùng tab: không để trạng thái thử tồn tại qua nhiều lần gọi.
- Thử những gì đổi ngày, đổi bản lưu nhiều bước (đi ngủ, lên đời…) ở `http://127.0.0.1:8766/`: khác nguồn với `localhost` nên có bản lưu riêng, không đụng tiến trình thật.
- Khung trình duyệt bị ẩn thì hoạt ảnh đứng hoặc chạy chập chờn: đo bằng số (thời gian, style tính toán) thay vì tin ảnh chụp.
- Không gán `duel = {...}` để thử: vòng tick sẽ cho thắng thật (cộng trận thắng và thưởng vào bản lưu).
- Bấm nhân vật cần cú bấm thật (`ev.isTrusted`, tối đa 20 lần/giây); `$('hero').click()` bị bỏ qua. Các nút khác bấm bằng `.click()` được.
- Thử cả khung máy tính và điện thoại (375×812) khi đổi bố cục.
- Mọi ảnh đều có phương án dự phòng (emoji hoặc nền màu), nên thiếu ảnh game vẫn chạy; hiện tại không còn ảnh nào thiếu, thấy 404 là có lỗi đường dẫn.
