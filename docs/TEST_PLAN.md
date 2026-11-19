# Bộ test thủ công cho Gym God

Mỗi dòng là một bài test: làm theo cột **Bước**, so với cột **Kết quả mong muốn**. Đánh dấu Đạt/Lỗi vào cột cuối. Khi lỗi, ghi lại mã bài test, điều thấy được và ảnh chụp màn hình.

Con số trong file này lấy từ `docs/GAME_DESIGN.md`. Nếu đổi luật hay con số thì sửa cả hai.

## Kiểm tra tự động

Cài Playwright cho công cụ QA một lần với Node.js và npm. Lệnh kiểm tra ZIP còn cần Python để giải nén.

```powershell
npm --prefix tools/qa ci
npm --prefix tools/qa run install:browser
```

Sau đó chạy từ thư mục gốc dự án:

```powershell
npm --prefix tools/qa test
python tools/dist.py
npm --prefix tools/qa run test:zip
```

Bộ test kiểm tra cú pháp JavaScript trước khi chạy Chromium giả lập cảm ứng 375×812. Mỗi ca dùng bộ nhớ riêng. Bộ test đi hết ngày đầu bằng thao tác thật, tải lại trước và sau khi lưu buổi sáng, khôi phục khi bản chính hỏng (A12), nhận quà ngày 7 rồi tải lại (Q2), kiểm tra yêu cầu ảnh lúc khởi động và sau khi mở Thi đấu (N24), rồi đo các thay đổi DOM khi ẩn tab đó. Chế độ `test:zip` giải nén chính `dist/gym-god.zip` vào thư mục tạm và báo lỗi nếu HTML trong gói lệch mã nguồn.

Các ca này chạy với SDK CrazyGames vắng mặt. Kiểm tra quảng cáo, tài khoản và thiết bị thật theo nhóm P và phần chơi thử bên dưới.

Khi sửa giao diện iPhone hoặc cách tải ảnh, chạy thêm `npm --prefix tools/qa run install:webkit` một lần và `npm --prefix tools/qa run test:webkit`. Có thể dùng `npm --prefix tools/qa run test:zip -- --webkit` để kiểm tra gói phát hành bằng WebKit. Module quảng cáo trong ca bố cục được giả lập chỉ để hiện nút.

## Lần chạy gần nhất

Ngày 2026-11-15, chạy bằng script trên trình duyệt (cửa sổ 1024×768, tablet 768×1024, điện thoại 375×812 giả lập).

- **Đạt**: A1, A3–A6, B1–B8, C1–C4, C6, D1–D6, E1–E10, F1–F7, G1–G9, H1–H8, I1–I7, J1–J9, K1–K5, L1–L9, M7, N1–N7, O1–O4, P1, P3, P4.
- **Lỗi tìm được và đã sửa**: E2 (thông báo thành tựu đè mất thông báo lên hạng và mở khoá); N5 (màn đấu trên điện thoại chỉ thấy đầu nhân vật, không thấy đối thủ; ô thông số văn phòng bị xuống dòng; màn nhà trên điện thoại không thấy nhân vật).
- **2026-11-16, bổ sung** (bộ nhớ riêng ở `127.0.0.1`): A1, N8, G5, H7, I3–I6, O3 đều **đạt**. Tìm và sửa: ô Mệt mỏi hiện ở phòng tập khi mới hạng 1 (CSS `.pill` đè thuộc tính `hidden`).
- **2026-11-16, nhóm 2**: B9–B12 **đạt** (ngày 1 về nhà 2,0 giây, ngày 5 đi tập 0,8 giây, đi ngủ 3,4 giây; cuộn tới thẻ Lưng).
- **Chưa chạy được bằng script, cần người thử**: A2 (nhìn câu nói đổi), C5 (auto-click thật), M1–M6 và M8–M10 (phải nghe), K4 (tỉ lệ độ hiếm khi gọi nhiều lần), P2 (bỏ ngang quảng cáo), P5–P7 (cần CrazyGames), R1–R6 (chơi thật bấm đồng hồ), và mọi thứ trên điện thoại thật.

## Chuẩn bị

1. Mở server xem thử rồi vào `http://localhost:8766/`. Muốn chơi nhanh thì dùng `http://localhost:8766/?test` (mỗi cú bấm x100 calo, góc dưới trái có nhãn đỏ "TEST x100"). Các con số calo trong bộ test ghi theo **chế độ thường**; ở chế độ test thì calo mỗi cú bấm nhân 100.
2. Mở bảng điều khiển của trình duyệt (F12 → Console) để dán các lệnh hỗ trợ bên dưới. Các lệnh này chỉ để nhảy nhanh tới tình huống cần thử, không phải cách chơi thật.
3. **Sao lưu bản lưu thật trước khi test**, vì test sẽ ghi đè tiến trình.

| Việc | Lệnh dán vào Console |
|---|---|
| Sao lưu | `localStorage.setItem('backup', JSON.stringify(s))` |
| Khôi phục | `s = Object.assign(fresh(), JSON.parse(localStorage.getItem('backup'))); shown = -1; syncRank(true); buildTexts(); go('office'); save()` |
| Chơi mới từ đầu (tiếng Việt) | `s = fresh(); s.lang = 'vi'; shown = -1; syncRank(true); buildTexts(); go('office'); coach('intro'); save()` |
| Sang ngày mới, coi như đã tập hết thể lực | `s.used = s.cap; endDay()` |
| Sang ngày mới, coi như nghỉ | `s.used = 0; endDay()` |
| Đặt cấp bài tập (ví dụ đủ hạng 2) | `Object.assign(s.lv, {tay: 5, vai: 4, nguc: 2}); syncRank(); ui()` |
| Đổi một chỉ số rồi vẽ lại | ví dụ `s.fat = 50; go('office')` |
| Cho thêm calo | `s.cal += 1e6` |

Cấp bài tập để đạt từng hạng (dán vào `Object.assign(s.lv, {...})`):

| Hạng | Cấp cần |
|---|---|
| 2 | `tay: 5, vai: 4, nguc: 2` |
| 3 | `tay: 12, vai: 10, nguc: 5, bung: 1` |
| 4 | `tay: 22, vai: 18, nguc: 14, bung: 8, mat: 3` và cân ≤ 84,5 kg |
| 5 | `tay: 40, vai: 35, nguc: 30, bung: 22, mat: 15, chan: 10, lung: 3` và cân ≤ 82 kg |
| 6 | `tay: 70, vai: 60, nguc: 55, bung: 48, mat: 40, chan: 40, lung: 32, cardio: 20` và cân ≤ 78 kg |

Môi trường cần thử: máy tính (cửa sổ rộng hơn 900px), tablet dọc (768×1024), điện thoại (375×812), và ít nhất một điện thoại thật.

---

## A. Khởi động và lưu

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| A1 | Chạy lệnh "Chơi mới từ đầu". | Màn chơi hiện bằng hiệu ứng nhẹ; Bắp xuất hiện rồi dẫn chuyện qua năm bước: giới thiệu game trước, hướng dẫn thao tác sau. Khi hoàn tất, focus ở nút "Đến phòng tập". Bấm nút đó: sang phòng tập, Bắp hướng dẫn tập luyện. Calo 0, Thể lực 300 / 300; chưa thấy cân nặng hay mệt mỏi, chỉ có tab Bài tập. Tải lại trang: phần mở đầu không tự hiện lại. | |
| A2 | Tải lại trang (F5) 5 lần. | Câu nói ở văn phòng thay đổi giữa các lần (có 8 câu, có thể trùng). Các thông số không đổi. | |
| A3 | Vào phòng tập, bấm 20 cú, mua 1 cấp Tay. Đợi 6 giây rồi tải lại trang. | Mở lại ở **văn phòng** (không phải phòng tập). Calo, cấp Tay và thể lực còn lại giữ nguyên như trước khi tải lại. | |
| A4 | Về nhà (chưa ngủ), đợi 6 giây, tải lại trang. | Mở lại ở **nhà**, vẫn cùng ngày, nút "Đi ngủ" còn đó. | |
| A5 | Tải lại trang rồi bấm thật nhanh vào bất kỳ nút nào trong 1–2 giây đầu. | Không mất tiến trình: sau khi game tải xong, số liệu vẫn như trước khi tải lại. (Nếu kịp bấm "Đến phòng tập" thì vẫn được sang phòng tập, đó là bình thường.) | |
| A6 | Mở Console, xem có dòng đỏ nào không trong suốt buổi test. | Không có lỗi đỏ (Uncaught…), không có 404. | |
| A7 | Ngủ sang ngày mới. Làm hỏng bản chính: `store().setItem(KEY, '{hong')`, rồi tải lại trang. | Game tải bản dự phòng: đúng ngày vừa sang, đúng hạng, trận thắng, calo của sáng hôm đó. Không bị về ván mới. | |
| A8 | Xoá bản chính: `store().removeItem(KEY)`, tải lại trang. | Như A7: tải bản dự phòng, không về ván mới. Sau 5 giây bản chính được ghi lại. | |
| A9 | Mở ⚙️, giữ nút "Giữ để xoá toàn bộ tiến trình" đủ 1,5 giây, rồi chạy `JSON.parse(store().getItem(OLD)).day` | Thanh đỏ chạy ngang nút; đủ 1,5 giây thì menu đóng và game về ván mới, nhưng lệnh trả về ngày của ván cũ: trạng thái trước khi xoá vẫn còn để cứu nếu lỡ tay. | |
| A12 | Ở màn nhà, bấm Đi ngủ và tải lại trang trước khi ngày đổi. Làm lại, lần này tải lại sau khi thể lực đầy nhưng trước lúc cửa văn phòng mở. Lặp lại lần hai với bản lưu chính bị hỏng. | Trước khi ngày đổi: vẫn ở nhà, đúng ngày cũ. Sau khi ngày đổi: ở văn phòng, đúng một ngày mới, thể lực đã hồi; bản dự phòng cũng mở ở văn phòng. Nếu qua ngưỡng cân nặng trong đêm, hạng mới vẫn được giữ. | |

