# Bộ test thủ công cho Gym God

Mỗi dòng là một bài test: làm theo cột **Bước**, so với cột **Kết quả mong muốn**. Đánh dấu Đạt/Lỗi vào cột cuối. Khi lỗi, ghi lại mã bài test, điều thấy được và ảnh chụp màn hình.

Con số trong file này lấy từ `docs/GAME_DESIGN.md`. Nếu đổi luật hay con số thì sửa cả hai.

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
| Chơi mới từ đầu (tiếng Việt) | `s = fresh(); s.lang = 'vi'; shown = -1; syncRank(true); buildTexts(); go('office'); save()` |
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
| A1 | Chạy lệnh "Chơi mới từ đầu". | Vào thẳng **phòng tập**, không có khung nào che. Calo 0, Thể lực 300 / 300, Cân nặng 85.0 kg. Không thấy ô Mệt mỏi. Thanh hạng: "1 · Dân văn phòng suy nhược", "0/3 nhóm cơ". Bàn tay 👆 nhún nhảy trên nhân vật, dòng nhắc "Bấm vào nhân vật để tập!". Bảng bài tập bên phải. | |
| A2 | Tải lại trang (F5) 5 lần. | Câu nói ở văn phòng thay đổi giữa các lần (có 8 câu, có thể trùng). Các thông số không đổi. | |
| A3 | Vào phòng tập, bấm 20 cú, mua 1 cấp Tay. Đợi 6 giây rồi tải lại trang. | Mở lại ở **văn phòng** (không phải phòng tập). Calo, cấp Tay và thể lực còn lại giữ nguyên như trước khi tải lại. | |
| A4 | Về nhà (chưa ngủ), đợi 6 giây, tải lại trang. | Mở lại ở **nhà**, vẫn cùng ngày, nút "Đi ngủ" còn đó. | |
| A5 | Tải lại trang rồi bấm thật nhanh vào bất kỳ nút nào trong 1–2 giây đầu. | Không mất tiến trình: sau khi game tải xong, số liệu vẫn như trước khi tải lại. (Nếu kịp bấm "Đến phòng tập" thì vẫn được sang phòng tập, đó là bình thường.) | |
| A6 | Mở Console, xem có dòng đỏ nào không trong suốt buổi test. | Không có lỗi đỏ (Uncaught…), không có 404. | |
| A7 | Ngủ sang ngày mới. Làm hỏng bản chính: `store().setItem(KEY, '{hong')`, rồi tải lại trang. | Game tải bản dự phòng: đúng ngày vừa sang, đúng hạng, trận thắng, calo của sáng hôm đó. Không bị về ván mới. | |
| A8 | Xoá bản chính: `store().removeItem(KEY)`, tải lại trang. | Như A7: tải bản dự phòng, không về ván mới. Sau 5 giây bản chính được ghi lại. | |
| A9 | Bấm "Xoá toàn bộ tiến trình" → Đồng ý, rồi chạy `JSON.parse(store().getItem(OLD)).day` | Game về ván mới, nhưng lệnh trả về ngày của ván cũ: trạng thái trước khi xoá vẫn còn để cứu nếu bấm nhầm. | |
| A10 | Trên CrazyGames, chơi khi chưa đăng nhập, rồi đăng nhập giữa chừng. | Trang tự tải lại. Nếu tài khoản chưa từng chơi game: tiến trình khách được chuyển sang tài khoản. Nếu tài khoản đã có tiến trình: hiện tiến trình của tài khoản, không bị bản khách ghi đè. | |
| A11 | Trên CrazyGames, đăng nhập, chơi một ngày, rồi mở game trên máy hoặc trình duyệt khác cùng tài khoản. | Cùng tiến trình ở cả hai nơi (có thể trễ tới 30 giây sau lần lưu cuối). | |

