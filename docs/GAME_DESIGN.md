# Thiết kế game Gym God

Luật chơi và con số **hiện hành**. Khi file này lệch với `index.html` thì code đúng, và phải sửa lại file này. Đổi con số nào thì đổi luôn `G` trong `tools/sim.py`.

## Ý tưởng

Dân văn phòng suy nhược đi tập sau giờ làm và lột xác qua 6 hạng. Game không chỉ là bấm: mỗi ngày người chơi sắp xếp tập, nghỉ và ăn.

Nguyên tắc thiết kế:

- **Đầu dễ, sau khó.** Người mới chỉ thấy thể lực; tính năng mở dần theo hạng.
- **Không bao giờ phải chờ.** Ngày là ngày trong game: hết thể lực thì về nhà, ngủ, sang ngày mới ngay.
- **Phải tập đủ nhóm cơ.** Lên hạng cần đạt mục tiêu của từng bài tập, không dồn vào một bài được.
- **Lựa chọn nào cũng có giá.** Nghỉ thì hồi sức nhưng tăng cân; ăn vặt thì mạnh nhưng giảm cân chậm.

## Vòng lặp một ngày (2–3 phút)

1. **Văn phòng**: mọi ván mới mở ở đây; Bắp tự giới thiệu và chỉ nút "Đến phòng tập". Màn có câu nói ngẫu nhiên, ngày/thứ, lịch tuần và các thông số. Hai nút: "Đến phòng tập", "Về nhà nghỉ" (có hộp xác nhận, vì nghỉ là bỏ tập).
2. **Phòng tập**: bấm nhân vật để tập (tốn thể lực), mua bài tập, thách đấu, nhiệm vụ. Nút "Về nhà" có hộp xác nhận, trừ khi đã hết thể lực (lúc đó không thể là bấm nhầm). Thẻ bài tập rẻ nhất còn thiếu mục tiêu hạng kế được viền vàng; bấm thanh hạng thì mở tab Bài tập và cuộn tới thẻ đó.
3. **Nhà**: từ hạng 1 đi ngủ; từ hạng 2 có thể chọn hoặc bỏ bữa tối. Không hiện bảng bài tập ở nhà. Tab Nhiệm vụ mở từ hạng 4, Bạn tập mở từ hạng 5; sau đó bấm "Đi ngủ" sang ngày mới.

**Cửa chuyển cảnh** khi đi tập / về nhà (`door()`): hai cánh cửa khép lại kèm tiếng cửa lùa và "cạch" (0,3 giây), biển nơi đến hiện trên cửa, màn đổi lúc cửa kín, rồi cửa mở ra (0,4 giây); cả lượt khoảng 0,9–1,1 giây, mọi ngày như nhau. Chạm vào cửa (sau 0,25 giây đầu) thì phần còn lại chạy nhanh x6 chứ không cắt ngang. Có ảnh `bg-door-gym`, `bg-door-home` thì dùng, không thì cửa vẽ bằng CSS. Giảm chuyển động: cửa hiện/mờ tại chỗ.

**Qua đêm** (`sleepNight()`, khi bấm Đi ngủ): ngay trong căn nhà, trời tối dần phủ sân khấu (thanh chỉ số vẫn thấy), "Zzz" bay lên; ngày mới được tính lúc trời tối (`nextDay()`) nên thanh thể lực đầy dần ngay trước mắt; ba khung truyện (Khò khò, Buổi sáng, Đi đến công ty) hiện lần lượt; tiếng chim, trời chuyển cam rồi sáng; cuối cùng cửa văn phòng đóng mở và tới văn phòng (`arrive()`: thông báo ngày mới, lên hạng qua đêm). Cố ý chậm để người chơi xem: tối dần 0,7 giây, mỗi khung truyện 1,1 giây, dừng 0,6 giây, bình minh 1,1 giây, rồi cửa khoảng 1 giây: cả lượt khoảng 6,7 giây, mọi ngày như nhau; có tổng kết tuần hoặc cân kiểm tra thì dừng thêm 0,9 giây. Sau 1,2 giây hiện dòng "Chạm để tua nhanh"; chạm thì phần còn lại (kể cả cửa) chạy x6. Vắng hơn 24 giờ thì qua đêm không hoạt ảnh (`endDay()`).

Calo/giây chạy ở mọi màn, không tốn thể lực. Tắt game vẫn cộng calo, tối đa 8 giờ. Đang xem game mà 5 phút không chạm hay bấm phím (hằng `IDLE`) thì calo/giây tạm dừng, dòng nhắc hiện "Treo máy… Chạm để tiếp tục!"; chạm lại thì chạy tiếp. Treo máy không ra calo vô hạn. Chuyển sang tab khác hoặc tắt game thì tính như vắng mặt (tối đa 8 giờ kể từ lúc rời đi). Mở lại game tính là quay lại. Vắng hơn 24 giờ thật tính là 1 ngày nghỉ.

## Mở tính năng theo hạng

Tính theo hạng cao nhất từng đạt (`unl()`), nên lên đời không bị khoá lại.

