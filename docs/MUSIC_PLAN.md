# Kế hoạch: nhạc nền theo giai đoạn

Trạng thái: **đợt 1 đã vào game** (5 bài trong `assets/music/`, hàm `music()`/`tune()` trong `index.html`). Còn lại: bước 6 và đợt 2. Hiện game chỉ có hiệu ứng âm thanh ngắn tạo bằng code (`beep()`, `sfx`), không có nhạc.

## Mục tiêu

Mỗi màn có nhạc riêng để người chơi cảm được nhịp một ngày: uể oải ở văn phòng, hưng phấn ở phòng tập, thư giãn ở nhà, căng thẳng khi thi đấu.

## Danh sách nhạc

| File | Khi nào phát | Cảm giác | Độ dài |
|---|---|---|---|
| `office.mp3` | Màn văn phòng | Lo-fi chậm, hơi buồn ngủ, tiếng gõ phím nhẹ | Lặp 60–90 giây |
| `gym.mp3` | Màn phòng tập | Nhịp nhanh, trống điện tử, tạo hứng bấm | Lặp 60–90 giây |
| `home.mp3` | Màn nhà | Ấm, nhẹ, guitar hoặc piano buổi tối | Lặp 60–90 giây |
| `duel.mp3` | Trong 15 giây thi đấu | Dồn dập, căng | Lặp 15–30 giây |
| `sleep.mp3` | Chuỗi màn chờ khi đi ngủ (8,5 giây; từ ngày 4 còn 3,4 giây, chạm để bỏ qua) | Hộp nhạc ru ngủ rồi sáng dần | Một đoạn 9 giây, không lặp |

Nhạc đã phản ứng theo lối chơi (làm bằng code, không cần file): nhỏ lại ~1,5 giây khi lên hạng/thắng/thua (`duck()`), đục đi khi mở hướng dẫn hoặc hộp xác nhận (`muffle()`), nhanh x1,08 trong 5 giây cuối trận.

Đợt 2 (sau khi đợt 1 chạy ổn): `gym2.mp3` mạnh hơn cho hạng 4–6, để nhạc phòng tập "lớn lên" cùng nhân vật; đoạn nhạc ngắn khi lên hạng và khi thắng trận (hiện đang là tiếng bíp).

## Nguồn nhạc

Chủ dự án tạo bằng công cụ tạo nhạc AI (như Suno, Udio) theo prompt, giống cách đã làm với ảnh. Trước khi dùng phải kiểm tra điều khoản của công cụ có cho dùng thương mại không (thường cần gói trả phí), vì game sẽ đăng lên CrazyGames.

Không tạo nhạc bằng code: làm được nhưng nghe như máy chơi game 8-bit, không hợp phong cách ảnh hiện tại.

## Kỹ thuật

- **File**: `assets/music/*.mp3`, 96 kbps, mỗi file khoảng 0,7–1 MB, cả bộ dưới 4 MB. Không qua `build.py`.
- **Tải lười**: chỉ tải một bài khi lần đầu vào màn đó, để không làm chậm lần tải game đầu (CrazyGames chấm điểm tốc độ tải).
- **Lặp không hở**: phát bằng WebAudio (`AudioBufferSourceNode`, `loop = true`) thay cho thẻ `<audio>`, vì mp3 phát lặp bằng `<audio>` bị khựng ở chỗ nối. Game đã có sẵn `AudioContext` (`ac`) cho hiệu ứng âm thanh.
- **Chuyển bài**: trong `go(scene)` và `startDuel()/stopDuel()`, làm mờ bài cũ 0,5 giây rồi lên bài mới. Một hàm `music(name)` duy nhất.
- **Âm lượng**: nhạc khoảng 30% để không át tiếng bấm.
- **Im lặng đúng lúc**: tắt nhạc khi nấc nhạc `s.vm` = 0, khi có quảng cáo (`adOn`), khi CrazyGames bật `muteAudio`, và khi tab bị ẩn. Đây là yêu cầu bắt buộc của CrazyGames.
- **Chính sách tự phát của trình duyệt**: nhạc chỉ bắt đầu sau cú bấm đầu tiên của người chơi (nút "Đến phòng tập" là đủ). Màn văn phòng lúc mới mở game sẽ im lặng cho tới cú bấm đầu.

## Quyết định đã chốt

1. **Âm lượng**: khung cài đặt ⚙️, nhạc và hiệu ứng mỗi loại 0–10 nấc, mặc định 3 và 5 (thay cho nút loa 3 trạng thái trước đây).
2. **Nhạc theo hạng** (`gym2.mp3` cho hạng 4–6): để đợt 2.
3. **Màn chờ ngắn** (đi đến phòng tập, về nhà, 2 giây): không có nhạc riêng, chỉ làm mờ chuyển bài.

## Các bước

1. ~~Chốt quyết định.~~ Xong.
2. ~~Viết prompt tạo nhạc.~~ Xong: `assets/PROMPTS.md` Phần 4.
3. ~~Chủ dự án tạo 5 bài, thả vào `assets/music/`.~~ Xong.
4. ~~Viết `music(name)` và nối vào `go()`.~~ Xong. Âm lượng tự cân theo độ to thật của từng file (hằng `LOUD`), nên file to nhỏ khác nhau vẫn nghe đều.
5. ~~Nối thi đấu và chuỗi đi ngủ; nút tắt tiếng 3 trạng thái; xử lý quảng cáo, tab ẩn.~~ Xong.
6. Thử trên máy tính và điện thoại thật (chính sách tự phát trên iOS khắt khe nhất), đo dung lượng tải.

## Rủi ro

- **iOS Safari** có thể chặn `AudioContext` cho tới khi có cú chạm; đã tính trong bước 6.
- **Nhạc lặp gây mệt** khi chơi lâu: bài phòng tập nghe nhiều nhất nên cần dài nhất và ít giai điệu nổi bật.
- **Dung lượng**: nếu cả bộ vượt 4 MB thì giảm xuống 64 kbps mono cho bài văn phòng và nhà.