## B. Vòng ngày và chuyển cảnh

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| B1 | Ở văn phòng, bấm "Đến phòng tập". | Màn chờ tối phủ cả khung, có hình nhân vật xách túi và chữ "Đi đến phòng tập..." với dấu chấm chạy, kéo dài 2 giây. Trong lúc đó không bấm được gì. Sau đó vào phòng tập: nền phòng gym, có số calo lớn, các ô thể lực/cân nặng, bảng bài tập bên phải. | |
| B2 | Ở phòng tập, bấm "Về nhà" rồi bấm "Huỷ". | Hộp hỏi "Tập đủ rồi, về nhà thôi?" với nút Huỷ và Đồng ý. Bấm Huỷ: hộp đóng, vẫn ở phòng tập. | |
| B3 | Bấm "Về nhà" rồi "Đồng ý". | Màn chờ "Đi về nhà..." 2 giây, rồi vào nhà: nền căn hộ buổi tối, nút "Đi ngủ", bảng bên phải chỉ có tab Bạn tập. | |
| B4 | Ở nhà, bấm "Đi ngủ". | Bốn màn chờ nối tiếp, mỗi màn một hình: "Khò khò..." 2 giây → "Buổi sáng..." 1,5 giây → "Đi đến công ty..." 2 giây → "Đang làm việc..." 3 giây. Sau đó về văn phòng, số ngày tăng 1, thứ đổi theo. Thông báo "Ngày N" kèm dòng cân nặng. Thể lực đầy lại. | |
| B5 | Ở văn phòng, bấm "Về nhà nghỉ" rồi "Huỷ". | Hộp hỏi "Về nhà nghỉ luôn? Hôm nay sẽ không tập." Bấm Huỷ: vẫn ở văn phòng. | |
| B6 | Bấm "Về nhà nghỉ" rồi "Đồng ý" (mệt mỏi dưới 40 hoặc chưa mở mệt mỏi). | Màn chờ "Đi về nhà..." 2 giây, vào nhà, thông báo "Tiếc quá, lại một ngày không luyện tập!". | |
| B7 | Ở nhà nhìn bảng bên phải; ở phòng tập nhìn bảng bên phải. | Ở nhà chỉ có tab Bạn tập. Ở phòng tập có Bài tập, Thi đấu, Nhiệm vụ, Thành tựu, Lên đời và **không có** tab Bạn tập. | |
| B8 | Ở văn phòng, bấm vào nhân vật nhiều lần. | Không có gì xảy ra: calo không tăng, thể lực không giảm. | |
| B9 | Ở phòng tập, bấm tới hết thể lực rồi bấm "Về nhà". | **Không** có hộp hỏi, vào thẳng màn chờ về nhà. | |
| B10 | `s.day = 5; go('office')`, bấm "Đến phòng tập"; sau đó về nhà và bấm "Đi ngủ". | Màn chờ đi tập khoảng 0,8 giây; chuỗi đi ngủ khoảng 3,4 giây, đủ 4 hình. Ngày 1–3 vẫn là 2 giây và 8,5 giây như B1, B4. | |
| B11 | Bấm "Đi ngủ", chạm vào màn chờ sau khoảng 1 giây. Lần sau chạm ngay khi màn chờ vừa hiện. | Màn chờ có dòng "Chạm để bỏ qua". Chạm sau 1 giây: bỏ qua phần còn lại, sang ngày mới ngay (ngày +1, thông báo ngày mới). Chạm ngay lập tức (dưới 0,4 giây): không có tác dụng. | |
| B12 | Ở phòng tập, nhìn bảng Bài tập; bấm vào thanh hạng trên cùng. | Đúng một thẻ có viền vàng phát sáng: bài rẻ nhất còn thiếu mục tiêu hạng kế (ván mới: Tay; Tay đủ 5 thì sang Vai). Bấm thanh hạng: mở tab Bài tập, cuộn tới thẻ đó, thẻ nảy nhẹ. Ở văn phòng bấm thanh hạng không làm gì. Hạng cao nhất hoặc chỉ còn thiếu cân nặng: không thẻ nào viền vàng. | |