| Hạng | Mở |
|---|---|
| 1 | Vòng cơ bản: bấm, bài tập, thể lực, về nhà và ngủ |
| 2 | Bữa tối, khách ghé phòng tập, Rep hoàn hảo và nước tăng lực (trên CrazyGames) |
| 3 | Mệt mỏi, lịch tuần, mục tiêu tuần và sự kiện văn phòng |
| 4 | Cân nặng bắt đầu chặn lên hạng; mở Thi đấu và Nhiệm vụ |
| 5 | Mở Bạn tập và Thành tựu |
| 6 | Mở Thử thách (tab Lên đời); tab Lên đời cũng có thể xuất hiện từ hạng 4 khi đủ Sao để lên đời |
| 7 | Thông báo sức mạnh siêu nhân thức tỉnh (phản diện mở theo số trận thắng, không theo hạng) |

Các tab tính năng chưa mở được ẩn, không hiện danh sách khoá. Khách, Rep và nước tăng lực (nếu có CrazyGames SDK) chỉ mở từ hạng 2; sự kiện văn phòng bắt đầu từ hạng 3. Mở khoá vẫn tính theo hạng cao nhất từng đạt nên lên đời không khoá lại.

## Bài tập

Giá cấp kế tiếp = giá gốc × 1,17^cấp. Đạt cấp 25, 50, 100 thì hiệu quả bài đó nhân đôi mỗi mốc.

| Bài | Giá gốc | Mỗi cấp |
|---|---|---|
| Tay | 15 | +1 calo/bấm |
| Vai | 100 | +1 calo/giây |
| Ngực | 1.100 | +8 calo/giây |
| Bụng | 12.000 | +47 calo/giây |
| Mắt | 40.000 | +12 calo/bấm |
| Chân | 130.000 | +260 calo/giây |
| Lưng | 1.400.000 | +1.400 calo/giây |
| Cardio | 20.000.000 | +7.800 calo/giây, +5 thể lực tối đa |

Calo mỗi cú bấm = (1 + tổng calo/bấm + 25% calo/giây gốc) × các hệ số (hằng `TAP`). Nhờ phần 25% này, cú bấm chiếm khoảng một nửa thu nhập ở mọi hạng (trước là 5%: hạng 5–6 chỉ còn 15%, bấm gần như vô nghĩa). Treo máy vẫn có calo, nhưng người chịu bấm được gấp đôi.

## Hạng

Lên hạng khi đủ cấp tối thiểu của **mọi** bài tập và cân nặng không quá ngưỡng. Đã lên thì không tụt.

| Hạng | Tên | Hệ số calo | Cấp tối thiểu (Tay, Vai, Ngực, Bụng, Mắt, Chân, Lưng, Cardio) | Cân tối đa |
|---|---|---|---|---|
| 1 | Dân văn phòng suy nhược | x1,25 | — | — |
| 2 | Tập tành cho vui | x1,5 | 5, 4, 2 | không chặn |
| 3 | Gymer nghiệp dư | x1,75 | 12, 10, 5, 1 | không chặn |
| 4 | Body săn chắc | x2 | 22, 18, 14, 8, 3 | 84,5 kg |
| 5 | Sáu múi lấp ló | x2,5 | 40, 35, 30, 22, 15, 10, 3 | 82 kg |
| 6 | Thần gym công sở | x3 | 70, 60, 55, 48, 40, 40, 32, 20 | 78 kg |
| 7 | Siêu nhân văn phòng | x3,5 | 85, 75, 70, 64, 55, 55, 45, 32 | 76 kg |
| 8 | Người hùng thành phố | x4 | 100, 92, 88, 80, 70, 70, 60, 44 | 74 kg |
| 9 | Hộ vệ Trái Đất | x5 | 120, 112, 106, 98, 88, 86, 76, 58 | 72 kg |

Bốn hạng đầu cố ý dễ và nhanh (hạng 4 khoảng 9–10 phút); hệ số calo hạng 1–3 cao hơn (x1,25 / x1,5 / x1,75) để bù việc khách ghé và Rep hoàn hảo chỉ mở từ hạng 2 để người mới quen vòng lặp; hạng 3 chỉ cần 4 bài tập đầu vì bài Mắt (40.000) quá đắt ở giai đoạn đó. Độ khó dồn về hạng 5–6 và các mốc sẽ thêm sau.

**Hạng 7–9 (sức mạnh siêu nhân)** dành cho các đời sau: giá bài tập tăng x1,17 mỗi cấp còn thu nhập tăng chậm hơn, nên đời đầu chạm "bức tường" sau hạng 7 và cách vượt là lên đời. Sim (người nghỉ khi Mỏi):

| | Đời 1 | Đời 2 (hệ số calo khoảng x4,5, giữ 78 kg) | Đời 3 (khoảng x11, 74 kg) |
|---|---|---|---|
| Hạng 7 | 2h21 | 32 phút | 16 phút |
| Hạng 8 | 5h48 | 1h12 | 36 phút |
| Hạng 9 | 25h25 | 5h29 | 2h03 |