## S. Hướng dẫn và mở tính năng

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| S1 | Xoá tiến trình trong bộ nhớ test rồi tải lại trang. | Ván mới mở ở văn phòng; màn hiện nhẹ, Bắp xuất hiện rồi giới thiệu game trước khi hướng dẫn thao tác qua năm bước. Đóng chat thì nút "Đến phòng tập" nhận focus; vào phòng tập mới hiện mẹo tập. Tải lại không tự mở phần mở đầu hoặc nhắc ngày trùng nội dung. | |
| S2 | Hạng 1, xem các tab và chỉ số ở phòng tập và ở nhà. | Chỉ có Bài tập ở phòng tập; không có cân nặng, mệt mỏi, nước tăng lực, đối thủ, nhiệm vụ, bạn tập, thành tựu hay thử thách. Về nhà không có bảng bài tập hay bữa tối; chỉ hiện nút đi ngủ. | ✓ cục bộ |
| S3 | Dùng `s = Object.assign(fresh(), {rk:1,best:1}); shown=1; buildTexts(); go('home')`. | Hạng 2 mở bữa tối; lời dẫn không gợi ý chọn món ở hạng 1. Vào phòng tập có thể gặp khách và Rep hoàn hảo. Nước tăng lực chỉ hiện trên CrazyGames. Thi đấu, Nhiệm vụ, Bạn tập và Thành tựu vẫn ẩn. | ✓ cục bộ |
| S4 | Lặp S3 với `rk` và `best` lần lượt bằng 2, 3, 4, 5. Ở hạng 3 đặt `s.ev=EV[0].k; drawDay()`. | Hạng 3 mở mệt mỏi/lịch tuần/sự kiện; hạng 4 mở Thi đấu/Nhiệm vụ và cân nặng (ở nhà chỉ có tab Nhiệm vụ); hạng 5 mở Bạn tập/Thành tựu (ở nhà có Bạn tập và Nhiệm vụ, không có Bài tập); hạng 6 mở Thử thách. | ✓ cục bộ |
| S5 | Bấm ❓ ở hạng 1 rồi ở hạng 5; đổi ngôn ngữ và mở lại. | Chỉ hiện câu của tính năng đã mở, theo từng bước chat, chữ đúng ngôn ngữ; không liệt kê mục bị khoá. | ✓ cục bộ |
| S6 | Mở hướng dẫn tại 375×812, 768×1024 và 1024×768 bằng cả hai ngôn ngữ; thử Tab/Shift+Tab, Enter, Esc và bấm nền. | Hộp thoại kiểu đấu trường, chó con, lời dẫn, chỉ báo bước và nút không bị cắt hay tràn ngang; nút Tiếp tục nhấp nhẹ. Tab/Shift+Tab chuyển focus giữa Tiếp tục và ✕; Esc và bấm nền không đóng hay chuyển bước; chỉ Tiếp tục/Đã hiểu mới tiến lên. | ✓ cục bộ |
| S7 | Ván mới, lần đầu về nhà ở 375×812 và 1440×900. | Nền nhà hiện ngay và phủ trọn khu vực chơi; ở hạng 1 không có bảng bài tập hay thẻ bữa tối, lời dẫn chỉ chỉ người chơi đi ngủ. | |
| S8 | Tạo bản lưu hạng 1 ngày 1 chưa bấm/tập nhưng có `s.play = 60` và `s.tips.intro = 1` (bản lưu cũ), chưa có `s.tips.start`; tải lại trang. | Phần mở đầu năm bước vẫn hiện; thời gian tab mở và cờ intro cũ không bị hiểu nhầm là đã xem phần mở đầu mới. | |
| S10 | Mở hướng dẫn, bấm nền và Esc ở giữa một mục; sau đó bấm Tiếp tục đến hết. | Bấm nền và Esc không làm mất hướng dẫn. Tiếp tục chuyển từng bước; bước cuối đóng và lưu trạng thái đã xem. | ✓ cục bộ |
| S11 | Ở hạng 6, bấm ❓ rồi bấm ✕ ở bước 2. Với hướng dẫn tự hiện lần đầu (vd. tab Thi đấu), bấm ✕ giữa chừng. | ❓: khung đóng ngay, không cần bấm hết các bước. Tự hiện: khung đóng, mục đang xem được ghi là đã xem, mục chưa tới sẽ hiện lại lần sau. | |
| S9 | Hạng 3, về nhà khi chưa xem mẹo nhà/bữa tối/mệt mỏi; qua một mẹo rồi đóng chat. Về nhà lần nữa. | Chỉ các mẹo đã xem được đánh dấu; mẹo chưa xem vẫn hiện ở lần gặp tiếp theo, không bị mất vì đóng sớm. | |
| A10 | Trên CrazyGames, chơi khi chưa đăng nhập, rồi đăng nhập giữa chừng. | Trang tự tải lại. Nếu tài khoản chưa từng chơi game: tiến trình khách được chuyển sang tài khoản. Nếu tài khoản đã có tiến trình: hiện tiến trình của tài khoản, không bị bản khách ghi đè. | |
| A11 | Trên CrazyGames, đăng nhập, chơi một ngày, rồi mở game trên máy hoặc trình duyệt khác cùng tài khoản. | Cùng tiến trình ở cả hai nơi (có thể trễ tới 30 giây sau lần lưu cuối). | |

## B. Vòng ngày và chuyển cảnh

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| B1 | Ở văn phòng, bấm "Đến phòng tập". | Hai cánh cửa kính khung thép khép lại từ hai bên, tiếng cửa lùa rồi "cạch"; biển "🏋️ PHÒNG TẬP" hiện trên cửa; cửa mở ra, cả lượt khoảng 1 giây. Không còn màn chờ tối hay chớp trắng. Trong lúc đó không bấm được gì. Sau đó vào phòng tập: nền phòng gym, có số calo lớn, các ô thể lực/cân nặng, bảng bài tập bên phải. | |
| B2 | Ở phòng tập, còn thể lực, bấm "Về nhà" một lần rồi chờ 3 giây. | Không có hộp hỏi. Nút đổi chữ thành "Chắc chưa? Bấm lần nữa", viền vàng, lắc nhẹ; vẫn ở phòng tập. Sau 3 giây nút trở lại "Về nhà". | |
| B3 | Bấm "Về nhà" hai lần liền (trong 3 giây). | Cửa gỗ có biển "🏠 NHÀ" đóng rồi mở (khoảng 1 giây), rồi vào nhà: nền căn hộ buổi tối, nút "Đi ngủ", bảng bên phải chỉ có tab Bạn tập. | |
| B4 | Ở nhà, bấm "Đi ngủ". | Tiếng công tắc, căn nhà tối dần (thanh chỉ số, HUD vẫn sáng; lời nhắc, bữa tối và nút Đi ngủ ẩn đi), "Zzz" bay lên; thanh ⚡ đầy dần, ô ngày đổi sang ngày mới; ba khung truyện Khò khò → Buổi sáng → Đi đến công ty hiện lần lượt; tiếng chim, trời cam rồi sáng; cửa văn phòng có biển "🏢 VĂN PHÒNG" đóng rồi mở. Tới văn phòng: số ngày tăng 1, thông báo "Ngày N" kèm dòng cân nặng. Mỗi khung truyện đứng khoảng 1 giây, cả lượt khoảng 6,5–7 giây; sau hơn 1 giây hiện dòng "Chạm để tua nhanh" ở dưới. Không còn màn chờ tối. | |
| B5 | Ở văn phòng, bấm "Về nhà nghỉ" một lần rồi chờ 3 giây. | Nút đổi thành "Chắc chưa? Bấm lần nữa" rồi trở lại; vẫn ở văn phòng. | |
| B6 | Bấm "Về nhà nghỉ" hai lần liền (mệt mỏi dưới 40 hoặc chưa mở mệt mỏi). | Cửa nhà đóng rồi mở, vào nhà, thông báo "Tiếc quá, lại một ngày không luyện tập!". | |
| B7 | Ở nhà nhìn bảng bên phải; ở phòng tập nhìn bảng bên phải. | Ở nhà chỉ có tab Bạn tập. Ở phòng tập có Bài tập, Thi đấu, Nhiệm vụ, Thành tựu, Lên đời và **không có** tab Bạn tập. | |
| B8 | Ở văn phòng, bấm vào nhân vật nhiều lần. | Không có gì xảy ra: calo không tăng, thể lực không giảm. | |
| B9 | Ở phòng tập, bấm tới hết thể lực rồi bấm "Về nhà". | **Không** có hộp hỏi, vào thẳng cửa về nhà. | |
| B10 | `s.day = 5; go('office')`, bấm "Đến phòng tập"; sau đó về nhà và bấm "Đi ngủ". | Cửa đi tập vẫn khoảng 1 giây như ngày 1; qua đêm vẫn khoảng 6,5–7 giây như ngày 1 (không còn rút ngắn theo ngày). | |
| B12 | Bấm "Đến phòng tập", chạm vào cửa khi nó đang khép. Lần sau chạm ngay khi bấm nút. Bật giảm chuyển động của hệ điều hành rồi thử lại. | Chạm giữa chừng: cửa đóng/mở nhanh hơn hẳn nhưng vẫn đủ các bước, vào phòng tập bình thường. Chạm ngay (dưới 0,25 giây): không tua. Giảm chuyển động: cửa hiện và mờ tại chỗ, không trượt. Hướng dẫn tập (lần đầu) chỉ hiện sau khi cửa mở xong. | |
| B11 | Bấm "Đi ngủ", chạm vào căn nhà tối sau khoảng 0,5 giây. Lần sau chạm ngay khi vừa bấm. | Chạm sau 0,5 giây: đêm, bình minh và cửa văn phòng chạy nhanh x6 (cả lượt khoảng 1,5 giây) nhưng đủ các bước, sang ngày mới bình thường. Chạm ngay (dưới 0,25 giây): không tua. Trong lúc đêm không bấm được tab hay nút nào. | |
| B12 | Ở phòng tập, nhìn bảng Bài tập; bấm vào thanh hạng trên cùng. | Đúng một thẻ có viền vàng phát sáng: bài rẻ nhất còn thiếu mục tiêu hạng kế (ván mới: Tay; Tay đủ 5 thì sang Vai). Bấm thanh hạng: mở tab Bài tập, cuộn tới thẻ đó, thẻ nảy nhẹ. Ở văn phòng bấm thanh hạng không làm gì. Hạng cao nhất hoặc chỉ còn thiếu cân nặng: không thẻ nào viền vàng. | |
| B13 | Ngày 1 và lúc mở game ở văn phòng khi chưa có sự kiện. Đi ngủ sang ngày 2. | Ngày 1: câu nói thường, không có nút sự kiện. Sáng ngày 2: khung câu nói viền vàng "📌 …", hai nút lựa chọn ghi tác dụng; lần đầu hiện mục hướng dẫn "📌 Sự kiện văn phòng". | |
| B14 | Bấm một lựa chọn (vd "Sếp rủ làm vài ly" → "Đi cho sếp vui"). | Thông báo tên lựa chọn và tác dụng. Cân +0,3 kg, calo cộng đúng số ghi trên nút. Hai nút biến mất, khung về câu nói thường. Tải lại trang: không hiện lại sự kiện. | |
| B15 | Lựa chọn may rủi (Crush rủ ăn trưa → Đi ngay; Bốc thăm). Làm nhiều ngày. | Nút ghi "60%: … · còn lại: …". Thông báo "Thành công: …" hoặc "Không may: …", tác dụng khớp. Bấm hôm nay +30% hiện ở số "mỗi lần bấm" và hết sau khi ngủ. | |
| B16 | Có sự kiện nhưng bấm "Đến phòng tập" luôn. Đi ngủ. Ở hạng 1–2 xem nhiều ngày. | Sự kiện bị bỏ qua, hôm sau có sự kiện khác (không trùng hôm qua). Trước hạng 3 không gặp Yoga, Deadline, Massage (sự kiện về mệt mỏi). | |