## C. Bấm, thể lực, chống auto-click

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| C1 | Chơi mới, vào phòng tập, bấm nhân vật 10 cú. | Mỗi cú: số "+1" bay lên, có tiếng bấm, calo +1, thể lực −1. Sau 10 cú: calo 10, thể lực 290 / 300. | |
| C2 | Chưa mua gì, bấm tới khi có 15 calo. | Dòng nhắc dưới nhân vật đổi từ "Bấm vào nhân vật để tập!" thành "Đủ calo rồi, mua bài tập đầu tiên!", nút mua Tay nhấp nháy. | |
| C3 | Bấm cho tới khi thể lực về 0 (chế độ test không giảm số cú cần bấm). | Thể lực 0 / 300. Dòng nhắc "Hết thể lực! Về nhà nghỉ thôi." thành nhãn đỏ viền trắng, to hơn, phồng lên và nhấp nháy liên tục. Nút "Về nhà" nhấp nháy. Bấm nhân vật tiếp: calo không tăng, nút "Về nhà" nảy lên. | |
| C4 | Khi còn thể lực, dán vào Console: `for (let i = 0; i < 200; i++) $('hero').click()` | Calo và thể lực **không đổi** (cú bấm giả bị bỏ qua). | |
| C5 | Dùng phần mềm auto-click hoặc bấm thật nhanh trong 5 giây, đếm thể lực đã mất. | Mất không quá khoảng 100 thể lực trong 5 giây (tối đa 20 cú mỗi giây được tính). | |
| C6 | Đứng yên ở phòng tập khi đã có calo/giây (đã mua Vai). | Calo tự tăng theo calo/giây, thể lực không giảm. Về văn phòng hoặc ở nhà calo vẫn tăng. | |

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
| E2 | Mua Ngực lên 2. | Màn hình loé sáng và rung, tiếng lên hạng, nhân vật đổi hình. Thông báo "LỘT XÁC!" · "Tập tành cho vui · x1.25 · Mở khoá: bữa tối ở nhà" hiện khoảng 6 giây, **sau đó** mới tới thông báo thành tựu "Đạt hạng 2 · +1%" (không được đè lên nhau). Số hạng thành 2. Calo/giây và calo/bấm tăng khoảng 26% (25% của hạng + 1% của thành tựu). | |
| E3 | Sau E2, sang ngày mới. | Thể lực tối đa là 420 (thể lực tối đa chỉ tăng từ sáng hôm sau, không tăng ngay lúc lên hạng). | |
| E4 | Trước hạng 2 về nhà; sau hạng 2 về nhà. | Trước hạng 2: chữ "Về đến nhà rồi. Ngủ một giấc để mai tập tiếp!", không có món ăn. Từ hạng 2: chữ "Tối rồi. Chọn một bữa ăn (hoặc bỏ bữa) rồi đi ngủ." và 3 thẻ món ăn. | |
| E5 | Đạt hạng 3 (Tay 12, Vai 10, Ngực 5, Bụng 1). | Thông báo lên hạng "Gymer nghiệp dư · x1.5" kèm "Mở khoá: mệt mỏi và lịch tuần… Hạng 4 cần cân nặng ≤ 84,5 kg: tập đủ mỗi ngày giảm 0,3 kg". Xuất hiện ô Mệt mỏi cạnh thể lực; ở văn phòng xuất hiện 7 ô lịch tuần, dòng "Buổi tập tuần này: n / 5" và ô thông số Mệt mỏi. | |
| E6 | Ở hạng 3, đặt đủ cấp hạng 4 nhưng cân 85 kg: `Object.assign(s.lv, {tay: 22, vai: 18, nguc: 14, bung: 8, mat: 3}); s.kg = 85; syncRank(); ui()` | **Không** lên hạng. Thanh hạng ghi "Giảm thêm 0.5 kg để lên hạng". | |
| E7 | Tiếp E6: `s.kg = 84.5; syncRank(); ui()` | Lên hạng 4 "Body săn chắc · x2". | |
| E8 | Ở hạng 4, tăng cân lại: `s.kg = 95; syncRank(); ui()` | Vẫn ở hạng 4, không bị tụt hạng. | |
| E9 | Đạt hạng 6 (dùng bảng cấp ở phần Chuẩn bị, cân ≤ 78). | Hạng 6 "Thần gym công sở · x3". Thanh hạng ghi "Hạng cao nhất", thanh tiến độ đầy. | |
| E10 | Lên từng hạng 1 → 6, đổi nhân vật bằng nút mặt người trên cùng. | Mỗi hạng một hình khác nhau cho cả nhân vật nam và nữ, nhân vật không bị nhảy vị trí hay đổi cỡ giữa các hạng. | |