Đã thử bộ mục tiêu cao hơn (hạng 9 cần cấp 150): đời 2 tới hạng 9 mất 13 giờ, bỏ. Cân tối đa 76 / 74 / 72 kg kéo người chơi về vùng lý tưởng 68–72 kg. Với mức giảm cân theo hạng, người nghỉ khi Mỏi đạt hạng 6 ở ngày 25 (1h16, 76,8 kg), nhanh hơn mốc cũ ngày 32; cân không còn là nút thắt tiến trình trong mô phỏng.

Có 2 nhân vật (nam, nữ), mỗi nhân vật 9 hình theo hạng. Chưa có ảnh hạng nào thì game dùng ảnh hạng thấp hơn gần nhất. Prompt ảnh hạng 7–9 và phản diện: `assets/PROMPTS.md` nhóm 14.

## Thể lực

- Tối đa = (300 + 120 × min(hạng, 5) + 5 × cấp Cardio) × hệ số mệt mỏi × (trên 90 kg: 0,8) × hệ số bữa ăn. Hạng tính từ 0. Từ hạng 7 thể lực không tăng theo hạng nữa: nếu tăng tiếp, một ngày ở hạng 9 dài hơn 6 phút.
- Mỗi cú bấm tốn 1 (miễn phí trong lúc đấu). Thách đấu tốn 40, Chủ nhật miễn phí.
- Đầy lại mỗi sáng.
- Quảng cáo thưởng "Nước tăng lực": +50% thể lực, một lần mỗi ngày.

## Mệt mỏi (0–100, từ hạng 3)

Mỗi ngày tập đủ cộng 40 điểm trước khi giảm 5 qua đêm; tập một phần thì tăng theo tỉ lệ thể lực đã dùng. Không có kỹ năng Hồi phục nhanh, bắt đầu từ 0 sẽ thành 35 → 70 → 100 sau ba ngày tập đủ liên tiếp. Ngày nghỉ −60.

| Mệt mỏi | Trạng thái | Thể lực tối đa |
|---|---|---|
| dưới 40 | Sung sức | 100% |
| 40–69 | Mỏi | 75% |
| 70–99 | Kiệt sức | 50% |
| 100 | Quá tải | bắt buộc nghỉ |

Lý do: tạo nhịp tập ba ngày rồi cần nghỉ, thay vì để người chơi tập đủ nhiều ngày liên tục. Mức tăng như nhau ở mọi hạng; kỹ năng Hồi phục nhanh vẫn giảm tốc độ tích mệt.

## Ngày nghỉ

- Ngày nghỉ là ngày dùng dưới 20% thể lực (hằng `REST`), kể cả có vào phòng tập bấm vài cú. Trước đây bấm 1 cú là tính ngày tập, thoát được phạt lười.
- Nghỉ khi mệt mỏi từ 40: hôm sau có "Hồi phục" (calo/bấm +25%), +0,1 kg.
- Nghỉ khi mệt mỏi dưới 40 (lười): không có Hồi phục, +0,3 kg.

## Cân nặng

- Bắt đầu 85 kg, giới hạn 68–120 kg. Sàn 68 kg là đáy vùng lý tưởng: người tập đều (kể cả ăn lành mạnh mỗi tối) dừng ở 68 kg và giữ được thưởng calo +20%; trước đây sàn 65 kg làm họ rơi khỏi vùng quanh ngày 60.
- **Tập là cách giảm cân chính**: dùng hết thanh thể lực giảm theo hạng; tập một phần thì giảm theo tỉ lệ. Hạng 1–3 giảm 0,3 kg; hạng 4–9 lần lượt giảm 0,4–0,9 kg mỗi ngày tập đủ. Thử thách Mùa tiệc cưới cộng thêm 0,1 kg giảm cho mỗi ngày tập đủ. Thông báo đầu ngày ghi phần tập/nghỉ, phần ăn uống và sự kiện trong ngày (đã cộng ngay lúc chọn), và tổng thay đổi so với sáng hôm trước (trường `kg1` = cân đầu ngày). Nếu qua đêm lên hạng, thông báo lên hạng hiện trước, báo cân xếp hàng sau.
- Vùng lý tưởng 68–72 kg: calo +20%. Trên 90 kg: thể lực tối đa −20%.
- Cân kiểm tra mỗi 30 ngày: 1 Sao cho mỗi 2 kg giảm so với lần trước.

## Bữa tối (từ hạng 2)

Mỗi tối bày 3 món, mỗi nhóm một món, đổi theo ngày (chu kỳ 9 ngày). Bữa ăn miễn phí: chọn tối đa một món, có thể bỏ bữa. Món ăn chỉ tác động lên chỉ số (cân nặng, thể lực, calo, mệt mỏi), không tốn calo.

| Nhóm | Món | Cân nặng | Hiệu ứng |
|---|---|---|---|
| Lành mạnh | Cơm gà luộc | −0,1 kg | mai: thể lực +10% |
| Lành mạnh | Salad cá hồi | −0,2 kg | mai: thể lực +5% |
| Lành mạnh | Yến mạch chuối | −0,1 kg | mệt mỏi −10 ngay |
| Đạm | Ức gà, trứng | 0 | mai: calo +25% |
| Đạm | Bò bít tết | +0,1 kg | mai: calo +35% |
| Đạm | Sinh tố whey | 0 | mai: thể lực +10%, calo +10% |
| Ăn vặt | Trà sữa, gà rán | +0,2 kg | mai: thể lực +50%, bấm x1,5, calo +10% |
| Ăn vặt | Pizza phô mai | +0,25 kg | mai: thể lực +70%, calo +15% |
| Ăn vặt | Mì tôm trứng | +0,1 kg | mai: bấm x1,3; mệt mỏi −5 ngay |