## C. Bấm, thể lực, chống auto-click

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| C1 | Chơi mới, vào phòng tập, bấm nhân vật 10 cú. | Mỗi cú: số "+1" bay lên, có tiếng bấm, calo +1, thể lực −1. Sau 10 cú: calo 10, thể lực 290 / 300. | |
| C2 | Chưa mua gì, bấm tới khi có 15 calo lần đầu. | Dòng nhắc dưới nhân vật đổi từ "Bấm vào nhân vật để tập!" thành "Đủ calo rồi, mua bài tập đầu tiên!". Chỉ nút mua Tay nháy nhẹ hai nhịp, các bài tập khác không nháy. | ✓ cục bộ |
| C3 | Bấm cho tới khi thể lực về 0 (chế độ test không giảm số cú cần bấm). | Thể lực 0 / 300. Dòng nhắc "Hết thể lực! Về nhà nghỉ thôi." thành nhãn đỏ viền trắng, to hơn, phồng lên và nhấp nháy liên tục. Nút "Về nhà" nhấp nháy. Bấm nhân vật tiếp: calo không tăng, nút "Về nhà" nảy lên. | |
| C4 | Khi còn thể lực, dán vào Console: `for (let i = 0; i < 200; i++) $('hero').click()` | Calo và thể lực **không đổi** (cú bấm giả bị bỏ qua). | |
| C5 | Dùng phần mềm auto-click hoặc bấm thật nhanh trong 5 giây, đếm thể lực đã mất. | Mất không quá khoảng 100 thể lực trong 5 giây (tối đa 20 cú mỗi giây được tính). | |
| C6 | Đứng yên ở phòng tập khi đã có calo/giây (đã mua Vai). | Calo tự tăng theo calo/giây, thể lực không giảm. Về văn phòng hoặc ở nhà calo vẫn tăng. | |
| C7 | Mở `?test`, vào phòng tập, chờ khoảng 3–12 giây. | Một vòng tròn nhấp nháy, phát sáng hiện trên sân khấu, có nhãn bên dưới; to khoảng 110px trên máy tính, 76px trên điện thoại; không che các nút. Không bấm: sau 8 giây biến mất. | |
| C8 | Bản lưu chưa từng gặp khách: bấm vào khách đầu tiên. | Khách đầu luôn là PT 🧑‍🏫 (vàng, "Bấm tôi!"). Thông báo "PT: Thưởng calo!" kèm số calo. Sau đó hiện mục hướng dẫn "🧑‍🏫 Khách ghé phòng tập". Lần sau không hiện lại. | |
| C9 | Bấm PT nhiều lần cho tới khi gặp đủ ba quà. | Bấm x5: thông báo "PT: Bấm x5!", vầng sáng chuyển cam, số bay lên màu vàng, mỗi cú x5 trong 8 giây. Thêm sức: thể lực +30% tối đa (vd 300 → +90). Thưởng calo: calo tăng đúng số trong thông báo. | |
| C10 | Chờ crush 💃 (hồng, "Bắt chuyện?"). Bấm nhiều lần qua nhiều ngày. | Crush đi từ trái sang phải màn hình trong 8 giây. Khoảng 2/3 số lần: "Crush cười với bạn!" kèm bấm x7 trong 10 giây hoặc calo. Còn lại: "Crush ngó lơ..." có tiếng buồn, thể lực mất 10% số đang có. | |
| C11 | Chờ bánh 🎂 (xanh, "Ăn bánh?"), bấm vào. Lần sau để bánh tự đi. | Bấm: "Bánh sinh nhật đồng nghiệp", calo tăng và cân +0,1 kg. Không bấm: không có gì thay đổi. | |
| C13 | Bản lưu chưa từng bấm khách. Ở phòng tập (`?test`), **không bấm** khách nào, chờ 5–6 khách. | Khách đầu là PT; các khách sau có cả crush 💃 và bánh 🎂. |  |
| C14 | Ở `?test`, ở lì phòng tập, bấm mọi khách (nhất là quà thể lực). | Mỗi ngày tối đa 3 khách; sau khách thứ 3 không còn ai tới, thể lực cạn dần và ngày kết thúc. Tải lại trang không làm khách tới thêm. Sáng hôm sau khách lại tới. | |
| C15 | Ván mới: bấm 20 cú đầu. Bấm tiếp. | 20 cú đầu không có vòng. Sau đó cứ khoảng 25–35 cú: viền đích vàng nhấp nháy 2 giây kèm chữ "Sắp có Rep hoàn hảo, chuẩn bị!" (bấm trong lúc này vẫn tính bình thường), rồi mới hiện vòng trắng co dần với dòng chữ "Đợi vòng vàng rồi bấm!". | |
| C16 | Khi vòng hiện, dừng tay, bấm đúng lúc vòng chuyển vàng. Làm vài lần liên tiếp. | Chữ vàng "PERFECT x5", có tiếng "ting" (mỗi lần liên tiếp cao hơn), cú đó ra gấp 5 calo. Liên tiếp: x6, x7… tối đa x10. Sau lần PERFECT đầu, vòng không còn dòng chữ hướng dẫn. | |
| C17 | Khi vòng hiện, bấm liên tục không dừng; lần khác bấm trễ; lần khác không bấm. | Bấm liên tục hoặc trễ: chữ "Hụt", cú đó x1, chuỗi PERFECT về 0. Không bấm: vòng tự biến mất sau 1,1 giây, chuỗi về 0. Thể lực vẫn trừ 1 mỗi cú như thường. | |
| C18 | Trong trận đấu, trong lúc bấm x5/x7 của khách; khi đang báo trước hoặc vòng đang hiện thì về nhà, thách đấu, hoặc bấm khách cho x5. | Không có vòng trong trận đấu và lúc bấm x5/x7. Vòng biến mất khi rời phòng tập hay bắt đầu đấu. Trên điện thoại vòng tròn đều (không méo), bao quanh nhân vật. | |
| C12 | Khi khách đang hiện: thách đấu, hoặc về nhà. Ở văn phòng, nhà, trong trận đấu, khi mở ❓ thì chờ 2 phút. | Khách biến mất khi bắt đầu đấu hay rời phòng tập. Khách không bao giờ hiện ngoài phòng tập, trong trận đấu, hay khi có khung hướng dẫn / hộp xác nhận / màn chờ. | |
| C20 | Đã thấy nhắc mua Tay ở C2 nhưng chưa mua; tải lại trang, vào phòng tập và để calo vẫn đủ mua Tay. | Nút mua Tay không nháy lần thứ hai; cờ nhắc đã được lưu. | ✓ cục bộ |

## D. Bài tập và mua

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| D1 | Chơi mới, có 15 calo, mua Tay. | Calo −15, Tay "Cấp 1", calo mỗi lần bấm từ 1 lên 2. Giá cấp kế là 17,5 (15 × 1,17). | |
| D2 | Nhìn danh sách khi mới chơi. | Bài chưa đủ gần để mua hiện "???" và hình tối, trừ các bài mà hạng kế tiếp yêu cầu (Tay, Vai, Ngực luôn hiện tên và mục tiêu). Bài tiếp theo lộ ra khi có nửa giá của nó hoặc đã mua bài trước nó. | |
| D3 | Chọn "x10" rồi mua Tay khi đủ calo. | Mua đúng 10 cấp một lần, nút ghi "x10", giá là tổng 10 cấp. Không đủ calo thì nút mờ và có thanh đầy dần. | |
| D4 | Chọn "Tối đa". | Nút ghi số cấp nhiều nhất mua được với số calo đang có (ít nhất x1). Bấm mua: calo còn lại không đủ mua thêm cấp nào của bài đó. | |
| D5 | Đưa Tay lên cấp 25 (lệnh: `s.lv.tay = 24; s.cal += 1e6; ui()` rồi mua 1 cấp). | Trước khi mua thẻ ghi "x2 ở cấp 25". Sau khi mua, calo mỗi cấp của Tay gấp đôi; dòng nhắc mốc đổi thành "x2 ở cấp 50". | |
| D6 | Nhìn dòng mục tiêu trên thẻ bài tập mà hạng kế cần. | Ghi "🎯 hiện tại / mục tiêu" theo đơn vị của bài (kg, cái, phút…), màu hồng khi chưa đạt, màu xanh kèm ✓ khi đạt. | |

## E. Hạng và mở tính năng

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| E1 | Chơi mới. Mua Tay 5, Vai 4, nhưng Ngực chỉ 1. | **Chưa** lên hạng. Thanh hạng ghi "2/3 nhóm cơ". | |
| E2 | Mua Ngực lên 2. | Màn hình loé sáng và rung, tiếng lên hạng, nhân vật đổi hình. Băng rôn tối ngang màn có tia sáng: "LỘT XÁC!" · "Tập tành cho vui · x1,5", tự tắt sau 2,5 giây (chạm để tắt sớm). Cùng lúc, dải nhỏ dưới HUD "Đạt hạng 2 · +1%" (không đè lên băng rôn). Băng rôn tắt thì hiện thẻ "Tính năng mới!" với Bắp và chữ mở khoá, chỉ một nút "Tuyệt!", chờ bấm. Số hạng thành 2. Calo/giây và calo/bấm tăng khoảng 26% (25% của hạng + 1% của thành tựu). | |
| E3 | Sau E2, sang ngày mới. | Thể lực tối đa là 420 (thể lực tối đa chỉ tăng từ sáng hôm sau, không tăng ngay lúc lên hạng). | |
| E4 | Trước hạng 2 về nhà; sau hạng 2 về nhà. | Trước hạng 2: chữ "Về đến nhà rồi. Ngủ một giấc để mai tập tiếp!", không có món ăn. Từ hạng 2: chữ "Tối rồi. Chọn một bữa ăn (hoặc bỏ bữa) rồi đi ngủ." và 3 thẻ món ăn. | |
| E5 | Đạt hạng 3 (Tay 12, Vai 10, Ngực 5, Bụng 1). | Thông báo lên hạng "Gymer nghiệp dư · x1.5" kèm "Mở khoá: mệt mỏi và lịch tuần… Hạng 4 cần cân nặng ≤ 84,5 kg"; hạng 3 giảm 0,3 kg/ngày tập đủ, hạng 4 tăng lên 0,4 kg. Xuất hiện ô Mệt mỏi cạnh thể lực; ở văn phòng xuất hiện 7 ô lịch tuần, dòng "Buổi tập tuần này: n / 5" và ô thông số Mệt mỏi. | |
| E6 | Ở hạng 3, đặt đủ cấp hạng 4 nhưng cân 85 kg: `Object.assign(s.lv, {tay: 22, vai: 18, nguc: 14, bung: 8, mat: 3}); s.kg = 85; syncRank(); ui()` | **Không** lên hạng. Thanh hạng ghi "Giảm thêm 0.5 kg để lên hạng". | |
| E7 | Tiếp E6: `s.kg = 84.5; syncRank(); ui()` | Lên hạng 4 "Body săn chắc · x2". | |
| E8 | Ở hạng 4, tăng cân lại: `s.kg = 95; syncRank(); ui()` | Vẫn ở hạng 4, không bị tụt hạng. | |
| E9 | Đạt hạng 6 (dùng bảng cấp ở phần Chuẩn bị, cân ≤ 78). | Hạng 6 "Thần gym công sở · x3". Thanh hạng ghi "Hạng cao nhất", thanh tiến độ đầy. | |
| E10 | Lên từng hạng 1 → 6, đổi nhân vật bằng nút mặt người trên cùng. | Mỗi hạng một hình khác nhau cho cả nhân vật nam và nữ, nhân vật không bị nhảy vị trí hay đổi cỡ giữa các hạng. | |
| E11 | Lên hạng 7 (`?test`). | "LỘT XÁC!" kèm "Sức mạnh siêu nhân thức tỉnh!". Tên "Siêu nhân văn phòng", vầng sáng hồng. Chưa có ảnh hạng 7 thì nhân vật vẫn là ảnh hạng 6 (không phải hình vẽ đơn giản). Thể lực tối đa không tăng thêm so với hạng 6 (trừ phần Cardio). | |
| E12 | Lên hạng 8, 9. | Tên "Người hùng thành phố" (vầng xanh), "Hộ vệ Trái Đất" (vầng đỏ). Hạng 9 là hạng cao nhất, thanh hạng ghi "Hạng cao nhất". Cân tối đa 74 / 72 kg chặn đúng. | |