## F. Cân nặng

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| F1 | Chơi mới, tập hết 300 thể lực, về nhà, ngủ. | Thông báo "Ngày 2" · "Tập hôm nay: −0.3 kg → 84.7 kg". Ô cân nặng ghi 84.7 kg. | |
| F2 | Tập đúng nửa thanh thể lực (150 cú) rồi về nhà ngủ. | Cân giảm 0,15 kg so với hôm trước (hiển thị làm tròn 1 chữ số). | |
| F3 | Không tập, về nhà nghỉ, ngủ (mệt mỏi dưới 40). | Thông báo "Nghỉ hôm nay: +0.3 kg". Cân tăng 0,3 kg. | |
| F4 | `s.kg = 70; go('gym')` rồi so calo/giây với lúc `s.kg = 75; go('gym')`. | Ở 70 kg (vùng 68–72) calo/giây và calo/bấm cao hơn đúng 20% so với ở 75 kg. | |
| F5 | `s.kg = 91; s.used = 0; endDay()` rồi xem thể lực tối đa; so với khi cân 85. | Trên 90 kg, thể lực tối đa chỉ còn 80% (hạng 1: 240 thay vì 300). | |
| F6 | `s.kg = 65; s.used = s.cap; endDay()` và `s.kg = 120; s.used = 0; endDay()`. | Cân không xuống dưới 65.0 kg và không vượt 120.0 kg. | |
| F7 | Ở hạng 3, chưa đủ nhóm cơ cho hạng 4, cân 85. | Thanh hạng ghi "n/5 nhóm cơ · ≤ 84.5 kg (−0.5)". Khi cân ≤ 84,5 thì ghi "≤ 84.5 kg ✓". Ở hạng 1 và 2 thanh hạng không nhắc gì tới cân nặng. | |

## G. Mệt mỏi và ngày nghỉ (từ hạng 3)

