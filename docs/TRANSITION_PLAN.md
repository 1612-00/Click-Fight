# Kế hoạch: chuyển cảnh liền mạch

Trạng thái: **bước 1–2 đã vào game** (`door()` trong `index.html`), dùng ảnh `bg-door-gym`, `bg-door-home`; `bg-door-office` đã có, sẽ dùng ở bước 3 (sáng hôm sau tới văn phòng). Còn lại: bước 3–5.

## Vấn đề hiện tại

`travel(steps, done)` trong `index.html` phủ lớp `#wait` tối (`#26352ee8`) lên cả khung, hiện một ảnh `assets/scene/scene-*.webp`, một dòng chữ "Đi đến phòng tập..." có dấu chấm chạy, rồi chờ hết giờ:

| Chuyển cảnh | Thời gian (ngày 1–3) | Từ ngày 4 |
|---|---|---|
| Văn phòng → phòng tập | 2 giây | 0,8 giây |
| Phòng tập / văn phòng → nhà | 2 giây | 0,8 giây |
| Đi ngủ → văn phòng (4 màn: Khò khò → Buổi sáng → Đi đến công ty → Đang làm việc) | 8,5 giây | 3,4 giây |

Vì sao có cảm giác "chờ tải" thay vì đang ở trong game:

1. **Thế giới biến mất.** Nền, nhân vật, thanh calo, thể lực bị che tối hoàn toàn; người chơi nhìn một tấm ảnh rời rạc giữa màn hình.
2. **Không có chuyển động nối hai màn.** Màn cũ tắt, màn mới bật kèm chớp trắng (`#flash`); không có hướng đi, không có nhân vật di chuyển.
3. **Thời gian không mang thông tin.** Chữ và dấu chấm giống thanh tải. Kết quả của ngày (cân giảm, mệt mỏi, hồi thể lực) chỉ hiện thành thông báo *sau khi* đã tới văn phòng.
4. **Chỉ có hai lựa chọn: chờ hoặc bỏ qua.** Chạm là cắt ngang, không có trạng thái ở giữa.

## Mục tiêu

- Chuyển cảnh là một **hành động trong thế giới game** (cửa đóng rồi mở, đèn tắt rồi trời sáng) chứ không phải màn hình tải; không còn lớp phủ tối kèm chữ "...".
- Chuyển cảnh ngắn: đi tập / về nhà **khoảng 0,9 giây**, qua đêm **khoảng 2,5 giây** (khi không có gì đặc biệt).
- Thời gian chuyển cảnh **kể lại điều vừa xảy ra**: thể lực đầy lại, cân nặng thay đổi, ngày mới trên lịch.
- Chạm trong lúc chuyển cảnh = **tua nhanh** tới cuối (không cắt cụt), trạng thái game giống hệt khi xem hết.
- Không thêm thư viện; chỉ dùng CSS transform/opacity và Web Animations (`motion()` đã có), chạy mượt trên điện thoại.
- `prefers-reduced-motion`: thay bằng làm mờ chéo (crossfade) 200 ms, giữ nguyên thông tin.

## Thiết kế

### 1. Đi tập / về nhà: cửa đóng rồi mở (~0,9 giây)

Không dùng nhân vật bước đi (đã chốt). Thay bằng hai cánh cửa vẽ bằng CSS, không cần ảnh mới:

1. **0–300 ms**: hai cánh cửa trượt từ hai mép vào giữa, khép lại. Tiếng cửa lùa rồi tiếng "cạch" khi chốt (`noise()` lọc thấp + `beep` ngắn), rung nhẹ `buzz()`.
2. **300–500 ms**: cửa đóng kín; trên cửa có biển tên nơi đến ("🏋️ PHÒNG TẬP", "🏠 NHÀ", "🏢 VĂN PHÒNG", hai ngôn ngữ). Lúc này mới gọi `go(scene)` để đổi màn và nhạc (`tune()`), nên người chơi không thấy màn đổi đột ngột.
3. **500–900 ms**: cửa mở sang hai bên, kèm tiếng cửa mở; màn mới đã sẵn sàng phía sau.

Kiểu cửa theo nơi đến: phòng tập là cửa kính khung kim loại, nhà là cửa gỗ ấm, văn phòng là cửa kính văn phòng. Cùng một hoạt ảnh, chỉ đổi ảnh và biển, nên chỉ có một đoạn code.

**Ảnh cửa** (nên có để đẹp hơn): `bg-door-gym`, `bg-door-home`, `bg-door-office` trong `assets/original/bg/`, prompt ở `assets/PROMPTS.md` Nhóm 16. Mỗi ảnh là một cửa đôi đang đóng, khe giữa nằm đúng giữa ảnh; game cắt đôi theo khe đó, mỗi cánh mang một nửa ảnh. Biển tên nơi đến vẽ bằng CSS đè lên giữa, nên đổi được theo ngôn ngữ. Thiếu ảnh thì dùng cửa vẽ bằng CSS (màu và viền theo kiểu cửa), nên làm bước 1 không cần chờ ảnh.

Thanh trên cùng (HUD: calo, hạng) nằm trên lớp cửa, nên vẫn thấy được trong lúc chuyển cảnh.

Bỏ chớp trắng `#flash` khi đổi màn (vẫn giữ cho lên hạng).

### 2. Qua đêm: "đêm trôi qua" ngay tại nhà (~2,5 giây)

