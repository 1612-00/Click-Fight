# Nộp game lên CrazyGames

Chữ để dán vào form nộp game (tiếng Anh) và danh sách file đi kèm. Đổi luật hay thêm tính năng thì sửa lại phần mô tả cho khớp.

## Tên game

Gym God

## Description

Every great body starts with one push-up. Gym God is a clicker about a burnt-out office worker who finally decides to get in shape. Tap to train, buy workouts, beat your coworkers in tapping duels and glow up through 9 ranks, from Burnt-out Office Worker to superpowered Guardian of Earth.

Each in-game day follows a simple routine: leave the office, train at the gym until your stamina runs out, pick a dinner at home and go to sleep. A day takes about two to three minutes, so it fits a coffee break.

Features:

- Tap to earn calories and spend them on 8 workouts, from water-bottle curls to jogging to work. Calories per second keep coming even when you stop tapping.
- 9 ranks, each with a new look for your character, from office slump to superpowers. To rank up you have to train every muscle group, not just one.
- 30 rivals in 6 leagues, from Tom from Accounting to Earth's super villains like the Cobra Queen and the Core King. Every fight happens in its own arena with a VS intro and dialogue, and the villains slowly reveal who is behind humanity's laziness. Every win gives a permanent calorie bonus.
- Perfect reps: time your tap when the ring turns gold for x5, and chain PERFECTs up to x10.
- Office events every day: drinks with the boss, a broken elevator, lunch with your crush. Every choice has a cost.
- Visitors drop by the gym: your coach always brings a gift, your crush might smile at you or ignore you, and a coworker's birthday cake is tasty but adds weight.
- Choose your dinner: healthy food helps you lose weight, protein boosts tomorrow's calories, junk food gives the most stamina but adds weight.
- Fatigue and rest days, a weekly training goal and a weigh-in every 30 days.
- 8 gym buddies to collect, daily quests and 19 achievements.
- Ascend to start over and earn Stars that boost your calories forever, then spend them on a 9-skill Star tree.
- Four challenges after rank 6: hands only, a gym price hike, wedding season and a boss who takes your calories. Beat them for permanent rewards.
- Progress is saved to your CrazyGames account.
- Play in English or Vietnamese.

## Controls

- Click or tap the character: train (each tap costs 1 stamina)
- When the outline flashes "Perfect rep coming": a white ring will shrink around the character; wait until it turns gold, then tap for a PERFECT rep
- Click or tap buttons: buy workouts, fight rivals, pick a meal, go home, go to sleep
- Hold a buy button: keep buying
- Esc: close the guide

Works with mouse and touch. No keyboard needed.

## How to play

1. At the office, press "Go to the gym".
2. Tap the character to earn calories. Each tap costs 1 stamina, and stamina refills every morning. When a visitor pops up, tap them before they leave, or let them go if the risk isn't worth it.
3. Buy workouts in the Training Log. Reach every muscle target to rank up; tap the rank bar to jump to the next workout to buy.
4. Out of stamina? Go home, pick a dinner and sleep to start the next day.
5. Use the Rivals, Buddies, Quests and Awards tabs to manage the rest of your progress. Beat rivals for permanent bonuses; when progress slows, ascend for Stars.

Tap the ? button in the game for the full guide.

## Gói upload

**Không upload cả thư mục dự án** (khoảng 340 MB: `.git`, ảnh gốc PNG, video bìa). CrazyGames sẽ báo lỗi tải file, và game nặng hơn 20 MB không được lên trang chủ điện thoại (hơn 50 MB thì bị từ chối). Game thật chỉ cần `index.html` và ảnh/nhạc đã build, khoảng 6 MB.

```bash
python tools/dist.py
```

Lệnh này tạo `dist/gym-god.zip` (upload file này) và thư mục `dist/gym-god/` cùng nội dung. Muốn chơi thử đúng gói đó: mở server `dist` (preview), cổng 8767; bộ nhớ riêng nên không đụng bản lưu ở cổng 8766. Chạy lại lệnh mỗi lần sửa game hoặc thêm ảnh.

## File đi kèm

| File | Dùng cho | Yêu cầu của CrazyGames |
|---|---|---|
| `assets/original/store/cover-1920x1080.png` | Ảnh bìa ngang | 16:9, 1920×1080 |
| `assets/original/store/cover-800x1200.png` | Ảnh bìa dọc | 2:3, 800×1200 |
| `assets/original/store/cover-800x800.png` | Ảnh bìa vuông | 1:1, 800×800 |
| `assets/original/store/video-landscape.mp4` | Video ngang | 1080p 16:9, 15–20 giây, ≤ 50 MB, không tiếng |
| `assets/original/store/video-portrait.mp4` | Video dọc | 1080p 2:3, như trên |

Ba ảnh bìa trên được thu phóng (lanczos) từ ảnh gốc `cover-wide.png` (1672×941), `cover-tall.png` (1024×1536), `cover-square.png` (1254×1254); ảnh gốc đổi thì tạo lại:

```bash
cd assets/original/store
ffmpeg -y -i cover-wide.png -vf "scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080" cover-1920x1080.png
ffmpeg -y -i cover-tall.png -vf "scale=800:1200:force_original_aspect_ratio=increase:flags=lanczos,crop=800:1200" cover-800x1200.png
ffmpeg -y -i cover-square.png -vf "scale=800:800:force_original_aspect_ratio=increase:flags=lanczos,crop=800:800" cover-800x800.png
```

Video: 1920×1080 và 1080×1620, 17,1 giây, khoảng 10 MB, H.264, không tiếng.

## Làm lại video

Khi giao diện đổi, quay lại bằng hai bước (server xem thử `game` phải đang chạy):

1. Playwright MCP: `browser_run_code_unsafe` với `filename` = `tools/video/record.js`. Mỗi cảnh chạy trong một ngữ cảnh trình duyệt mới nên không đụng bản lưu thật.
2. `python tools/video/build.py`: ghép ảnh bìa (1 giây) với 5 đoạn gameplay (lột xác lên hạng 2, thắng một trận đấu, ăn tối rồi đi ngủ, sáng hôm sau, thần gym hạng 6), ghi đè hai file video ở trên.

Playwright cần ffmpeg ở `%LOCALAPPDATA%\ms-playwright\ffmpeg-1013\ffmpeg-win64.exe`; trên máy này đã chép ffmpeg của hệ thống vào đó.

Video tuân theo luật CrazyGames: khung đầu là ảnh bìa, không tua nhanh, không màn hình đen (các màn chờ tối của chuỗi đi ngủ đã bị cắt bỏ), không con trỏ chuột, không chữ quảng cáo.

Nguồn: [CrazyGames: Game covers](https://docs.crazygames.com/requirements/game-covers/), [Requirements](https://docs.crazygames.com/requirements/intro/).