Trước các bài này: đạt hạng 3, rồi `s.fat = 0; go('office')`.

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| G1 | Ở hạng 1 hoặc 2, tập hết thể lực nhiều ngày liền. | Không có ô Mệt mỏi, thể lực tối đa không bị giảm. | |
| G2 | Hạng 3, mệt mỏi 0. Tập hết thể lực, ngủ. | Mệt mỏi thành 17 (cộng 22, trừ 5 khi ngủ), trạng thái "Sung sức". Thể lực 540 / 540. | |
| G3 | Tập hết thể lực thêm 2 ngày nữa. | Mệt mỏi 34 rồi 51. Ở 51: trạng thái "Mỏi", thể lực tối đa còn 405 (75% của 540). | |
| G4 | `s.fat = 80; s.used = s.cap * .1; endDay()` (tập rất ít để mệt mỏi vẫn trên 70). | Ô mệt mỏi ghi "Kiệt sức". Thể lực tối đa sáng nay còn 50% (hạng 3: 270). | |
| G5 | `s.fat = 100; go('office')` | Câu nói đổi thành "Cơ thể quá tải rồi. Hôm nay bắt buộc phải nghỉ!". Nút "Đến phòng tập" mờ, không bấm được. Chỉ còn "Về nhà nghỉ". | |
| G6 | `s.fat = 50; go('office')`, bấm "Về nhà nghỉ" → Đồng ý, rồi ngủ. | Thông báo khi về nhà: "Nghỉ hôm nay để mai khoẻ hơn." Sáng hôm sau: mệt mỏi 0, cân chỉ +0,1 kg, dòng dưới lịch tuần có "Hồi phục: bấm +25%", calo mỗi lần bấm cao hơn 25% so với bình thường. | |
| G7 | Sau G6, tập rồi ngủ thêm một ngày. | "Hồi phục" biến mất, calo mỗi lần bấm về bình thường. | |
| G8 | `s.fat = 30; go('office')`, nghỉ, ngủ. | Thông báo "Tiếc quá, lại một ngày không luyện tập!". Sáng hôm sau: mệt mỏi 0, cân +0,3 kg, **không** có "Hồi phục". | |
| G9 | So mức cộng mệt mỏi khi tập hết thanh ở hạng 3, 4, 5, 6 (đặt `s.fat = 0` trước mỗi lần). | Sau một ngày tập đủ: hạng 3 → 17, hạng 4 → 13, hạng 5 → 9, hạng 6 → 5. Hạng càng cao càng lâu mệt. | |

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
| J1 | Chơi mới, vào tab Thi đấu. | 20 đối thủ có ảnh và tên. Chỉ đối thủ đầu (Anh Tom kế toán) có nút "Thách đấu" bấm được; thẻ ghi "Cần 300 / 15s" và "+3% vĩnh viễn · +900". | |
| J2 | Khi thể lực dưới 40 (không phải Chủ nhật). | Nút "Thách đấu" mờ, không bấm được. | |
| J3 | Thể lực từ 40 trở lên, bấm "Thách đấu". | Thể lực −40 ngay. Vào màn đấu: nhân vật bên trái, đối thủ bên phải, chữ "VS", đồng hồ đếm 15 giây, thanh xanh của bạn và thanh đỏ của đối thủ. Thanh đỏ đầy dần đều và đầy đúng lúc hết giờ. Nhạc đổi sang bài thi đấu. Nút "Về nhà" ẩn. | |
| J4 | Trong lúc đấu, bấm nhân vật liên tục. | Thanh xanh tăng theo mỗi cú bấm; thể lực **không giảm**. Thỉnh thoảng đối thủ lao tới "ra đòn", nhân vật chớp sáng (chỉ là hình ảnh, không mất điểm). | |
| J5 | Làm đầy thanh xanh trước khi hết giờ. | Thông báo "THẮNG!" · "+3% · +900". Calo +900, "Đối thủ đã thắng" tăng 1, calo/giây và calo/bấm tăng 3% (trận đầu tiên tăng 4% vì kèm thành tựu "Thắng 1 đối thủ"). Đối thủ vừa thắng không đấu lại được; đối thủ kế tiếp mở ra (cần 720). Nhạc về bài phòng tập. | |
| J6 | Chế độ thường, vào đấu rồi không bấm gì (khi calo/giây còn thấp). | Hết 15 giây: "Thua rồi!" · "Tập thêm rồi quay lại", có tiếng thua. Không mất gì ngoài 40 thể lực. Đấu lại được nếu còn thể lực. | |
| J7 | Đang đấu thì hết giờ hoặc thắng, kiểm tra tab Thi đấu. | Khi một trận đang diễn ra, mọi nút "Thách đấu" đều mờ. | |
| J8 | Thắng đủ 20 đối thủ (chế độ test). | "Đối thủ đã thắng 20 / 20". Không còn nút đấu nào bấm được. Nhiệm vụ "Thách đấu 1 lần" tự tính là xong. | |
| J9 | Khi ước chừng đủ sức thắng đối thủ kế tiếp. | Tab Thi đấu có chấm đỏ. | |

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
| L1 | Vào tab Nhiệm vụ. | 3 nhiệm vụ trong 5 loại: Bấm 200 lần, Mua 20 cấp bài tập, Thách đấu 1 lần, Gọi bạn tập 1 lần, Chơi 2 phút. Mỗi cái có icon, thanh tiến độ và nút thưởng (ít nhất 500 calo). | |
| L2 | Làm xong một nhiệm vụ. | Nút thưởng sáng lên, tab Nhiệm vụ có chấm đỏ. Bấm nhận: calo tăng đúng số ghi trên nút, thông báo "Xong nhiệm vụ!", nút thành ✓, thẻ mờ đi. Bấm lại không nhận lần hai. | |
| L3 | Sang ngày mới. | 3 nhiệm vụ đổi (xoay vòng theo ngày), tiến độ về 0. | |
| L4 | Vào tab Thành tựu. | 19 thành tựu; cái chưa đạt mờ. Đạt một cái (ví dụ bấm 100 lần): thẻ sáng lên, "Thành tựu n / 19" tăng, calo tăng 1%. Phần Thống kê phía dưới hiện đủ 8 dòng và cập nhật theo thời gian. | |
| L5 | Tab Lên đời khi tổng calo kiếm trong đời này dưới 1 triệu. | "Sao nhận nếu lên đời: 0". Nút ghi "Chưa đủ calo để nhận Sao", mờ. | |
| L6 | Kiếm 8 triệu calo trong đời này (chế độ test, hoặc `s.run = 8e6; ui()`). Bấm "Lên đời" → Đồng ý. | Trước khi bấm: "Sao nhận nếu lên đời: 2", tab có chấm đỏ. Hộp hỏi "Lên đời? Calo và cấp bài tập về 0, bạn nhận 2 Sao." Sau khi đồng ý: calo 0, mọi bài tập cấp 0, về hạng 1, Sao +2, "Thưởng hiện tại +20%". **Giữ nguyên**: ngày, cân nặng, mệt mỏi, bạn tập, số trận thắng, thành tựu. | |
| L7 | Sau L6 (đã từng đạt hạng 3 trước khi lên đời), về nhà và về văn phòng. | Bữa tối, ô mệt mỏi và lịch tuần **vẫn còn** dù đang ở hạng 1. | |
| L8 | Sau L6, so calo mỗi lần bấm với một ván mới chưa có Sao. | Cao hơn đúng 20% (2 Sao). | |
| L9 | Cuối tab Lên đời, bấm "Xoá toàn bộ tiến trình" → Huỷ; rồi bấm lại → Đồng ý. | Huỷ: không đổi gì. Đồng ý: mọi thứ về như chơi mới (calo, cấp, Sao, bạn tập, trận thắng, ngày 1, 85 kg), nhưng **giữ** ngôn ngữ, trạng thái loa và nhân vật đang chọn. | |