Vai trò từng nhóm: lành mạnh để siết cân; đạm tăng thu nhập mà không (hoặc gần như không) tăng cân; ăn vặt tăng nhiều chỉ số nhất nhưng tăng cân. **Ràng buộc**: món ăn vặt luôn tăng cân ít hơn 0,3 kg, để ngày tập đủ thì cân không tăng (trước đây ăn vặt mỗi tối làm kẹt vĩnh viễn).

## Lịch tuần (từ hạng 3)

- Tuần 7 ngày, ngày 1 là Thứ Hai.
- Mục tiêu tuần: 4 buổi (hạng 1–2), 5 buổi (hạng 3–4), 6 buổi (hạng 5–6). Một buổi = dùng ít nhất nửa thanh thể lực. Đạt thì tuần sau calo +10%.
- Chủ nhật: thách đấu miễn phí thể lực, thưởng calo x2.

## Thách đấu

Mở từ hạng 4; trước đó ẩn tab và không hiện chỉ số số trận thắng.

30 đối thủ theo thứ tự, 6 giải: Phòng ban, Công ty, Phòng gym, Giải quốc gia, rồi **phản diện trên Trái Đất**: Thế giới ngầm (Hàm Thép, Bà trùm Hổ Mang, Tiến sĩ Độc Dược, Gã Máy Xúc, Ông trùm Mặt Nạ Bạc) và Trùm Trái Đất (Tướng Bão Tố, Nữ hoàng Băng Giá, Titan Dung Nham, Siêu máy tính Omega, Hắc Vương Lõi Đất). Ngoài Trái Đất để dành cho lần mở rộng sau.

Mục tiêu đối thủ thứ i (từ 0) = 300 × 2,4^min(i, 19) × 1,25^max(0, i − 19) calo trong 15 giây (phản diện chỉ khó hơn x1,25 mỗi người: giữ x2,4 thì không ai đánh nổi; sim: đời 3 tới hạng 9 đã hạ 6 phản diện, 4 trùm còn lại là mục tiêu dài hạn); thưởng = mục tiêu × 3. Mỗi trận thắng +3% calo vĩnh viễn.

**Đấu trường** (chi tiết và toàn bộ lời thoại: [ARENA_PLAN.md](ARENA_PLAN.md)): thách đấu mở một màn riêng che cả khung, nền theo giải (phòng họp, sàn đấu, bãi xe ngầm, hang dung nham). Thứ tự: màn VS (1,3 giây) → thoại → đếm ngược 3·2·1·ĐẤU → 15 giây đấu → đối thủ nói câu kết → nút "Về phòng tập" (thua thì thêm "Đấu lại ⚡40").

- Lần đầu gặp đối thủ: xem hết thoại (giải 1–2 một câu, 3–4 hai câu, 5–6 ba câu, rồi nhân vật đáp một câu). Gặp lại (đấu lại sau khi thua): một câu. Đã gặp lưu ở `s.met`.
- Thoại có chữ chạy; chạm để hiện hết câu, chạm nữa để sang câu kế. Xưng hô `{anh|chị}` theo nhân vật.
- **Đấu đòn**: thanh mỗi bên chỉ tăng khi bên đó ra đòn (hằng `HIT`). Đòn của bạn: mỗi cú bấm, tối đa 20% thanh mỗi đòn, hai đòn cách nhau ít nhất 0,55 giây; không bấm thì cứ 0,7 giây tự ra đòn bằng calo/giây đã tích. Số sát thương đỏ hiện trên đối thủ; chỗ bấm chỉ hiện 👊 (số "+…" trông như được calo). Đối thủ ra đòn mỗi 0,8–1,4 giây, thanh đỏ nhảy tới đúng tỉ lệ thời gian đã trôi, đầy lúc hết giờ. Thắng thua vẫn theo tổng sát thương thật (hết giờ mà đủ sát thương thì có đòn kết liễu), nên độ khó không đổi. Lý do: trước đây đánh kẻ yếu thì thanh đầy ngay khung hình đầu, không thấy đánh nhau; giờ kẻ yếu nhất cũng mất khoảng 2,5 giây, 5 đòn của bạn và 2 đòn của đối thủ.
- **Trong trận, cú bấm chỉ đẩy thanh đấu, không ra calo** (trước đây vừa đẩy thanh vừa cộng calo, trận đấu không khác gì phòng tập). Calo/giây vẫn chạy ngầm và vẫn tính vào thanh đấu. Sim: hạng 6 chậm thêm 1–2 phút (mất calo từ cú bấm trong trận và khoảng 6 giây VS, thoại, đếm ngược mỗi trận).
- Mạch truyện: đồng nghiệp (giải 1–2) → người tập thật (3–4) → phản diện sống nhờ sự lười biếng của con người, nuôi Hắc Vương Lõi Đất (5–6); câu thua của Hắc Vương mở đường ra ngoài Trái Đất.