## F. Cân nặng

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| F1 | Chơi mới, tập hết 300 thể lực, về nhà, ngủ. | Thông báo "Ngày 2" · "Tập hôm nay: −0.3 kg → 84.7 kg (−0.3)". Ô cân nặng ghi 84.7 kg. | |
| F2 | Tập đúng nửa thanh thể lực (150 cú) rồi về nhà ngủ. | Cân giảm 0,15 kg so với hôm trước (hiển thị làm tròn 1 chữ số). | |
| F3 | Không tập, về nhà nghỉ, ngủ (mệt mỏi dưới 40). | Thông báo "Nghỉ hôm nay: +0.3 kg → … (+0.3)". Cân tăng 0,3 kg. | |
| F8 | Mệt mỏi dưới 40. Vào phòng tập, bấm 5 cú, về nhà ăn Salad cá hồi (−0,2), ngủ. | Sáng hôm sau: "Tập quá ít, tính là nghỉ: +0.3 kg · Ăn uống, sự kiện: −0.2 kg → … (+0.1)". Cân cả ngày +0,1. Mệt mỏi giảm 60 như ngày nghỉ. | |
| F9 | Dùng khoảng 25% thể lực (trên mức 20%), ăn Salad, ngủ. | Tính là ngày tập: "Tập hôm nay: −0.1 kg · Ăn uống, sự kiện: −0.2 kg → … (−0.3)". | |
| F10 | Chọn sự kiện văn phòng có +0,3 kg, tập hết thể lực, ăn món ăn vặt +0,2, ngủ. | "Tập hôm nay: −0.3 kg · Ăn uống, sự kiện: +0.5 kg → … (+0.2)". Số trong ngoặc khớp đúng chênh lệch cân giữa hai buổi sáng. | |
| F11 | Đang thiếu ít cân để lên hạng (ví dụ cần −0,2), tập hết thể lực, ngủ. | Sáng hôm sau: băng rôn "LỘT XÁC!"; tờ ghi chú trên bàn văn phòng đổi tiêu đề thành "BÁO CÁO SÁNG" và có dòng cân (không bị che mất). | |
| F12 | Trong các bản lưu thử riêng ở hạng 1, 4, 5, 6 và 9, đặt cân 85 kg, dùng hết thể lực rồi ngủ. | Dòng "Tập hôm nay" lần lượt giảm 0,3 / 0,4 / 0,5 / 0,6 / 0,9 kg; dùng một phần thể lực thì mức giảm theo đúng tỉ lệ. | |
| F13 | Hoàn thành thử thách Mùa tiệc cưới, đặt hạng 4 và dùng hết thể lực. | Ngày tập đủ giảm 0,5 kg: mức hạng 4 là 0,4 kg, cộng thưởng thử thách 0,1 kg. | |
| F4 | `s.kg = 70; go('gym')` rồi so calo/giây với lúc `s.kg = 75; go('gym')`. | Ở 70 kg (vùng 68–72) calo/giây và calo/bấm cao hơn đúng 20% so với ở 75 kg. | |
| F5 | `s.kg = 91; s.used = 0; endDay()` rồi xem thể lực tối đa; so với khi cân 85. | Trên 90 kg, thể lực tối đa chỉ còn 80% (hạng 1: 240 thay vì 300). | |
| F6 | `s.kg = 68; s.used = s.cap; endDay()` và `s.kg = 120; s.used = 0; endDay()`. | Cân không xuống dưới 68,0 kg (đáy vùng lý tưởng, vẫn được calo +20%) và không vượt 120.0 kg. | |
| F7 | Ở hạng 3, chưa đủ nhóm cơ cho hạng 4, cân 85. | Thanh hạng ghi "n/5 nhóm cơ · ≤ 84.5 kg (−0.5)". Khi cân ≤ 84,5 thì ghi "≤ 84.5 kg ✓". Ở hạng 1 và 2 thanh hạng không nhắc gì tới cân nặng. | |

## G. Mệt mỏi và ngày nghỉ (từ hạng 3)

Trước các bài này: đạt hạng 3, rồi `s.fat = 0; go('office')`.

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| G1 | Ở hạng 1 hoặc 2, tập hết thể lực nhiều ngày liền. | Không có ô Mệt mỏi, thể lực tối đa không bị giảm. | |
| G2 | Hạng 3, mệt mỏi 0, không học Hồi phục nhanh. Tập hết thể lực, ngủ. | Mệt mỏi thành 35 (cộng 40, trừ 5 khi ngủ), trạng thái "Sung sức". Thể lực 540 / 540. | |
| G3 | Tập hết thể lực thêm 2 ngày nữa. | Mệt mỏi thành 70 rồi 100. Ở 70: "Kiệt sức", thể lực tối đa còn 270 (50% của 540); sau ngày tập đủ thứ ba, sáng kế tiếp bắt buộc nghỉ và nút đi tập bị khoá. | |
| G4 | `s.fat = 80; s.used = s.cap * .2; endDay()` (đạt ngưỡng 20% để tính là ngày tập). | Ô mệt mỏi ghi "Kiệt sức". Thể lực tối đa sáng nay còn 50% (hạng 3: 270). | |
| G5 | `s.fat = 100; go('office')` | Câu nói đổi thành "Cơ thể quá tải rồi. Hôm nay bắt buộc phải nghỉ!". Nút "Đến phòng tập" mờ, không bấm được. Chỉ còn "Về nhà nghỉ". | |
| G6 | `s.fat = 50; go('office')`, bấm "Về nhà nghỉ" hai lần, rồi ngủ. | Thông báo khi về nhà: "Nghỉ hôm nay để mai khoẻ hơn." Sáng hôm sau: mệt mỏi 0, cân chỉ +0,1 kg, dòng dưới lịch tuần có "Hồi phục: bấm +25%", calo mỗi lần bấm cao hơn 25% so với bình thường. | |
| G7 | Sau G6, tập rồi ngủ thêm một ngày. | "Hồi phục" biến mất, calo mỗi lần bấm về bình thường. | |
| G8 | `s.fat = 30; go('office')`, nghỉ, ngủ. | Thông báo "Tiếc quá, lại một ngày không luyện tập!". Sáng hôm sau: mệt mỏi 0, cân +0,3 kg, **không** có "Hồi phục". | |
| G9 | So mức cộng mệt mỏi khi tập hết thanh ở hạng 3, 4, 5, 6 (đặt `s.fat = 0` trước mỗi lần, không học Hồi phục nhanh). | Sau một ngày tập đủ: mọi hạng đều lên 35 sau khi trừ 5 qua đêm. | |

## H. Bữa tối (từ hạng 2)

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| H1 | Hạng 2 trở lên, về nhà. | 3 thẻ món ăn: một món lành mạnh, một món đạm, một món ăn vặt. Mỗi thẻ có ảnh, tên, hiệu ứng (màu xanh), thay đổi cân nặng. Không có giá, bấm được kể cả khi có 0 calo. | |
| H2 | Bấm một món. | Món đó viền vàng, hai món kia mờ và không bấm được. Thông báo tên món và hiệu ứng. Cân nặng đổi ngay theo số ghi trên thẻ. | |
| H3 | Sau H2, bấm lại món đã chọn hoặc món khác. | Không có gì xảy ra: mỗi tối chỉ ăn một món. | |
| H4 | Không chọn món nào, bấm "Đi ngủ". | Sang ngày mới bình thường, không có hiệu ứng bữa ăn, cân nặng không đổi vì bữa ăn. | |
| H5 | Về nhà trong 9 ngày liên tiếp (dùng lệnh sang ngày nhanh rồi `go('home')`), ghi lại 3 món mỗi tối. | Thực đơn đổi theo ngày, luôn đủ 3 nhóm. Sau 9 ngày đã gặp đủ cả 9 món; ngày thứ 10 lặp lại như ngày đầu. | |
| H6 | Ăn từng món rồi ngủ, sáng hôm sau so thể lực tối đa và calo với một ngày không ăn. | Khớp bảng dưới đây. Hiệu ứng chỉ kéo dài đúng một ngày. | |
| H7 | Ăn món có "mệt mỏi −10" hoặc "−5" khi mệt mỏi đang là 30. | Mệt mỏi giảm **ngay lúc ăn** còn 20 hoặc 25. Khi mệt mỏi đang là 0 thì vẫn là 0, không âm. | |
| H8 | Ăn Trà sữa mỗi tối và tập hết thể lực mỗi ngày trong 5 ngày. | Cân nặng vẫn giảm 0,1 kg mỗi ngày (−0,3 do tập, +0,2 do ăn), không tăng. | |

Bảng đối chiếu cho H6:

| Món | Cân nặng | Thể lực tối đa hôm sau | Calo/giây hôm sau | Calo/bấm hôm sau | Mệt mỏi ngay |
|---|---|---|---|---|---|
| Cơm gà luộc | −0,1 | +10% | — | — | — |
| Salad cá hồi | −0,2 | +5% | — | — | — |
| Yến mạch chuối | −0,1 | — | — | — | −10 |
| Ức gà, trứng | 0 | — | +25% | +25% | — |
| Bò bít tết | +0,1 | — | +35% | +35% | — |
| Sinh tố whey | 0 | +10% | +10% | +10% | — |
| Trà sữa, gà rán | +0,2 | +50% | +10% | +65% (x1,5 × 1,1) | — |
| Pizza phô mai | +0,25 | +70% | +15% | +15% | — |
| Mì tôm trứng | +0,1 | — | — | +30% | −5 |