## M. Âm thanh và nhạc

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| M1 | Mở game, chưa bấm gì. | Im lặng (trình duyệt chưa cho phát tiếng). | |
| M2 | Bấm bất kỳ đâu trong game. | Nhạc văn phòng (chậm, nhẹ) bắt đầu, lên dần trong khoảng nửa giây. | |
| M3 | Đi văn phòng → phòng tập → nhà. | Mỗi màn một bài: phòng tập sôi động, nhà ấm nhẹ. Bài cũ mờ dần rồi bài mới lên, không cắt đột ngột, không có hai bài chồng nhau lâu hơn 1 giây. | |
| M4 | Ở mỗi màn, nghe đủ lâu để bài lặp lại ít nhất 2 lần. | Chỗ nối khi lặp không có khoảng lặng hay tiếng "khựng" rõ rệt. | |
| M5 | Bấm "Đi ngủ". | Đoạn nhạc ru ngủ rồi sáng dần phát một lần trong chuỗi màn chờ, không lặp. Về văn phòng thì nhạc văn phòng trở lại. | |
| M6 | So độ to giữa 5 bài, và giữa nhạc với tiếng bấm/tiếng mua. | Các bài to gần bằng nhau. Tiếng bấm, tiếng mua, tiếng lên hạng vẫn nghe rõ trên nền nhạc. | |
| M7 | Bấm nút loa 3 lần. | Lần 1: icon 🔉, thông báo "Tắt nhạc", nhạc dừng nhưng tiếng bấm vẫn còn. Lần 2: 🔇, "Tắt hết âm thanh", không còn tiếng gì. Lần 3: 🔊, "Bật nhạc và âm thanh", nhạc phát lại. | |
| M8 | Đặt loa ở 🔉, tải lại trang. | Vẫn ở 🔉, không có nhạc, còn tiếng bấm. | |
| M9 | Đang có nhạc, chuyển sang tab trình duyệt khác rồi quay lại. | Nhạc dừng khi rời tab và phát lại khi quay về. | |
| M10 | Trên điện thoại thật (đặc biệt iPhone/Safari): mở game, chạm một lần. | Nhạc phát được sau cú chạm đầu tiên. Bật chế độ im lặng của máy thì không có tiếng. | |