## Bạn tập

Mở từ hạng 5. Gọi ngẫu nhiên, giá 5.000 × 2,5^số lần đã gọi. Gọi trùng thì lên cấp. Tab Bạn tập chỉ hiện ở nhà.

| Độ hiếm | Tỉ lệ mỗi con | Bạn tập | Mỗi cấp |
|---|---|---|---|
| Thường | 20% | Cún, Hamster | +5% calo/giây |
| Thường | 20% | Mèo, Ếch | +5% calo/bấm |
| Hiếm | 7% | Khỉ đột / Kangaroo | +15% calo/giây / calo/bấm |
| Sử thi | 5% | Hổ | +15% cả hai |
| Huyền thoại | 1% | Rồng | +40% cả hai |

## Nhiệm vụ, thành tựu, lên đời

- **Nhiệm vụ ngày** (mở hạng 4): mỗi ngày chọn 3 loại khả dụng trong nhóm bấm 200, mua 20 cấp, đấu 1, gọi bạn tập 1, chơi 120 giây. Nhiệm vụ gọi bạn tập chỉ vào nhóm khả dụng từ hạng 5, khi tab Bạn tập đã mở. Làm mới theo ngày trong game. Thưởng = 300 giây thu nhập, tối thiểu 500.
- **Thành tựu** (mở hạng 5): 21 cái (thêm đạt hạng 9, thắng 30 đối thủ), mỗi cái +1% calo vĩnh viễn.
- **Lên đời**: nhận Sao = ⌊∛(calo kiếm được trong đời này / 1 triệu)⌋, mỗi Sao +10% calo. Chỉ xoá calo, cấp bài tập và hạng; ngày, cân nặng, mệt mỏi, bạn tập, trận thắng, kỹ năng, thử thách đã xong giữ nguyên. Lên đời thường khi đang làm thử thách thì bỏ thử thách.

## Kỹ năng Sao (cuối tab Lên đời)

Sao vừa là thưởng vừa là tiền: mỗi Sao **vẫn giữ +10% calo kể cả khi đã tiêu** (như cấp uy tín của Cookie Clicker), nên học kỹ năng không bao giờ làm người chơi yếu đi. Sao chưa dùng = tổng Sao − Sao đã tiêu (tính lại từ cấp kỹ năng, không lưu riêng).

Ba nhánh, mỗi nhánh ba kỹ năng; học kỹ năng sau cần cấp 1 của kỹ năng trước trong nhánh. Cấp kế tốn `giá × (cấp hiện tại + 1)` Sao. Học hết tốn 116 Sao; đời đầu tới hạng 6 được khoảng 21 Sao (sim), nên cần vài lần lên đời.

| Nhánh | Kỹ năng | Giá | Tối đa | Mỗi cấp |
|---|---|---|---|---|
| 💪 Sức mạnh | Cú bấm vàng | 1 | 5 | +25% calo/bấm |
| | Ký ức cơ bắp | 3 | 2 | Đời mới bắt đầu ở hạng 2 / hạng 3, đủ cấp bài tập của hạng đó |
| | Bấm chí mạng | 4 | 3 | 5% cú bấm được x10 |
| ⚡ Bền bỉ | Phổi thép | 1 | 5 | +10% thể lực tối đa |
| | Hồi phục nhanh | 3 | 3 | Mệt mỏi tăng chậm hơn 15% |
| | Đấu tiết kiệm | 5 | 1 | Thách đấu tốn 20 thể lực thay vì 40 |
| 🌟 Lối sống | Đầu tư dài hạn | 1 | 5 | +25% calo/giây |
| | Khách quen | 3 | 2 | +1 khách ghé phòng tập mỗi ngày |
| | Ngủ ngon | 2 | 2 | Calo lúc vắng mặt tính thêm 4 giờ (gốc 8 giờ) |

Ảnh: `assets/icon/icon-sk-<khoá>.webp` và `icon-ch-<khoá>.webp` (thiếu ảnh thì hiện emoji). Nhánh nào cũng có một kỹ năng rẻ (giá 1) để lần đầu có Sao là học được ngay. Sim chưa mô phỏng kỹ năng (sim chỉ chạy đời đầu).

## Thử thách (từ hạng 6, cuối tab Lên đời)

Bắt đầu thử thách = lên đời (vẫn nhận Sao) với một luật khó. Đạt hạng mục tiêu dưới luật đó thì luật hết, nhận thưởng vĩnh viễn; mỗi thử thách làm một lần. Bỏ giữa chừng hoặc lên đời thường: luật hết, không thưởng. Đang làm thì có nhãn hồng dưới thanh calo. Lưu ở `s.ch` (đang làm) và `s.chd` (đã xong); hằng số `CH`, `CHX`.