## I. Lịch tuần, Chủ nhật, cân kiểm tra (từ hạng 3)

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| I1 | Hạng 3, nhìn 7 ô lịch ở văn phòng qua vài ngày tập và nghỉ. | Ô hôm nay viền vàng. Ngày đã qua hiện 💪 nếu đã dùng từ nửa thanh thể lực trở lên, 💤 nếu ít hơn. Ngày chưa tới hiện T2…CN. Dòng "Buổi tập tuần này: n / 5" đếm đúng số 💪. | |
| I2 | Tập chỉ 40% thanh thể lực rồi ngủ. | Ngày đó hiện 💤 và không được tính là buổi tập. | |
| I3 | `s.week = [1,1,1,1,1,0]; s.day = 7; go('office')`, tập hết thể lực, ngủ. | Thông báo ngày 8 có "Đạt mục tiêu tuần: +10% calo tuần này!". Dòng dưới lịch có "+10% 🔥". Calo/giây cao hơn 10% so với trước. Lịch tuần trống lại cho tuần mới. | |
| I4 | `s.week = [1,0,0,0,0,0]; s.day = 7; go('office')`, tập, ngủ. | Thông báo có "Chưa đạt mục tiêu tuần". Không có "+10%". | |
| I5 | `s.day = 7; go('office')` rồi vào phòng tập, tab Thi đấu. | Dòng dưới lịch có "Chủ nhật: thách đấu miễn phí, thưởng x2". Thách đấu **không trừ** 40 thể lực, kể cả khi thể lực dưới 40 vẫn đấu được. Thắng nhận gấp đôi calo thưởng (đối thủ đầu: 1.800 thay vì 900). | |
| I6 | `s.day = 30; s.kg30 = 85; s.kg = 80.4; go('office')`, tập hết thể lực, ngủ. | Thông báo ngày 31 có "Cân kiểm tra: +2 ⭐". Số Sao tăng 2. | |
| I7 | `s.day = 30; s.kg30 = 85; s.kg = 86; go('office')`, ngủ. | "Cân kiểm tra: +0 ⭐". Sao không đổi, không bị trừ. | |

## J. Thi đấu

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| J1 | Chơi mới, vào tab Thi đấu. | 30 đối thủ có ảnh và tên. Chỉ đối thủ đầu (Anh Tom kế toán) có nút "Thách đấu" bấm được; thẻ ghi "Cần 300 / 15s" và "+3% vĩnh viễn · +900". | |
| J2 | Khi thể lực dưới 40 (không phải Chủ nhật). | Nút "Thách đấu" mờ, không bấm được. | |
| J3 | Thể lực từ 40 trở lên, bấm "Thách đấu" (lần đầu gặp Anh Tom). | Thể lực −40 ngay. Đấu trường che cả màn hình (cả bảng bên phải): nhân vật trượt vào từ trái, đối thủ từ phải, chữ "VS" đập xuống, tên giải và tên đối thủ ở trên. Nhạc đổi sang bài thi đấu. Sau đó khung thoại: Tom nói 1 câu, rồi "Bạn" đáp 1 câu; người đang nói sáng, người kia tối. Chạm khi chữ đang chạy thì hiện hết câu, chạm nữa sang câu kế. Hết thoại: đếm 3·2·1·ĐẤU!, rồi thanh đấu hiện ở trên, đồng hồ 15 giây, thanh đỏ đầy dần đều và đầy đúng lúc hết giờ. | |
| J4 | Trong lúc đấu, bấm liên tục vào đấu trường. Bấm trong lúc đếm ngược. Lần khác không bấm gì. | Chỗ bấm hiện 👊, không có số "+…". Thanh xanh **chỉ nhảy khi nhân vật ra đòn** (lao sang phải, đối thủ giật lùi, số sát thương đỏ trên đối thủ), không quá khoảng 2 đòn mỗi giây, mỗi đòn tối đa 1/5 thanh. Thể lực **không giảm**; **calo không tăng theo cú bấm**. Bấm lúc đếm ngược không tính. Không bấm: nhân vật vẫn tự ra đòn khoảng 0,7 giây một lần. Đối thủ ra đòn khoảng mỗi giây: lao sang trái, nhân vật chớp, màn rung, thanh đỏ nhảy lên một nấc. | |
| J5 | Làm đầy thanh xanh trước khi hết giờ. Đánh cả đối thủ rất yếu (Tom, khi đã mạnh). | Đối thủ nói câu khi thua ("Ơ… chắc anh nhập nhầm ô nào rồi."), chạm xong hiện nút "Về phòng tập" (không có nút Đấu lại). Thông báo "THẮNG!" · "+3% · +900". Calo +900, "Đối thủ đã thắng" tăng 1, calo/giây và calo/bấm tăng 3% (trận đầu tiên tăng 4% vì kèm thành tựu "Thắng 1 đối thủ"). Đối thủ vừa thắng không đấu lại được; đối thủ kế tiếp mở ra (cần 720). Nhạc về bài phòng tập. | |
| J6 | Chế độ thường, vào đấu rồi không bấm gì (khi calo/giây còn thấp). Sau đó bấm "Đấu lại". | Hết 15 giây: "Thua rồi!", có tiếng thua, đối thủ nói câu chế giễu. Hiện "Đấu lại ⚡40" (mờ nếu thiếu thể lực) và "Về phòng tập". Đấu lại: chỉ một câu gặp lại ("Anh sửa lại bảng tính rồi. Lần này hết đường."), rồi đếm ngược luôn. Tải lại trang rồi thách đấu lại: vẫn chỉ câu gặp lại. | |
| J7 | Đang đấu thì hết giờ hoặc thắng, kiểm tra tab Thi đấu. | Khi một trận đang diễn ra, mọi nút "Thách đấu" đều mờ. | |
| J8 | Thắng đủ 30 đối thủ (chế độ test). | "Đối thủ đã thắng 30 / 30". Không còn nút đấu nào bấm được. Nhiệm vụ "Thách đấu 1 lần" tự tính là xong. | |
| J10 | Thắng 20 đối thủ đầu, mở tab Thi đấu. | Có giải 5 "Thế giới ngầm" và giải 6 "Trùm Trái Đất", mỗi giải 5 phản diện. Phản diện 21 cần khoảng 6,3 nghìn tỷ calo, phản diện 30 khoảng 47 nghìn tỷ. Chưa có ảnh thì ô ảnh hiện emoji (🦹‍♂️ 🐍 🧪 …), có ảnh thì hiện ảnh. | |
| J9 | Khi ước chừng đủ sức thắng đối thủ kế tiếp. | Tab Thi đấu có chấm đỏ. | |
| J11 | Chơi nhân vật nữ, đấu Cody (giải 3) và một phản diện giải 5. Đổi sang EN. | Cody gọi "Chị" (nam: "Anh"). Giải 3 có 2 câu, giải 5 có 3 câu trước câu đáp. Nền đấu trường đổi theo giải (chưa có ảnh: nền màu tím, đỏ…). Bản tiếng Anh đủ thoại, không còn chữ tiếng Việt. Trên điện thoại: đối thủ ở trên bên phải, nhân vật dưới bên trái, khung thoại ở dưới, không cuộn ngang. |
| J12 | Đã mạnh hơn hẳn, thách đấu đối thủ đầu (Tom), bấm liên tục. | Trận vẫn kéo dài khoảng 2,5 giây: 5 đòn của bạn (thanh xanh 5 nấc), đối thủ kịp đánh lại khoảng 2 lần, rồi mới thắng. |
| J13 | Đã hạ ít nhất một đối thủ. Trong tab Thi đấu bấm nút "✓ 💬" của đối thủ đã hạ. | Đấu trường mở với màn VS, rồi đủ thoại lần đầu, câu bạn đáp và câu đối thủ nói lúc thua; xong chỉ có nút "Về phòng tập". Thể lực, số trận thắng và calo không đổi; không có đếm ngược hay trận đấu. Nút của đối thủ chưa mở vẫn là 🔒. | |

## K. Bạn tập

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| K1 | Về nhà, có dưới 5.000 calo. | Nút "Gọi bạn tập" giá 5 N, mờ, có thanh đầy dần. 8 thẻ bạn tập đều là "???" với hình tối. | |
| K2 | Có 5.000 calo, bấm "Gọi bạn tập". | Calo −5.000. Một bạn tập hiện ra (ảnh, tên, "Cấp 1"). Dòng tổng trên cùng tăng đúng theo bạn đó (ví dụ Cún: +5% calo/giây). Giá lần gọi kế là 12,5 N. | |
| K3 | Gọi nhiều lần cho tới khi trùng. | Bạn trùng lên "Cấp 2", thưởng gấp đôi. Giá mỗi lần gọi gấp 2,5 lần lần trước (5 N → 12,5 N → 31,25 N…). | |
| K4 | Gọi khoảng 20 lần (chế độ test), nhìn độ hiếm. | Phần lớn là bạn Thường; Hiếm và Sử thi ít; Huyền thoại (Rồng) rất hiếm. Nhãn độ hiếm và tỉ lệ trên thẻ: Thường 20%, Hiếm 7%, Sử thi 5%, Huyền thoại 1%. | |
| K5 | Khi đủ calo để gọi. | Tab Bạn tập có chấm đỏ. | |