## N. Giao diện, ngôn ngữ, bố cục

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| N1 | Bấm nút "EN" trên cùng. | Toàn bộ chữ đổi sang tiếng Anh: tên hạng, tab, bài tập, đối thủ (Tom from Accounting…), món ăn, nhiệm vụ, thành tựu, câu nói, màn chờ. Không còn chữ tiếng Việt sót lại. Nút đổi thành "VI". Số liệu không đổi. | |
| N2 | Đổi lại "VI", tải lại trang. | Ngôn ngữ được nhớ sau khi tải lại. | |
| N3 | Bấm nút nhân vật (mặt người). | Đổi giữa nhân vật nam và nữ ở đúng hạng hiện tại; lựa chọn được nhớ sau khi tải lại. | |
| N4 | Cửa sổ máy tính rộng hơn 900px. | Nhân vật bên trái, bảng bên phải rộng khoảng 430px. Màu chủ đạo xanh dương, nút mua vàng cam, nút hành động xanh lá. Không có thanh cuộn ngang. | |
| N5 | Tablet dọc 768×1024 và điện thoại 375×812, lần lượt ở văn phòng, phòng tập, nhà, màn đấu. | Bố cục xếp chồng: nhân vật ở trên, bảng ở dưới rộng hết màn hình. Không có chữ bị cắt, nút nào cũng bấm được, không cuộn ngang. Ở nhà thấy đủ 3 món ăn và nút "Đi ngủ"; trên điện thoại màn nhà ẩn số calo lớn và nhân vật nhỏ (khoảng 80px). Màn đấu trên điện thoại ẩn số calo và các ô chỉ số, thấy đủ cả hai nhân vật. Bảng thông số ở văn phòng mỗi ô một dòng. | |
| N6 | Nhìn mọi chỗ có icon: calo, thể lực, mệt mỏi, cân nặng, ngày, sao, cúp, các tab, nhiệm vụ, giá mua. | Đều là icon ảnh cùng phong cách, không có ô vuông trống hay ảnh vỡ. | |
| N7 | Khi số calo lớn (nghìn, triệu, tỷ). | Tiếng Việt: "1,5 N", "4,2 Tr", "1,2 T". Tiếng Anh: "1.5K", "4.2M", "1.2B". Số không tràn khỏi nút hay thẻ. | |
| N8 | Ván mới (cửa sổ ẩn danh), bấm nhân vật 5 cú, rồi bấm tới hết thể lực. | Bàn tay 👆 biến mất sau cú bấm thứ 5. Lúc hết thể lực, khung "Hướng dẫn" hiện cùng lúc 3 mục: "Hết thể lực", "Bấm hay để calo tự chạy?", "Một ngày của bạn". Bấm "Đã hiểu" thì đóng, không hiện lại. | |
| N9 | Tiếp N8: về nhà; mở tab Thi đấu; mở tab Lên đời; ngủ sang ngày 2 rồi vào phòng tập. | Mỗi lần hiện đúng một mục tương ứng, chỉ lần đầu. Về nhà ở hạng 1 chỉ hiện "Buổi tối ở nhà", không hiện mục bữa tối. Vào phòng tập ngày 2 không hiện gì (đã xem). | |
| N10 | Lần đầu về nhà sau khi đạt hạng 3 (chưa từng xem). | Một khung hiện cùng lúc ba mục: bữa tối, mệt mỏi, cân nặng. Mục cân nặng ghi đúng ngưỡng 84,5 / 82 / 78 kg. | |
| N11 | Bấm nút ❓ ở hạng 1, rồi ở hạng 3, cả hai ngôn ngữ. | Hiện đủ 9 mục. Ở hạng 1: bữa tối ghi "🔒 Mở khi đạt hạng 2", mệt mỏi và cân nặng ghi "hạng 3". Khung không cao quá màn hình (thử cả 1440×900, 1366×650, 375×812), nội dung cuộn bên trong, nút "Đã hiểu" luôn thấy. Máy tính 2 cột, điện thoại 1 cột. Đóng được bằng "Đã hiểu", nút ✕, bấm ra ngoài khung, phím Esc; bấm vào trong khung thì không đóng. Bấm ❓ không làm đổi bản lưu. | |
| N12 | Điện thoại 375×812, xem hàng nút trên cùng. | Thấy đủ 4 nút tròn (❓, nhân vật, âm thanh, ngôn ngữ). Tên hạng dài xuống dòng, không bị cắt. | |
| N13 | Ván mới (cửa sổ ẩn danh), kể cả trên máy cài tiếng Việt. | Game hiện **tiếng Anh**, nút ngôn ngữ ghi "VI". Bấm "VI" rồi tải lại: vẫn tiếng Việt. Bản lưu có từ trước vẫn giữ ngôn ngữ đang dùng. | |
## O. Vắng mặt

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| O1 | Có calo/giây lớn hơn 0. Ghi lại calo và calo/giây, rồi dán: `s.t = Date.now() - 2 * 3600e3; save(); location.reload()` | Sau khi tải lại: thông báo "Lúc bạn vắng mặt" · "+X", với X ≈ calo/giây × 7.200. Vẫn cùng ngày trong game. | |
| O2 | `s.t = Date.now() - 20 * 3600e3; save(); location.reload()` | Calo cộng thêm chỉ bằng calo/giây × 28.800 (giới hạn 8 giờ), không phải 20 giờ. | |
| O3 | Ghi lại ngày và cân nặng (mệt mỏi dưới 40), rồi: `s.t = Date.now() - 25 * 3600e3; save(); location.reload()` | Sau khi tải lại: ngày tăng **đúng 1** (dù vắng bao lâu), cân +0,3 kg như một ngày nghỉ, thể lực đầy, ở văn phòng. | |
| O4 | Đóng tab dưới 1 phút rồi mở lại. | Không có thông báo vắng mặt. | |