| Thử thách | Luật | Mục tiêu | Thưởng vĩnh viễn | Sim (sau đời đầu) |
|---|---|---|---|---|
| 👆 Chỉ dùng tay | Không có calo/giây (cả lúc vắng mặt); cú bấm vẫn ăn 25% calo/giây gốc | Hạng 6 | +25% calo/bấm | 31 phút |
| 🏷️ Phòng gym tăng giá | Bài tập đắt x3 | Hạng 6 | Bài tập rẻ hơn 10% | 43 phút |
| 🎉 Mùa tiệc cưới | Bắt đầu ở ít nhất 85 kg, mỗi tối +0,1 kg | Hạng 5 | Ngày tập đủ giảm thêm 0,1 kg | 55 phút |
| 👔 Sếp soi | Calo x0,25 | Hạng 6 | +15% calo | 1 giờ |

Cân bằng: sau đời đầu (hệ số calo khoảng x4,5 nhờ Sao, trận thắng, thành tựu; giữ cân 78 kg) một đời thường tới hạng 6 chỉ 17 phút, nên mỗi thử thách nhắm 30–60 phút. Đo bằng `run(G, …)` trong `tools/sim.py` với `mults` x4,5, `kg0`, `night`, `hands`, `fee`. Đã loại: cắt thể lực (Tăng ca) gần như không làm chậm vì về sau calo/giây chiếm phần lớn; Sếp soi x0,5 và đích hạng 5 chỉ 10 phút; Tiệc cưới 88 kg +0,2/tối mất 5 giờ.

## Khách ghé phòng tập

Mở từ hạng 2. Lấy ý từ bánh quy vàng của Cookie Clicker: phần thưởng bất ngờ để người chơi nhìn màn hình thay vì treo máy. Có ba loại khách, hai loại sau là **lựa chọn**: bấm hay bỏ qua.

- Chỉ hiện ở phòng tập, ngoài trận đấu, khi không có màn chờ, hộp xác nhận hay hướng dẫn. Lần đầu sau khoảng 30 giây ở phòng tập, sau đó mỗi 60–120 giây ở phòng tập. **Tối đa 3 khách mỗi ngày** (lưu trong `s.vis`, sang ngày mới về 0). Chế độ thử: nhanh gấp 10, vẫn tối đa 3.
- Lý do giới hạn: quà thể lực kéo dài buổi tập, buổi tập dài lại có thêm khách. Khi chơi thật vòng này yếu (trung bình 0,8–2,6 khách/ngày, ngày tập dài thêm 4–12%), nhưng khách đến dày (chế độ thử) thì ngày gần như không bao giờ hết: thể lực 1.000 thì trung bình 82 phút/ngày, khoảng 540 khách. Giới hạn 3 khách chặn vòng này mà gần như không đổi gì khi chơi thật. Giảm quà thể lực xuống 15% không đủ (chế độ thử vẫn dài gấp đôi).
- Khách là một vòng tròn nhấp nháy, mỗi loại một màu, kèm nhãn bên dưới (76px trên điện thoại, 110px trên máy tính). Ở lại 8 giây; không bấm thì đi mất, không phạt.

| Khách | Tỉ lệ | Nhãn | Bấm vào |
|---|---|---|---|
| 🧑‍🏫 PT (vàng) | 50% | Bấm tôi! | Luôn có quà, ngẫu nhiên đều: bấm x5 trong 8 giây / +30% thể lực tối đa / thưởng calo |
| 💃 Crush (hồng), đi ngang qua màn hình | 30% | Bắt chuyện? | 65%: crush cười, được bấm x7 trong 10 giây hoặc thưởng calo x2 (đều nhau). 35%: crush ngó lơ, mất 10% thể lực đang có |
| 🎂 Bánh sinh nhật đồng nghiệp (xanh) | 20% | Ăn bánh? | Thưởng calo x1,5 nhưng +0,1 kg |

- Thưởng calo = 60 giây calo/giây + 30 cú bấm. Trong lúc bấm x5 / x7 vầng sáng quanh nhân vật chuyển cam; mỗi cú vẫn tốn 1 thể lực.
- Khi chưa từng bấm khách nào, khách đầu tiên mỗi lần mở game là PT (người mới không gặp ngay crush ngó lơ), các khách sau ngẫu nhiên theo tỉ lệ. Lần đầu bấm PT luôn cho thưởng calo, rồi hiện mục hướng dẫn "Khách ghé phòng tập" (để khung hướng dẫn không làm phí 8 giây bấm x5).
- Không lưu gì: tải lại trang thì đếm lại từ đầu. Hằng số ở `PT` và `VIS` trong `index.html`. Ảnh: `assets/icon/icon-vis-pt|crush|cake.webp` (thiếu ảnh thì hiện emoji).

## Rep hoàn hảo

Mở từ hạng 2, cho cú bấm một chút kỹ năng (giống nạp đạn chủ động của Gears of War, thanh lực đánh golf). Hằng số `REP` trong `index.html`.