## L. Nhiệm vụ, thành tựu, lên đời, xoá tiến trình

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| L1 | Ở hạng 4, đặt ngày 6 (`s.day = 6; refresh()`) rồi vào tab Nhiệm vụ. Lặp lại ở hạng 5. | Hạng 4 chỉ chọn trong 4 loại khả dụng, không có "Gọi bạn tập"; hạng 5 mở đủ 5 loại và ngày 6 có "Gọi bạn tập". Mỗi thẻ có icon, thanh tiến độ và nút thưởng (ít nhất 500 calo). | |
| L2 | Làm xong một nhiệm vụ. | Nút thưởng sáng lên, tab Nhiệm vụ có chấm đỏ. Bấm nhận: calo tăng đúng số ghi trên nút, thông báo "Xong nhiệm vụ!", nút thành ✓, thẻ mờ đi. Bấm lại không nhận lần hai. | |
| L3 | Sang ngày mới. | 3 nhiệm vụ đổi (xoay vòng theo ngày), tiến độ về 0. | |
| L12 | Ở hạng 5, đặt ngày 6, đủ calo để gọi; về nhà, gọi một bạn rồi mở tab Nhiệm vụ trước khi ngủ. | Tab Nhiệm vụ dùng được ở nhà; tiến độ thành 1/1, tab có chấm báo nhận thưởng. Nhận thưởng được một lần, sau đó ngủ sang ngày mới thì nhiệm vụ/tiến độ reset như thường lệ. | |
| L4 | Vào tab Thành tựu. | 19 thành tựu; cái chưa đạt mờ. Đạt một cái (ví dụ bấm 100 lần): thẻ sáng lên, "Thành tựu n / 19" tăng, calo tăng 1%. Phần Thống kê phía dưới hiện đủ 8 dòng và cập nhật theo thời gian. | |
| L5 | Tab Lên đời khi tổng calo kiếm trong đời này dưới 1 triệu. | "Sao nhận nếu lên đời: 0". Nút ghi "Chưa đủ calo để nhận Sao", mờ. | |
| L6 | Kiếm 8 triệu calo trong đời này (chế độ test, hoặc `s.run = 8e6; ui()`). Bấm "Lên đời" → Đồng ý. | Trước khi bấm: "Sao nhận nếu lên đời: 2", tab có chấm đỏ. Hộp kiểu trang sổ rơi xuống (tiếng "bộp"), biển "⭐ Lên đời", câu "Bắt đầu lại từ hạng 1 và nhận 2 Sao.", hai cột **Mất** (Calo, Cấp bài tập, Hạng) / **Giữ** (Sao, kỹ năng, bạn tập, thành tựu, trận thắng, cân nặng). Sau khi đồng ý: băng rôn "⭐ 2", calo 0, mọi bài tập cấp 0, về hạng 1, Sao +2, "Thưởng hiện tại +20%". **Giữ nguyên**: ngày, cân nặng, mệt mỏi, bạn tập, số trận thắng, thành tựu. | |
| L7 | Sau L6 (đã từng đạt hạng 3 trước khi lên đời), về nhà và về văn phòng. | Bữa tối, ô mệt mỏi và lịch tuần **vẫn còn** dù đang ở hạng 1. | |
| L8 | Sau L6, so calo mỗi lần bấm với một ván mới chưa có Sao. | Cao hơn đúng 20% (2 Sao). | |
| L9 | Mở ⚙️, giữ nút xoá 0,5 giây rồi buông; sau đó giữ đủ 1,5 giây. | Buông sớm: thanh đỏ lùi về, không đổi gì. Giữ đủ: mọi thứ về như chơi mới (calo, cấp, Sao, bạn tập, trận thắng, ngày 1, 85 kg), nhưng **giữ** ngôn ngữ, âm lượng và nhân vật đang chọn. Thử cả giữ phím Enter/Space khi nút đang được chọn bằng Tab. Tab Lên đời không còn nút xoá. | |
| L10 | Bản lưu có vài Sao (vd lên đời hoặc cân kiểm tra). Mở tab Lên đời, cuộn xuống "Kỹ năng Sao". | Có dòng "Sao chưa dùng", 3 nhánh x 3 kỹ năng. Kỹ năng thứ 2, 3 mỗi nhánh mờ, nút 🔒, ghi "Cần học … trước". Nút kỹ năng giá 1 bấm được khi có ≥ 1 Sao. | |
| L11 | Học Cú bấm vàng 2 cấp. | Sao chưa dùng giảm 1 rồi 2 (tổng 3). Thưởng "+N%" của Sao **không đổi**. Calo mỗi lần bấm x1,25 rồi x1,5 so với lúc chưa học. Ký ức cơ bắp mở khoá. | |
| L12 | Học Đấu tiết kiệm (cần Phổi thép, Hồi phục nhanh trước). | Nút thách đấu ghi "⚡20", trận đấu chỉ trừ 20 thể lực. Hướng dẫn ❓ mục Thi đấu ghi 20. | |
| L13 | Học Ký ức cơ bắp 1 cấp rồi lên đời. | Đời mới bắt đầu ở hạng 2, Tay 5, Vai 4, Ngực 2. Lên 2 cấp: hạng 3. | |
| L14 | Chưa từng đạt hạng 6: xem mục "Thử thách". Đạt hạng 6 (`?test`). | Trước: "🔒 Mở khi đạt hạng 6", nút 🔒. Lúc lên hạng 6: thông báo mở khoá Thử thách. Sau: 4 thử thách có nút "Bắt đầu"; lần đầu mở tab Lên đời hiện mục hướng dẫn Thử thách. | |
| L15 | Bắt đầu "Sếp soi" → Đồng ý. | Hộp có biển "👔 Sếp soi", luật của thử thách, cột Mất/Giữ. Như lên đời (nhận Sao, calo và cấp về 0). Nhãn hồng "👔 Sếp soi · 🎯 Mục tiêu: đạt hạng 6" dưới thanh calo. Calo/giây và mỗi lần bấm còn khoảng 1/4. Các nút thử thách khác bị khoá, nút này ghi "Đang làm", có link "Bỏ thử thách". | |
| L16 | Đang làm thử thách, đạt hạng mục tiêu (`?test`). | Thông báo "🏅 Hoàn thành thử thách!" kèm thưởng. Nhãn hồng biến mất, thẻ thử thách mờ với ✓. Calo trở lại bình thường và có thêm thưởng vĩnh viễn. | |
| L17 | Từng thử thách: Chỉ dùng tay / Phòng gym tăng giá / Mùa tiệc cưới. | Tay: calo/giây = 0, vắng mặt không cộng calo. Tăng giá: giá bài tập x3 (Tay cấp 0: 45). Tiệc cưới: cân lên ít nhất 85 kg ngay, mỗi sáng thông báo cân có +0,1 kg. | |
| L18 | Đang làm thử thách: bấm "Bỏ thử thách" → Đồng ý. Làm lại, lần này bấm "Lên đời" thường. | Cả hai: nhãn hồng biến mất, luật hết, không có thưởng, thử thách có thể bắt đầu lại. | |
| L19 | Tải lại trang khi đang làm thử thách và đã học kỹ năng. | Kỹ năng, thử thách đang làm, thử thách đã xong giữ nguyên. | |

## M. Âm thanh và nhạc

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| M1 | Mở game, chưa bấm gì. | Im lặng (trình duyệt chưa cho phát tiếng). | |
| M2 | Bấm bất kỳ đâu trong game. | Nhạc văn phòng (chậm, nhẹ) bắt đầu, lên dần trong khoảng nửa giây. | |
| M3 | Đi văn phòng → phòng tập → nhà. | Mỗi màn một bài: phòng tập sôi động, nhà ấm nhẹ. Bài cũ mờ dần rồi bài mới lên, không cắt đột ngột, không có hai bài chồng nhau lâu hơn 1 giây. | |
| M4 | Ở mỗi màn, nghe đủ lâu để bài lặp lại ít nhất 2 lần. | Chỗ nối khi lặp không có khoảng lặng hay tiếng "khựng" rõ rệt. | |
| M5 | Bấm "Đi ngủ". | Đoạn nhạc ru ngủ phát khi trời tối, không lặp; bị cắt khi cửa văn phòng đóng. Về văn phòng thì nhạc văn phòng trở lại. | |
| M6 | So độ to giữa 5 bài, và giữa nhạc với tiếng bấm/tiếng mua. | Các bài to gần bằng nhau. Tiếng bấm, tiếng mua, tiếng lên hạng vẫn nghe rõ trên nền nhạc. | |
| M7 | Ván mới, bấm ⚙️. Thử − và +, bấm thẳng vào một ô, bấm lại đúng ô cuối đang sáng. | Mặc định Nhạc 5 ô sáng, Âm thanh 7 ô. − / + đổi một nấc, không xuống dưới 0, không quá 10. Bấm ô thứ 7: sáng 7 ô; bấm lại ô đó: còn 6. Nhạc to nhỏ ngay khi chỉnh; chỉnh Âm thanh thì nghe một tiếng bấm thử ở mức mới. Nhạc 0: nhạc dừng, tiếng bấm còn. Âm thanh 0: không còn tiếng hiệu ứng, không rung. Bấm ✕, bấm ra ngoài khung hoặc Esc đều đóng. | |
| M8 | Đặt Nhạc 0, Âm thanh 8, tải lại trang. Rồi dán bản lưu cũ có `mute: 2` (hoặc `mute: 1`) vào và tải lại. | Vẫn Nhạc 0, Âm thanh 8. Bản lưu cũ `mute: 2` thành 0 / 0; `mute: 1` thành 0 / 7; không có `mute` thành 5 / 7. | |
| M9 | Đang có nhạc, chuyển sang tab trình duyệt khác rồi quay lại. | Nhạc dừng khi rời tab và phát lại khi quay về. | |
| M10 | Trên điện thoại thật (đặc biệt iPhone/Safari): mở game, chạm một lần. | Nhạc phát được sau cú chạm đầu tiên. Bật chế độ im lặng của máy thì không có tiếng. | |
| M11 | Bấm nhân vật liên tục 20 giây thật nhanh, có PERFECT chen vào. | Tiếng bấm là tiếng "thịch" trầm, mỗi cú hơi khác nhau. Không rè, không vỡ tiếng khi bấm dồn. Cú chí mạng có thêm tiếng "chát" sáng. | |
| M12 | PERFECT liên tiếp 5 lần, rồi trượt một lần, rồi PERFECT lại. | Mỗi lần PERFECT cao hơn lần trước một chút; trượt xong thì về lại nốt thấp nhất. Trên điện thoại: rung nhẹ mỗi lần PERFECT. | |
| M13 | Mua bài tập; ăn ở nhà; chọn sự kiện văn phòng; nhận thưởng nhiệm vụ; đạt một thành tựu; lên hạng. | Ba tầng nghe khác nhau rõ: mua/ăn/chọn là tiếng nhỏ, nhiệm vụ/thành tựu là tiếng "ding"/"xu", lên hạng là đoạn kèn to nhất, nhạc nền nhỏ hẳn lại ~1,5 giây rồi lên lại. | |
| M14 | Bấm "Đến phòng tập". Ngủ sang ngày mới. | Đến phòng tập: tiếng "vút". Sáng ngày mới: 4 nốt đi lên nhẹ nhàng. | |
| M15 | Mở hướng dẫn ❓, hộp xác nhận (ví dụ "Lên đời") hoặc menu ⚙️. Đóng lại. | Khi mở: nhạc nghe đục như vọng từ phòng bên. Đóng: nhạc trong lại. | |
| M16 | Thi đấu, để trận chạy tới cuối. | 5 giây cuối nhạc nhanh hơn một chút; 3 giây cuối có tiếng tích mỗi giây. Đòn của bạn và của đối thủ có tiếng va chạm khác nhau; trên điện thoại rung khi bị đánh. | |
| M17 | Bấm nhân vật liên tục 2 phút đến khi thể lực xuống dưới 20%. | Đúng một tiếng tim đập trầm khi vừa qua mốc 20%, không lặp lại. | |
| M18 | Tải lại trang và chạm ngay khi game còn đang tải (kể cả chạm vào nhân vật). | Không có lỗi trong console. Khi tải xong, nhạc là bài của màn đang hiện (không phải bài phòng tập khi đang ở văn phòng). | |
| M19 | Vào phòng tập ở hạng 1–3, rồi 4–6, rồi 7–9 (dùng `?test` để lên nhanh). | Hạng 1–3: bài điện tử cũ. Hạng 4–6: bài funk có kèn. Hạng 7–9: bài kiểu phim siêu anh hùng. Đúng lúc lên hạng 4 hoặc 7 trong phòng tập: bài đổi ngay, mờ dần sang bài mới. Lên đời về hạng 1: về bài cũ. | |
| M20 | Lên hạng; thắng một trận; thua một trận; lên đời. | Lên hạng và lên đời: đoạn kèn đồng (~5,7 giây). Thắng: đoạn nhạc thắng (~5 giây). Thua: trombone "wah wah" (~4 giây). Trong lúc đó nhạc nền nhỏ hẳn lại, hết đoạn thì lên lại. Đoạn thưởng to nhỏ theo nấc Âm thanh, Âm thanh 0 thì im. | |
| M21 | Chặn file `rankup.mp3` (DevTools → Network → Block request URL), tải lại, lên hạng. | Không lỗi; nghe tiếng bíp lên hạng như trước. | |
| M22 | Ở phòng tập chờ khách: PT, Crush, bánh (dùng `?test` cho khách đến nhanh). | PT hiện: tiếng còi rồi giọng "Hey/Hup/Yeah". Crush đi ngang: giọng "Hi~/Hmm?/cười nhẹ". Bánh: kèn tiệc. Mỗi lần nghe một biến thể ngẫu nhiên. Khách bỏ đi: im lặng. | |
| M23 | Bấm Crush nhiều lần. | Đồng ý: tiếng xu + cười vui hoặc "Ooh!". Ngó lơ: "Hmph!" hoặc "Mm-mm" (không còn tiếng bíp buồn). | |
| M24 | Khi vòng PERFECT bắt đầu co. Thử nhắm mắt, bấm theo tiếng tích. | Có tiếng "vút" nhẹ lúc vòng bắt đầu co, tiếng "tích" đúng lúc vòng chuyển vàng; bấm ngay khi nghe tích thì trúng PERFECT. Bấm sớm (vòng biến mất) thì không còn tiếng tích. | |
| M25 | Đạt chuỗi PERFECT x3, x4, x5… liên tục, với nhân vật nam rồi nữ. | Từ x3: tiếng gắng sức của nhân vật (giọng nam với nhân vật nam, nữ với nhân vật nữ), không quá một lần mỗi 4 giây. | |
| M26 | Âm thanh 0 trong ⚙️, chờ khách. | Không còn tiếng khách, giọng hay tiếng vòng. | |

