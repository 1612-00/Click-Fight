# Nộp game lên CrazyGames

Chữ để dán vào form nộp game (tiếng Anh) và danh sách file đi kèm. Đổi luật hay thêm tính năng thì sửa lại phần mô tả cho khớp.

## Tên game

Gym God

## Description

Every great body starts with one push-up. Gym God is a clicker about a burnt-out office worker who finally decides to get in shape. Tap to train, buy workouts, beat your coworkers in tapping duels and glow up through 9 ranks, from Burnt-out Office Worker to superpowered Guardian of Earth.

Each in-game day follows a simple routine: leave the office, train at the gym until your stamina runs out, then go home and sleep. Dinner becomes available at rank 2, and can be picked before bed. A day takes about two to three minutes, so it fits a coffee break.

Features:

- New players start at the office. The scene fades in, then Biscuit the dog appears to introduce the game before guiding the player through the first workout in a five-step narrated chat, using the same dialogue-box style as rival fights. More features unlock gradually as they rank up.
- Tap to earn calories and spend them on 8 workouts, from water-bottle curls to jogging to work. Calories per second keep coming even when you stop tapping.
- 9 ranks, each with a new look for your character, from office slump to superpowers. To rank up you have to train every muscle group, not just one.
- Unlock dinner, gym visitors, perfect reps and the rewarded stamina boost on CrazyGames at rank 2; fatigue, weekly goals and office events at rank 3.
- Unlock 30 rivals and daily quests at rank 4, then 8 gym buddies and 19 achievements at rank 5. Rivals appear in 6 leagues, from Tom from Accounting to Earth's super villains. Every fight has its own arena and dialogue; every win gives a permanent calorie bonus.
- Choose dinner after it unlocks: healthy food helps you lose weight, protein boosts tomorrow's calories, and junk food gives more stamina but adds weight.
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
2. Tap the character to earn calories. Each tap costs 1 stamina, and stamina refills every morning. Gym visitors and perfect reps unlock at rank 2.
3. Buy workouts in the Training Log. Reach every muscle target to rank up; tap the rank bar to jump to the next workout to buy.
4. Out of stamina? Go home and sleep to start the next day. Dinner unlocks at rank 2.
5. Keep ranking up to unlock events, rivals, quests, buddies and achievements. Ascend when you have earned a Star; challenges unlock at rank 6.

Tap the ? button in the game to hear Biscuit's short tips for unlocked features.

## Gói upload

Gói upload chỉ cần `index.html` và ảnh/nhạc đã build. Lệnh đóng gói in ra dung lượng thực tế của gói. Xem [giới hạn tải của CrazyGames](https://docs.crazygames.com/requirements/technical/#file-size-count-limits) để đối chiếu khi nộp.

```bash
python tools/dist.py
```

Lệnh này tạo `dist/gym-god.zip` (upload file này) và thư mục `dist/gym-god/` cùng nội dung. Muốn chơi thử đúng gói đó: mở server `dist` (preview), cổng 8767; bộ nhớ riêng nên không đụng bản lưu ở cổng 8766. Chạy lại lệnh mỗi lần sửa game hoặc thêm ảnh.

Trước khi upload, chạy `npm --prefix tools/qa run test:zip` để kiểm tra chính gói ZIP. Xem [cài Chromium và chạy bộ test](TEST_PLAN.md#kiểm-tra-tự-động).

## File đi kèm

| File | Dùng cho | Yêu cầu của CrazyGames |
|---|---|---|
| `assets/original/store/cover-1920x1080.png` | Ảnh bìa ngang | 16:9, 1920×1080 |
| `assets/original/store/cover-800x1200.png` | Ảnh bìa dọc | 2:3, 800×1200 |
| `assets/original/store/cover-800x800.png` | Ảnh bìa vuông | 1:1, 800×800 |
| `assets/original/store/video-landscape.mp4` | Video ngang | 1080p 16:9, 15–20 giây, ≤ 50 MB, không tiếng |
| `assets/original/store/video-portrait.mp4` | Video dọc | 1080p 2:3, như trên |

Clip mạng xã hội nằm ở `assets/original/store/video-social.mp4`. Bản này dọc 9:16, có âm thanh và chữ tiếng Anh.
Nếu cần đăng video ngang ở kênh khác, dùng `assets/original/store/video-landscape-with-sound.mp4` với nhạc và âm báo của game.
Hai bản có lời dẫn tiếng Anh dành cho mạng xã hội là `assets/original/store/video-social-voiceover.mp4` (dọc) và `assets/original/store/video-landscape-voiceover.mp4` (ngang).

Ba ảnh bìa trên được thu phóng (lanczos) từ ảnh gốc `cover-wide.png` (1672×941), `cover-tall.png` (1024×1536), `cover-square.png` (1254×1254); ảnh gốc đổi thì tạo lại:

```bash
cd assets/original/store
ffmpeg -y -i cover-wide.png -vf "scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080" cover-1920x1080.png
ffmpeg -y -i cover-tall.png -vf "scale=800:1200:force_original_aspect_ratio=increase:flags=lanczos,crop=800:1200" cover-800x1200.png
ffmpeg -y -i cover-square.png -vf "scale=800:800:force_original_aspect_ratio=increase:flags=lanczos,crop=800:800" cover-800x800.png
```

## Làm lại video

Chạy các lệnh sau từ thư mục gốc để quay lại theo giao diện hiện tại. Bước quay dùng Chromium đã cài theo [kế hoạch kiểm thử](TEST_PLAN.md#kiểm-tra-tự-động). Bước dựng cần `ffmpeg`, `ffprobe` và font Segoe UI Bold trên Windows.

```powershell
node tools/video/record.js
python tools/video/build.py
```

Mỗi cảnh được quay ở một phiên trình duyệt riêng. Hai trailer CrazyGames mở bằng ảnh bìa, sau đó chiếu cảnh tan ca, mua bài Tay, lên hạng, thắng trận và nhân vật hạng 6 ở tốc độ gốc. Clip mạng xã hội mở bằng cảnh hạng cao và dùng nhạc cùng âm báo lên hạng, thắng trận của game.

Nguồn: [CrazyGames: Game covers](https://docs.crazygames.com/requirements/game-covers/), [Requirements](https://docs.crazygames.com/requirements/intro/).