- Sau khoảng 30 cú bấm (ngẫu nhiên 25–35), **báo trước 2 giây**: viền đích vàng nhấp nháy kèm chữ "Sắp có Rep hoàn hảo, chuẩn bị!" (vẫn bấm bình thường, không chấm điểm). Sau đó một vòng trắng co dần quanh nhân vật trong 1,1 giây; viền đứt nét là đích. Vòng chuyển vàng trong khoảng 50–70% thời gian (±110 ms quanh lúc chạm đích).
- **Cú bấm ngay sau khi vòng hiện** được chấm: rơi vào lúc vàng là PERFECT, cú đó x5; PERFECT liên tiếp x6, x7… tối đa x10. Sớm hay trễ là hụt, mất chuỗi. Không bấm thì vòng tự biến mất, cũng mất chuỗi.
- Bấm liên tục (4 lần/giây) thì cú kế tiếp tới sau khoảng 250 ms, luôn hụt: muốn PERFECT phải dừng tay một nhịp. Đó là đánh đổi: chậm hơn chút, nhưng cùng một thanh thể lực ra nhiều calo hơn. Mỗi cú vẫn tốn 1 thể lực như thường.
- Ban đầu là 15 cú và không báo trước: chơi thử thấy đến quá dày, bị bất ngờ nên bỏ qua.
- Không hiện trong trận đấu, lúc đang bấm x5/x7 của khách (bắt đầu đấu hay bấm x5/x7 trong lúc báo trước thì huỷ vòng), và trong 20 cú bấm đầu tiên của người mới. Vòng đầu tiên có chữ "Đợi vòng vàng rồi bấm!" cho tới lần PERFECT đầu (lưu ở `s.tips.rep`).
- Cân bằng (sim, tham số `rep_p` = tỉ lệ PERFECT): calo thêm trung bình mỗi vòng = 1,3 / 2,5 / 5,4 / 7,9 cú bấm với tỉ lệ 30 / 50 / 80 / 95% (mỗi 30 cú bấm). **Số ngày lên hạng không đổi** dù bắt vòng giỏi hay không, vì từ hạng 4 tiến độ bị chặn bởi cân nặng và thể lực mỗi ngày; người giỏi có thêm calo cho bạn tập và thi đấu (phần calo từ cú bấm của người quen: 45% → 49%). Giá phải trả: khoảng 0,4 giây dừng tay mỗi vòng, làm tổng thời gian tới hạng 6 dài thêm 3–4 phút.

## Sự kiện văn phòng

Mở từ hạng 3. Mỗi ngày từ ngày 2 có một tình huống với hai lựa chọn: chữ trong khung vàng, hai nút ghi rõ tác dụng. Danh sách `EV` trong `index.html`.

- Chọn sự kiện lúc sang ngày, ngẫu nhiên, không lặp lại sự kiện hôm qua; lưu ở `s.ev` (tải lại trang không đổi được). Không chọn mà đi tập hay về nhà thì bỏ qua sự kiện đó.
- Tác dụng: cân nặng, mệt mỏi, thể lực (theo % thể lực tối đa) cộng ngay; calo = số giây thu nhập như phần thưởng nhiệm vụ; "hôm nay" (calo hoặc sức bấm) kéo dài tới khi đi ngủ, lưu ở `s.buff`; Sao.
- Lựa chọn may rủi ghi tỉ lệ trên nút; kết quả hiện trong thông báo ("Thành công" / "Không may").
- Sự kiện về mệt mỏi chỉ xuất hiện từ hạng 3 (khi mệt mỏi đã mở).

| Sự kiện | Lựa chọn A | Lựa chọn B |
|---|---|---|
| Sếp rủ làm vài ly | +0,3 kg, calo (300 giây) | thể lực +10% |
| Thang máy hỏng, tầng 12 | thể lực −15%, −0,1 kg, bấm hôm nay +20% | thể lực +5% |
| Sếp nhờ tăng ca | thể lực −20%, calo (600 giây) | 50%: không sao; còn lại calo hôm nay −10% |
| Trà sữa full topping | +0,2 kg, thể lực +20% | −0,1 kg |
| Bàn làm việc đứng | thể lực −10%, calo hôm nay +15% | thể lực +10% |
| Bốc thăm quà | 30%: +1 Sao; còn lại thể lực −5% | thể lực +5% |
| Yoga trưa (hạng 3) | mệt mỏi −15 | thể lực +10% |
| Deadline (hạng 3) | mệt mỏi +10, calo (600 giây) | bấm hôm nay +15% |
| Crush rủ ăn trưa | 60%: bấm hôm nay +30%; còn lại thể lực −10% | −0,1 kg |
| Đạp xe về | −0,15 kg, thể lực −10% | thể lực +10% |
| Phiếu massage (hạng 3) | mệt mỏi −10, thể lực −5% | calo hôm nay +10% |

Tác dụng nhỏ so với bữa tối và nghỉ ngơi, nên sim chưa mô phỏng sự kiện.

## Hướng dẫn