## N. Giao diện, ngôn ngữ, bố cục

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| N1 | Bấm ⚙️ → "English". | Toàn bộ chữ đổi sang tiếng Anh: tên hạng, tab, bài tập, đối thủ (Tom from Accounting…), món ăn, nhiệm vụ, thành tựu, câu nói, màn chờ. Không còn chữ tiếng Việt sót lại. Nút "English" sáng, tiêu đề khung thành "Settings". Số liệu không đổi. | |
| N2 | Chọn lại "Tiếng Việt", tải lại trang. | Ngôn ngữ được nhớ sau khi tải lại. | |
| N3 | Bấm nút nhân vật (mặt người). | Đổi giữa nhân vật nam và nữ ở đúng hạng hiện tại; lựa chọn được nhớ sau khi tải lại. | |
| N4 | Cửa sổ máy tính rộng hơn 900px. | Nhân vật bên trái, bảng bên phải rộng khoảng 430px. HUD và bảng dùng nền giấy ấm, xanh sage/olive và điểm nhấn hổ phách; đấu trường vẫn tối. Không có thanh cuộn ngang. | |
| N5 | Tablet dọc 768×1024 và điện thoại 375×812, lần lượt ở văn phòng, phòng tập, nhà, màn đấu. | Bố cục xếp chồng: nhân vật ở trên, bảng ở dưới rộng hết màn hình. Không có chữ bị cắt, nút nào cũng bấm được, không cuộn ngang. Ở nhà thấy đủ 3 món ăn và nút "Đi ngủ"; trên điện thoại màn nhà ẩn số calo lớn; khi có thẻ bữa tối thì ẩn dòng nhắc "Tối rồi…" và nhân vật cao khoảng 240px (ngang phòng tập). Tiếng Việt hiện số lẻ bằng dấu phẩy (`84,8 kg`, hệ số `x1,25`); tiếng Anh dùng dấu chấm. Màn đấu trên điện thoại ẩn số calo và các ô chỉ số, thấy đủ cả hai nhân vật. Bảng thông số ở văn phòng mỗi ô một dòng. UI sáng ấm, riêng đấu trường giữ nền tối. | |
| N6 | Nhìn mọi chỗ có icon: calo, thể lực, mệt mỏi, cân nặng, ngày, sao, cúp, các tab, nhiệm vụ, giá mua. | Đều là icon ảnh cùng phong cách, không có ô vuông trống hay ảnh vỡ. | |
| N7 | Khi số calo lớn (nghìn, triệu, tỷ). | Tiếng Việt: "1,5 N", "4,2 Tr", "1,2 T". Tiếng Anh: "1.5K", "4.2M", "1.2B". Số không tràn khỏi nút hay thẻ. | |
| N8 | Ván mới (cửa sổ ẩn danh), bấm nhân vật 5 cú, rồi bấm tới hết thể lực. | Bàn tay 👆 biến mất sau cú bấm thứ 5. Lúc hết thể lực, khung "Hướng dẫn" hiện cùng lúc 3 mục: "Hết thể lực", "Bấm hay để calo tự chạy?", "Một ngày của bạn". Bấm "Đã hiểu" thì đóng, không hiện lại. | |
| N9 | Tiếp N8: về nhà; mở tab Thi đấu; mở tab Lên đời; ngủ sang ngày 2 rồi vào phòng tập. | Mỗi lần hiện đúng một mục tương ứng, chỉ lần đầu. Về nhà ở hạng 1 chỉ hiện "Buổi tối ở nhà", không hiện mục bữa tối. Vào phòng tập ngày 2 không hiện gì (đã xem). | |
| N10 | Lần đầu về nhà sau khi đạt hạng 3 (chưa từng xem). | Một khung hiện cùng lúc ba mục: bữa tối, mệt mỏi, cân nặng. Mục cân nặng ghi đúng ngưỡng 84,5 / 82 / 78 kg. | |
| N11 | Bấm nút ❓ ở hạng 1, rồi ở hạng 3, cả hai ngôn ngữ. | Hiện đủ 9 mục. Ở hạng 1: bữa tối ghi "🔒 Mở khi đạt hạng 2", mệt mỏi và cân nặng ghi "hạng 3". Khung không cao quá màn hình (thử cả 1440×900, 1366×650, 375×812), nội dung cuộn bên trong, nút "Đã hiểu" luôn thấy. Máy tính 2 cột, điện thoại 1 cột. Đóng được bằng "Đã hiểu", nút ✕, bấm ra ngoài khung, phím Esc; bấm vào trong khung thì không đóng. Bấm ❓ không làm đổi bản lưu. | |
| N12 | Điện thoại 375×812, xem hàng nút trên cùng. | Thấy đủ các nút tròn (🎁 từ ngày 2, ❓, nhân vật, ⚙️), không cuộn ngang. Khung cài đặt vừa màn hình, không cuộn ngang. Tên hạng dài xuống dòng, không bị cắt. | |
| N14 | Điện thoại 375×812, phòng tập xem tab Bài tập, Thi đấu, Nhiệm vụ, Thành tựu, Lên đời; về nhà mở tab Bạn tập. | Thẻ gọn (ô ảnh 40–44 px, chữ nhỏ hơn bản máy tính), thấy ít nhất 2 thẻ đầy đủ; danh sách cuộn được, chữ vẫn đọc được, nút mua vẫn dễ bấm. Dòng mục tiêu (🎯 kg) nằm cùng dòng với chỉ số khi đủ chỗ. Máy tính không đổi. | |
| N13 | Ván mới (cửa sổ ẩn danh), kể cả trên máy cài tiếng Việt. | Game hiện **tiếng Anh**, trong ⚙️ nút "English" sáng. Chọn "Tiếng Việt" rồi tải lại: vẫn tiếng Việt. Bản lưu có từ trước vẫn giữ ngôn ngữ đang dùng. | |
| N15 | 1024×768 và điện thoại 375×812, mở tab Bài tập; đổi qua lại tiếng Việt/Anh và bấm x10, rồi x1. | Tiêu đề sổ tập hiện đúng bản dịch ("Sổ tập" / "Training log"), bài kế tiếp được nhấn rõ, các chế độ mua vẫn chọn được và x1 được khôi phục. Không tràn ngang; trên điện thoại danh sách cuộn riêng trong bảng. | |
| N16 | 1024×768 và điện thoại 375×812; xem tab Thi đấu, Nhiệm vụ, Thành tựu, Lên đời ở phòng tập và tab Bạn tập ở nhà bằng cả hai ngôn ngữ. | Mỗi bảng có tiêu đề chương đúng ngôn ngữ, mặt giấy và hàng phân cách nhất quán với Sổ tập; nút đánh, gọi bạn tập, nhận nhiệm vụ, mua kỹ năng và thử thách vẫn giữ trạng thái đúng. Danh sách cuộn bên trong, không tràn ngang. | |
| N17 | 1024×768 và điện thoại 375×812, xem màn văn phòng và nhà; chọn một bữa ăn rồi kiểm tra nút chuyển màn. | Lịch tuần, thống kê và thẻ bữa tối dùng bề mặt sáng dễ đọc trên nền cảnh; bữa chọn được phân biệt rõ. Nút đi tập/nghỉ/ngủ còn thấy và dùng được, không có tràn ngang hay chữ cắt. | |
| N18 | Mở ⚙️, ❓ và hộp Lên đời; dùng Tab để đi qua nút, thử Enter và Esc trong hộp; sau đó vào trận đấu tới thoại và kết quả. | Cài đặt, hướng dẫn và xác nhận dùng cùng tông giấy, nút đóng/huỷ rõ. Hộp Lên đời: focus sẵn ở nút chính, Tab chỉ đi giữa hai nút của hộp, Enter bấm nút đang chọn, Esc đóng không làm gì; đóng xong focus về nút đã mở hộp. Focus bàn phím dễ thấy trên nền sáng. Trận đấu vẫn giữ nền tối; kết quả thắng/thua hiện bằng băng rôn đọc rõ trên nền đấu trường. Thử cả 375×812. | |
| N19 | 1024×768 và 375×812; kiểm tra hover, nhấn, focus và nút bị khóa ở màn văn phòng/phòng tập. Chọn x10 rồi khôi phục x1, không mua bài hay nhận thưởng. | Tab đang chọn vẫn nổi bật khi rê chuột; hover không dính trên thiết bị cảm ứng. Focus bàn phím có viền rõ (tối trên bảng giấy, sáng trên nền tối). Nút chính lún nhẹ khi nhấn; nút bị khóa không sáng như nút dùng được. Tab/nút hành động cao ít nhất 44 px, chip chọn ít nhất 36 px; không tràn ngang. | |
| N20 | Gây 5 thông báo nhỏ liền nhau (mua bài, khách ghé, nhiệm vụ…) trong lúc đang bấm nhân vật. | Dải nhỏ hiện ngay dưới HUD, không che nhân vật và không chặn bấm; tối đa 3 dải xếp chồng, tin cũ bị đẩy đi; mỗi dải tự tắt sau 2,5 giây và được công bố như trạng thái. | |
| N21 | 1024×768, 768×1024 và 375×812; lần lượt dùng Việt/Anh, kiểm tra HUD với các tên hạng dài và mục tiêu cân nặng; mở hướng dẫn đủ mục. | Tên hạng không bị cắt (điện thoại tối đa 2 dòng), mục tiêu chiếm 1 dòng có ellipsis khi thiếu chỗ; ba nút tròn đều 44 px, không tràn ngang. Hướng dẫn nhiều mục cuộn bên trong, nút Đã hiểu luôn thấy. | ✓ cục bộ |
| N22 | Bật giả lập `prefers-reduced-motion`; xem REP, toast, khách ghé, chữ thoại và hiệu ứng VS ở cả máy tính lẫn điện thoại. | Tắt chuyển động trang trí; vòng REP vẫn đổi trắng/vàng và được chấm đúng thời điểm; toast, pop và khách vẫn tự hết hạn; thoại hiện đủ ngay. Nhịp đếm ngược/trận đấu và kết quả không đổi. | ✓ cục bộ |
| N23 | 1024×768, 768×1024 và 375×812; xem văn phòng, phòng tập, nhà, các tab, cài đặt/hướng dẫn và đấu trường. | Các màn thường dùng nền giấy ấm, xanh sage/olive và điểm nhấn hổ phách; không còn các mảng xanh navy tối hay glow nặng. Đấu trường vẫn tối và giàu tương phản. Chữ và trạng thái nút đọc rõ, không ảnh hưởng luật chơi hay lưu. | ✓ cục bộ |
| N24 | Mở game từ bộ nhớ đệm trống, xem Network. Sau đó đổi nhân vật, lên hạng, mở tab Thi đấu và cuộn danh sách. | Ban đầu chỉ tải ảnh nhân vật đang dùng ở hạng hiện tại và hạng kế. Ảnh đối thủ bắt đầu tải khi mở Thi đấu. Cuộn danh sách vẫn thấy ảnh; khi ảnh bị thiếu vẫn có hình dự phòng. | |
| N25 | Mở văn phòng và phòng tập ở 320×510, 375×610 (khung chơi iPhone X), 430×755, 768×1024 và 812×350. Thử hạng cao có mệt mỏi, thử thách và nút nước tăng lực. | Nhân vật ở giữa và có đủ chỗ. Thông số văn phòng vừa khung, lịch tuần chỉ hiện từ hạng 3. Ở 375×610 thấy ít nhất hai thẻ bài tập đầy đủ. Khi xoay ngang, sổ tập nằm bên cạnh sân khấu. | |
| N27 | Ngủ sang ngày mới ở hạng 3 trở lên, rồi đi tập. | Tờ ghi chú văn phòng có tiêu đề "BÁO CÁO SÁNG", các dòng cân nặng/tuần/cân kiểm tra mỗi dòng một hàng, phía trên câu nói hoặc sự kiện. Rời văn phòng thì báo cáo không còn. Không còn thông báo ngày mới giữa màn. | |
| N28 | Mở ⚙️ ở 375×812 và máy tính. | Tiêu đề "Tạm nghỉ"; nút đỏ "Giữ để xoá toàn bộ tiến trình" ở cuối menu, vừa màn. Trên CrazyGames: mở menu khi đang ở phòng tập gọi `gameplayStop`, đóng gọi lại `gameplayStart`. | |
| N26 | Ở phòng tập 375×610, làm chậm tải ảnh nữ. Đổi nữ, quay lại nam ngay, rồi đổi lại nữ. Làm thiếu ảnh nữ hạng hiện tại và tải lại. | Trong lúc tải giữ ảnh đang hiển thị. Ảnh tải muộn không ghi đè lựa chọn mới. Ảnh nữ hạng thấp hơn hoặc SVG dự phòng ở giữa sau khi tải lại. | |