Thay chuỗi 4 màn chờ bằng một cảnh liền trong căn nhà:

1. **Tắt đèn** (0–400 ms): lớp màu xanh đêm phủ dần *trên nền*, không che HUD; nhạc `sleep.mp3` bắt đầu. "Zzz" bay lên từ nhân vật.
2. **Đêm trôi** (400–1600 ms): thanh ⚡ thể lực đầy dần từ số còn lại lên tối đa; mệt mỏi giảm. (Lịch tuần `#wk` chỉ có ở văn phòng: khi tới văn phòng, ô hôm qua mới được đóng dấu 💪/💤 bằng hoạt ảnh.) Các ảnh `scene-sleep`, `scene-morning`, `scene-commute` hiện thành **khung truyện nhỏ** trượt qua góc màn (kiểu dải truyện tranh), không chiếm cả màn.
3. **Bình minh** (1600–2100 ms): lớp đêm chuyển cam rồi tan; cân nặng hiện số mới bằng hiệu ứng đếm (vd. 84,6 → 84,3 kg, màu xanh khi giảm).
4. **Đi làm** (2100–2500 ms): cửa văn phòng đóng rồi mở như mục 1, sau đó hiện thông báo ngày mới như hiện nay.

Kéo dài thêm chỉ khi có chuyện đáng xem (lên hạng qua đêm, cân kiểm tra 30 ngày, tổng kết tuần): khung truyện tương ứng giữ thêm ~1 giây. Bỏ quy tắc "3 ngày đầu chạy đủ, sau đó còn 40%".

### 3. Chạm để tua nhanh

- Chạm trong lúc chuyển cảnh: mọi hoạt ảnh còn lại chạy x4 (đặt `playbackRate` của các Animation), không nhảy cóc.
- Vẫn giữ khoá 400 ms đầu để cú bấm vừa rồi không vô tình tua.
- Trong lúc chuyển cảnh: chặn bấm nhân vật, mua bài, mở tab (như hiện nay `#wait` đang chặn), nhưng bằng `pointer-events` trên khung thay vì lớp phủ.

### 4. Kỹ thuật

- Một hàm `shift(to, beats)` trả về `Promise`, dựng từ `motion()`; `travel()` giữ tên cho các chỗ gọi hiện có (`go`, `rest`, `goHome`, `sleep`) để thay đổi gọn.
- Trạng thái game đổi **một lần, đúng một chỗ** như hiện nay (`go(scene)`, `endDay()`); hoạt ảnh chỉ trình bày, không quyết định kết quả. Lưu (`save()`) giữ nguyên thời điểm.
- Hoạt ảnh huỷ an toàn nếu có trận đấu, lên đời, xoá tiến trình hoặc tab bị ẩn giữa chừng (`finish()` mọi Animation rồi gọi `done`).
- Khách ghé (`ptShow`), hướng dẫn (`coach`) và thông báo chỉ hiện sau khi chuyển cảnh xong (hiện đang chặn bằng `$('wait').hidden`; đổi sang một cờ `moving`).
- Tải trước `bg1–3` (đã tải `bg3`, thêm `bg1`, `bg2`) để nền mới hiện ngay khi cửa mở.
- Có thể bỏ `#wait` sau khi xong; giữ lại làm phương án dự phòng cho reduced motion nếu crossfade không đủ rõ.

## Các bước

| Bước | Nội dung | Ảnh mới? |
|---|---|---|
| 1 | Cửa đóng/mở có biển nơi đến, cho đi tập / về nhà / về văn phòng; dùng ảnh cửa nếu có, không thì cửa CSS; bỏ `#flash` khi đổi màn | Nên có: 3 ảnh cửa (PROMPTS Nhóm 16) |
| 2 | Chạm để tua x4, cờ `moving` thay cho `#wait` ở các chỗ kiểm tra | Không |
| 3 | Đêm trôi qua: lớp đêm/bình minh, thể lực đầy dần, cân đếm số, khung truyện nhỏ dùng ảnh `scene-*` | Không |
| 4 | Âm thanh: cửa lùa, chốt cửa, tắt đèn, chim sáng (`noise`/`beep`); nếu tiếng tổng hợp chưa đạt thì thêm file vào `assets/sfx/` qua `vox()` | Không (tuỳ chọn file âm thanh) |
| 5 | Reduced motion, điện thoại 375×812, máy tính; cập nhật GAME_DESIGN (mục Màn chờ), TEST_PLAN nhóm B, MUSIC_PLAN (độ dài `sleep.mp3`), CRAZYGAMES (quay lại video) | Không |

Bước 1–2 đã đủ bỏ cảm giác "màn tải"; bước 3 là phần đắm chìm nhất.

## Cần chủ dự án quyết định

1. **Qua đêm**: làm ngay trong căn nhà như mục 2 (đề xuất), hay giữ ảnh `scene-*` toàn màn nhưng đổi thành dải truyện trượt liên tục?
2. ~~Ảnh bước đi~~: **đã chốt** không dùng; thay bằng cửa đóng/mở kèm âm thanh.
3. **Độ dài**: 0,9 giây / 2,5 giây có hợp không, hay muốn ngắn hơn nữa cho người chơi lâu năm?

## Không làm

- Không đổi luật, con số, thời điểm lưu hay phần thưởng.
- Không thêm thư viện hoạt ảnh, không canvas/WebGL.
- Không chặn người chơi lâu hơn hiện nay ở bất kỳ chuyển cảnh nào.