- Khung thoại của hướng dẫn dùng cùng kiểu bảng tên và hộp thoại dưới màn hình như lúc gặp đối thủ ở đấu trường; ảnh chó con Bắp đứng cạnh khung. Khi bắt đầu ván mới, màn chơi hiện nhẹ trước, rồi Bắp xuất hiện và mở đầu câu chuyện; chuyển động tôn trọng cài đặt giảm chuyển động.
- Lần đầu mở ván mới, người chơi bắt đầu ở văn phòng. Bắp dẫn chuyện qua năm bước: giới thiệu game và hành trình, sau đó chỉ nút vào phòng tập, cách chạm để kiếm calo và dùng calo mua bài tập. Khi hoàn tất, nút "Đến phòng tập" được focus; các mẹo về tập và hồi thể lực xuất hiện đúng lúc. Chỉ nút "Tiếp tục"/"Đã hiểu" mới chuyển bước hoặc đóng ở bước cuối; bấm nền và Esc không bỏ qua hướng dẫn. Nút nhấp nhẹ để người chơi nhận ra cách tiếp tục.
- Lần đầu đủ calo mua bài Tay ở phòng tập, nút mua Tay nháy nhẹ hai nhịp đúng một lần trong ván lưu; các nút bài tập khác không nháy. Cờ nhắc được lưu để không lặp lại sau khi tải trang.
- **Gợi ý lần đầu** chỉ hiện khi gặp tính năng đã mở; mỗi câu chỉ hiện một lần và được lưu vào `s.tips`. Mẹo khác mở theo hạng và ngữ cảnh. Bấm ❓ để xem lại những mục đã mở.
- Không giải thích con số hay chiến lược nâng cao trước khi cần; ưu tiên hành động kế tiếp. Cửa sổ chat đóng được bằng nút, nền hoặc phím Esc.

## Chống auto-click

Cú bấm nhân vật phải là cú bấm thật và cách cú trước ít nhất 50 ms (tối đa 20 lần/giây). Thể lực cũng giới hạn tổng số cú bấm mỗi ngày.

## CrazyGames

SDK v3. Lưu qua `SDK.data`. Quảng cáo giữa game: sau khi ngủ, mỗi 3 ngày một lần, và khi lên đời. Quảng cáo thưởng: nước tăng lực. Tắt tiếng khi có quảng cáo. Không có SDK thì game vẫn chạy, không có quảng cáo.

Ngôn ngữ: người chơi lần đầu luôn thấy tiếng Anh (khán giả CrazyGames phần lớn nói tiếng Anh), đổi sang tiếng Việt trong khung cài đặt ⚙️. Lựa chọn được lưu; bản lưu cũ giữ ngôn ngữ đang dùng.

Âm lượng: khung cài đặt ⚙️ có hai thanh 0–10 nấc, nhạc nền mặc định 5, hiệu ứng mặc định 7 (chốt sau khi chủ dự án nghe thử). Nấc v nhân âm lượng với (v/5)²: nấc 5 là mức gốc, nấc 7 to hơn khoảng 6 dB, nấc 3 nhỏ hơn khoảng 9 dB. Bản lưu cũ có nút loa 3 trạng thái: "tắt nhạc" thành nhạc 0, "tắt hết" thành cả hai 0, còn lại dùng mặc định.

## Mục tiêu cân bằng

Đo bằng `python tools/sim.py` (4 lần bấm/giây, ăn cơm gà, bấm mọi khách; thời gian là tổng thời gian chơi tới hạng đó). Kết quả sau khi tăng mệt mỏi, giảm cân theo hạng và mở tính năng theo hạng (khách ghé, Rep hoàn hảo từ hạng 2; thi đấu từ hạng 4; bạn tập từ hạng 5) và tăng hệ số calo hạng 1–3, rồi nâng sàn cân lên 68 kg (chỉ hạng 7–9 đổi):

| Hạng | Không chủ động nghỉ (vẫn bắt buộc nghỉ ở 100) | Tự nghỉ khi Mỏi (mệt ≥40) |
|---|---|---|
| 2 | ngày 2, 1m45 | ngày 2, 1m45 |
| 3 | ngày 3, 4m52 | ngày 3, 4m52 |
| 4 | ngày 4, 9m38 | ngày 4, 9m38 |
| 5 | ngày 9, 21m55 | ngày 10, 27m06 |
| 6 | ngày 34, 1h17 | ngày 25, 1h16 |
| 7 | ngày 53, 2h12 | ngày 42, 2h21 |
| 8 | ngày 113, 5h11 | ngày 84, 5h14 |
| 9 | — | ngày 309, 21h35 |

Các ước tính cũ về tác động riêng của khách ghé và Rep hoàn hảo bên dưới được đo trước khi tăng mệt mỏi; cần chạy lại nếu cân bằng lại hai tính năng đó. Sim hiện giả định khách xoay vòng đúng tỉ lệ và người chơi bấm mọi khách, kể cả bánh.

- Một ngày dài ít nhất 2 phút chơi ở mọi hạng.
- Hạng 2 trong khoảng 2 phút, hạng 4 dưới 10 phút; hạng 5 → 6 khoảng 50 phút nếu nghỉ khi Mỏi; hạng 6 tổng khoảng 1h15.
- Cú bấm chiếm 40–55% calo từ hạng 2 trở đi.
- Nghỉ khi Mỏi giúp lên hạng 6+ sớm hơn; ở hạng 5, nghỉ quá thường xuyên có thể chậm hơn không nghỉ.
- Người tập đều không bị cân nặng chặn quá 1–3 ngày.