## P. Quảng cáo và CrazyGames

Bản chạy trên máy dùng quảng cáo giả của SDK. Phần này cần thử lại bằng công cụ QA của CrazyGames trước khi đăng.

| Mã | Bước | Kết quả mong muốn | Đạt? |
|---|---|---|---|
| P1 | Ở phòng tập, bấm "🥤 Nước tăng lực +50%". | Quảng cáo chạy; xem hết thì thể lực cộng thêm 50% thể lực tối đa (hạng 1: +150, có thể vượt mức tối đa). Nút biến mất cho tới ngày hôm sau. | |
| P2 | Bỏ ngang hoặc quảng cáo lỗi. | Không được cộng thể lực, nút vẫn còn. | |
| P3 | Ngủ để sang ngày 3, 6, 9… | Có quảng cáo giữa game ngay sau khi sang ngày (ngày chia hết cho 3). Các ngày khác không có. Lên đời cũng có một quảng cáo. | |
| P4 | Trong lúc quảng cáo chạy. | Nhạc và mọi tiếng trong game tắt; hết quảng cáo thì nhạc phát lại. | |
| P5 | Trên CrazyGames: bật tắt tiếng bằng nút của cổng game. | Game tắt hết tiếng khi cổng yêu cầu, bất kể nút loa trong game. | |
| P6 | Trên CrazyGames: chơi, đăng xuất/đổi máy cùng tài khoản. | Tiến trình được giữ (lưu qua Data Module). | |
| P7 | Chặn mạng tới `sdk.crazygames.com` rồi mở game. | Game vẫn vào được sau tối đa khoảng 4 giây, chơi bình thường, không có nút nước tăng lực và không có quảng cáo. | |

---

## Kiểm tra nhịp chơi (chơi thật, không dùng lệnh)

Chơi một ván mới ở chế độ thường, bấm đồng hồ, không dùng Console.

| Mã | Mốc | Mong muốn | Thực tế |
|---|---|---|---|
| R1 | Lên hạng 2 | Trong ngày 1, khoảng 2 phút | |
| R2 | Lên hạng 3 | Ngày 2, khoảng 5 phút | |
| R3 | Lên hạng 4 | Ngày 4–5, khoảng 12–14 phút | |
| R4 | Lên hạng 5 | Ngày 10–12, khoảng 30–35 phút | |
| R5 | Độ dài một ngày | 2–3 phút ở mọi hạng | |
| R6 | Cảm nhận | Không có quãng nào dài hơn 5 phút mà không có gì mới (hạng, bài tập, đối thủ, bạn tập) trong 15 phút đầu | |