## O. Vắng mặt

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| O1 | Có calo/giây lớn hơn 0. Ghi lại calo và calo/giây, rồi dán: `s.t = s.act = Date.now() - 2 * 3600e3; save(); location.reload()` | Sau khi tải lại: calo đã cộng sẵn X ≈ calo/giây × 7.200; thẻ "Lúc bạn vắng mặt" · "+X 🔥" (tiếng xu). Không có SDK: chỉ một nút "Nhận". Vẫn cùng ngày trong game. Nếu đang có hướng dẫn thì thẻ chờ hướng dẫn đóng rồi mới hiện. | |
| O2 | `s.t = Date.now() - 20 * 3600e3; save(); location.reload()` | Calo cộng thêm chỉ bằng calo/giây × 28.800 (giới hạn 8 giờ), không phải 20 giờ. | |
| O3 | Ghi lại ngày và cân nặng (mệt mỏi dưới 40), rồi: `s.t = Date.now() - 25 * 3600e3; save(); location.reload()` | Sau khi tải lại: ngày tăng **đúng 1** (dù vắng bao lâu), cân +0,3 kg như một ngày nghỉ, thể lực đầy, ở văn phòng. | |
| O4 | Đóng tab dưới 1 phút rồi mở lại. | Không có thông báo vắng mặt. | |
| O5 | Ở phòng tập, có calo/giây lớn hơn 0. Để tab mở, không chạm 5 phút (hoặc giả lập: `s.act = Date.now() - 301e3`). Ghi lại calo, chờ 3 giây. Sau đó chạm màn hình, chờ 3 giây. | Khi chưa chạm: calo đứng yên, dòng nhắc "💤 Treo máy quá 5 phút…". Sau khi chạm: dòng nhắc mất, calo/giây chạy lại. | |
| O6 | Chuyển sang tab khác 10 phút rồi quay lại. | Calo/giây vẫn cộng đủ 10 phút (rời tab tính như vắng mặt, không bị dừng ở 5 phút); không có dòng nhắc treo máy. | |

## Q. Quà mỗi ngày

Đặt ngày thật đã nhận bằng `s.gd = 'YYYY-MM-DD'` (ví dụ hôm qua) rồi tải lại; xem `s.gn` để biết ô kế tiếp.

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| Q1 | Ván mới, chơi qua dẫn chuyện và ngủ sang ngày 2. Bấm 🎁. Tải lại cùng ngày, bấm 🎁 lần nữa. | Ngày 1 trong game: không có nút 🎁. Sáng ngày 2: nút 🎁 hiện cạnh ❓ với chấm đỏ, Bắp giới thiệu một lần; không có thẻ tự bật. Bấm: thẻ "🎁 Quà ngày 1/7" (dải 7 ô, ô đầu 🎁, ô cuối ⭐), calo Q × 0,25 đã cộng, dòng "Mai quay lại nhận quà ngày 2!"; chấm đỏ tắt. Bấm lại (kể cả sau khi tải lại): thẻ "🎁 Quà mỗi ngày" một nút, chỉ xem vòng quà và quà ngày mai, không cộng gì. | |
| Q2 | Đặt `s.gd` thành hôm qua, bấm 🎁; lặp tới hết ngày 7 rồi thêm một lần. | Lần lượt Q × 0,25 / 0,5 / +50% thể lực / Q × 0,75 / calo +25% hôm nay / Q × 1 / 1 Sao + Q × 1; sau ngày 7 quay về ngày 1. Dải ô ✅ đúng số đã nhận. | |
| Q3 | Đặt `s.gd` thành 3 ngày trước, bấm 🎁. | Nhận đúng ô kế tiếp, không mất chuỗi. | |
| Q4 | Đặt `s.gd` thành ngày mai (đồng hồ bị lùi). | Không có chấm đỏ; bấm 🎁 chỉ xem vòng quà, `gd`/`gn` không đổi. | |
| Q5 | Để game mở qua nửa đêm (hoặc đặt `s.gd` thành hôm qua mà không tải lại). | Chấm đỏ trên 🎁 hiện trong vòng 0,1 giây, không cần tải lại. | |
| Q6 | Vắng hơn 1 phút và `s.gd` hôm qua, tải lại. | Chỉ thẻ vắng mặt tự hiện; quà chờ ở nút 🎁 có chấm đỏ. | |
| Q7 | Nhận quà ngày 5, rồi chọn sự kiện văn phòng có thưởng calo trong ngày. | Hai thưởng nhân dồn (ví dụ 1,25 × 1,3), không ghi đè nhau; sang ngày sau hết cả hai. | |
| Q8 | Xoá tiến trình (giữ nút trong ⚙️) sau khi đã nhận quà hôm nay. | Vòng quà giữ nguyên, không nhận thêm quà hôm nay khi tới ngày 2 của ván mới. | |

## P. Quảng cáo và CrazyGames

Bản chạy trên máy dùng quảng cáo giả của SDK. Phần này cần thử lại bằng công cụ QA của CrazyGames trước khi đăng.

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| P1 | Ở phòng tập, bấm "🥤 Nước tăng lực +50%". | Quảng cáo chạy; xem hết thì thể lực cộng thêm 50% thể lực tối đa (hạng 1: +150, có thể vượt mức tối đa). Nút biến mất cho tới ngày hôm sau. | |
| P2 | Bỏ ngang hoặc quảng cáo lỗi. | Không được cộng thể lực, nút vẫn còn. | |
| P3 | Ngủ để sang ngày 3, 6, 9… | Có quảng cáo giữa game ngay sau khi sang ngày (ngày chia hết cho 3). Các ngày khác không có. Lên đời cũng có một quảng cáo. | |
| P4 | Trong lúc quảng cáo chạy. | Nhạc và mọi tiếng trong game tắt; hết quảng cáo thì nhạc phát lại. | |
| P5 | Trên CrazyGames: bật tắt tiếng bằng nút của cổng game. | Game tắt hết tiếng khi cổng yêu cầu, bất kể âm lượng chỉnh trong game. | |
| P6 | Trên CrazyGames: chơi, đăng xuất/đổi máy cùng tài khoản. | Tiến trình được giữ (lưu qua Data Module). | |
| P8 | Trên CrazyGames: vắng mặt hơn 1 phút có calo/giây, mở lại, bấm "📺 Nhân đôi" trên thẻ vắng mặt. Lần khác bấm "Nhận" hoặc Esc. | Xem hết quảng cáo: cộng thêm đúng số calo trên thẻ (dải nhỏ báo lại). Bỏ ngang hoặc lỗi: chỉ giữ phần đã cộng. "Nhận" và Esc không mở quảng cáo. | |
| P9 | Trên CrazyGames: nhận quà mỗi ngày ở ngày có calo, bấm "📺 Nhân đôi"; lần khác bỏ ngang; ngày 3, 5. | Xem hết: cộng thêm đúng phần calo (dải nhỏ báo lại). Bỏ ngang: giữ phần đã cộng. Ngày 3 và 5 chỉ có nút "Nhận". |
| P7 | Chặn mạng tới `sdk.crazygames.com` rồi mở game. | Game vẫn vào được sau tối đa khoảng 4 giây, chơi bình thường, không có nút nước tăng lực và không có quảng cáo. | |

---

## Kiểm tra nhịp chơi (chơi thật, không dùng lệnh)

Chơi một ván mới ở chế độ thường, bấm đồng hồ, không dùng Console.

Với người mới chơi trên điện thoại thật, bắt đầu bấm giờ khi thấy lời dẫn đầu tiên. Ghi thiết bị, trình duyệt, ngôn ngữ, thời điểm chạm tập lần đầu, mua Tay lần đầu và sang ngày 2. Trong 15 phút đầu, ghi chỗ người chơi dừng để hỏi hoặc bỏ qua, và xem họ có nhận ra vòng Rep hoàn hảo khi nó xuất hiện không.

| Mã | Mốc | Mong muốn | Thực tế |
|---|---|---|---|
| R1 | Lên hạng 2 | Trong ngày 1, khoảng 2 phút | |
| R2 | Lên hạng 3 | Ngày 2, khoảng 5 phút | |
| R3 | Lên hạng 4 | Ngày 4–5, khoảng 12–14 phút | |
| R4 | Lên hạng 5 | Ngày 10–12, khoảng 30–35 phút | |
| R5 | Độ dài một ngày | 2–3 phút ở mọi hạng | |
| R6 | Cảm nhận | Không có quãng nào dài hơn 5 phút mà không có gì mới (hạng, bài tập, đối thủ, bạn tập) trong 15 phút đầu | |
