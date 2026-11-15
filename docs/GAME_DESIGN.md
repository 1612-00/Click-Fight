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

1. **Văn phòng**: mở game luôn ở đây (trừ ván mới: vào thẳng phòng tập để bấm được ngay). Chỉ có câu nói ngẫu nhiên, ngày/thứ, lịch tuần và các thông số. Hai nút: "Đến phòng tập", "Về nhà nghỉ" (có hộp xác nhận, vì nghỉ là bỏ tập).
2. **Phòng tập**: bấm nhân vật để tập (tốn thể lực), mua bài tập, thách đấu, nhiệm vụ. Nút "Về nhà" có hộp xác nhận, trừ khi đã hết thể lực (lúc đó không thể là bấm nhầm). Thẻ bài tập rẻ nhất còn thiếu mục tiêu hạng kế được viền vàng; bấm thanh hạng thì mở tab Bài tập và cuộn tới thẻ đó.
3. **Nhà**: chọn một bữa tối, xem/gọi bạn tập, bấm "Đi ngủ" sang ngày mới.

**Màn chờ** giữa các màn: đi tập / về nhà 2 giây, chuỗi đi ngủ 8,5 giây (Khò khò → Buổi sáng → Đi đến công ty → Đang làm việc). Ba ngày đầu chạy đủ để kể chuyện; từ ngày 4 còn 40% (0,8 giây và 3,4 giây), vì lặp 40–50 lần thì 12,5 giây mỗi ngày là khoảng 8% thời gian chơi. Chạm vào màn chờ để bỏ qua (sau 0,4 giây đầu, để cú bấm vừa rồi không vô tình bỏ qua luôn).

Calo/giây chạy ở mọi màn, không tốn thể lực. Tắt game vẫn cộng calo, tối đa 8 giờ. Vắng hơn 24 giờ thật tính là 1 ngày nghỉ.

## Mở tính năng theo hạng

Tính theo hạng cao nhất từng đạt (`unl()`), nên lên đời không bị khoá lại.

| Hạng | Mở |
|---|---|
| 1 | Thể lực, bài tập, thách đấu, nhiệm vụ, bạn tập |
| 2 | Bữa tối ở nhà |
| 3 | Mệt mỏi, lịch tuần và mục tiêu tuần |
| 4 | Cân nặng bắt đầu chặn lên hạng |
| 6 | Thử thách (tab Lên đời) |

Lần đầu đạt hạng 2 và 3, thông báo lên hạng nói rõ tính năng vừa mở.

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
| 1 | Dân văn phòng suy nhược | x1 | — | — |
| 2 | Tập tành cho vui | x1,25 | 5, 4, 2 | không chặn |
| 3 | Gymer nghiệp dư | x1,5 | 12, 10, 5, 1 | không chặn |
| 4 | Body săn chắc | x2 | 22, 18, 14, 8, 3 | 84,5 kg |
| 5 | Sáu múi lấp ló | x2,5 | 40, 35, 30, 22, 15, 10, 3 | 82 kg |
| 6 | Thần gym công sở | x3 | 70, 60, 55, 48, 40, 40, 32, 20 | 78 kg |

Bốn hạng đầu cố ý dễ và nhanh (hạng 4 trong khoảng 8–9 phút) để người mới quen vòng lặp; hạng 3 chỉ cần 4 bài tập đầu vì bài Mắt (40.000) quá đắt ở giai đoạn đó. Độ khó dồn về hạng 5–6 và các mốc sẽ thêm sau.

Có 2 nhân vật (nam, nữ), mỗi nhân vật 6 hình theo hạng.

## Thể lực

- Tối đa = (300 + 120 × hạng + 5 × cấp Cardio) × hệ số mệt mỏi × (trên 90 kg: 0,8) × hệ số bữa ăn. Hạng tính từ 0.
- Mỗi cú bấm tốn 1 (miễn phí trong lúc đấu). Thách đấu tốn 40, Chủ nhật miễn phí.
- Đầy lại mỗi sáng.
- Quảng cáo thưởng "Nước tăng lực": +50% thể lực, một lần mỗi ngày.

## Mệt mỏi (0–100, từ hạng 3)

Tập hết thanh thể lực cộng theo hạng: 30, 26, 22, 18, 14, 10 (hạng 1 → 6); tập một phần thì theo tỉ lệ. Ngủ sau ngày tập −5. Ngày nghỉ −60.

| Mệt mỏi | Trạng thái | Thể lực tối đa |
|---|---|---|
| dưới 40 | Sung sức | 100% |
| 40–69 | Mỏi | 75% |
| 70–99 | Kiệt sức | 50% |
| 100 | Quá tải | bắt buộc nghỉ |

Lý do: hạng thấp nhanh mệt, hạng cao lâu mệt, để người chơi tự xếp ngày nghỉ trong tuần.

## Ngày nghỉ

- Nghỉ khi mệt mỏi từ 40: hôm sau có "Hồi phục" (calo/bấm +25%), +0,1 kg.
- Nghỉ khi mệt mỏi dưới 40 (lười): không có Hồi phục, +0,3 kg.

## Cân nặng

- Bắt đầu 85 kg, giới hạn 65–120 kg.
- **Tập là cách giảm cân chính**: hết thanh thể lực −0,3 kg (một phần thì theo tỉ lệ). Thông báo đầu ngày ghi rõ số kg vừa giảm.
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

20 đối thủ theo thứ tự. Mục tiêu đối thủ thứ i (từ 0) = 300 × 2,4^i calo trong 15 giây; thưởng = mục tiêu × 3. Mỗi trận thắng +3% calo vĩnh viễn. Màn đấu: hai nhân vật hai bên, hai thanh chạy đua; thanh đối thủ đầy đúng lúc hết giờ.

## Bạn tập

Gọi ngẫu nhiên, giá 5.000 × 2,5^số lần đã gọi. Gọi trùng thì lên cấp. Tab Bạn tập chỉ hiện ở nhà.

| Độ hiếm | Tỉ lệ mỗi con | Bạn tập | Mỗi cấp |
|---|---|---|---|
| Thường | 20% | Cún, Hamster | +5% calo/giây |
| Thường | 20% | Mèo, Ếch | +5% calo/bấm |
| Hiếm | 7% | Khỉ đột / Kangaroo | +15% calo/giây / calo/bấm |
| Sử thi | 5% | Hổ | +15% cả hai |
| Huyền thoại | 1% | Rồng | +40% cả hai |

## Nhiệm vụ, thành tựu, lên đời

- **Nhiệm vụ ngày**: 3 trong 5 loại (bấm 200, mua 20 cấp, đấu 1, gọi 1, chơi 120 giây), làm mới theo ngày trong game. Thưởng = 300 giây thu nhập, tối thiểu 500.
- **Thành tựu**: 19 cái, mỗi cái +1% calo vĩnh viễn.
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
| 🎉 Mùa tiệc cưới | Bắt đầu ở ít nhất 85 kg, mỗi tối +0,1 kg | Hạng 5 | Ngày tập đủ giảm 0,4 kg thay vì 0,3 | 55 phút |
| 👔 Sếp soi | Calo x0,25 | Hạng 6 | +15% calo | 1 giờ |

Cân bằng: sau đời đầu (hệ số calo khoảng x4,5 nhờ Sao, trận thắng, thành tựu; giữ cân 78 kg) một đời thường tới hạng 6 chỉ 17 phút, nên mỗi thử thách nhắm 30–60 phút. Đo bằng `run(G, …)` trong `tools/sim.py` với `mults` x4,5, `kg0`, `night`, `hands`, `fee`. Đã loại: cắt thể lực (Tăng ca) gần như không làm chậm vì về sau calo/giây chiếm phần lớn; Sếp soi x0,5 và đích hạng 5 chỉ 10 phút; Tiệc cưới 88 kg +0,2/tối mất 5 giờ.

## Khách ghé phòng tập

Lấy ý từ bánh quy vàng của Cookie Clicker: phần thưởng bất ngờ để người chơi nhìn màn hình thay vì treo máy. Có ba loại khách, hai loại sau là **lựa chọn**: bấm hay bỏ qua.

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

## Hướng dẫn

- **Nút ❓** trên cùng mở toàn bộ hướng dẫn, 11 mục: một ngày, bấm hay để calo tự chạy, hết thể lực, khách ghé phòng tập, buổi tối ở nhà, bữa tối, mệt mỏi, cân nặng, thi đấu, lên đời (kèm kỹ năng Sao), thử thách. Mục chưa mở hiện "🔒 Mở khi đạt hạng N" thay cho nội dung.
- **Gợi ý lần đầu**: mỗi mục tự hiện một lần khi người chơi gặp nó. Ván mới không có khung nào chặn: chỉ có bàn tay 👆 chỉ vào nhân vật cho tới cú bấm thứ 5. Lần hết thể lực đầu tiên (chỗ nghỉ tự nhiên) hiện cùng lúc hết thể lực, bấm hay để calo tự chạy, một ngày. Sau đó: mở game ở văn phòng (một ngày), vào phòng tập, về nhà (nhà, bữa tối, mệt mỏi, cân nặng, mục nào đã mở thì hiện), lần đầu mở tab Thi đấu, tab Lên đời (thêm mục thử thách khi đã đạt hạng 6), lần đầu bấm vào khách. Đã hiện thì lưu vào `s.tips`.
- Bản lưu có từ trước khi có hướng dẫn: coi như đã xem 4 mục cơ bản, chỉ còn gợi ý các tính năng.
- Mục đích chính là nói rõ các **đánh đổi**: bấm (tốn thể lực) và calo/giây; ăn vặt (tập nhiều, tăng cân) và healthy; nghỉ lúc mỏi (thưởng) và nghỉ lúc sung sức (lười); 40 thể lực cho một trận đấu; lên đời mất gì, giữ gì.

## Chống auto-click

Cú bấm nhân vật phải là cú bấm thật và cách cú trước ít nhất 50 ms (tối đa 20 lần/giây). Thể lực cũng giới hạn tổng số cú bấm mỗi ngày.

## CrazyGames

SDK v3. Lưu qua `SDK.data`. Quảng cáo giữa game: sau khi ngủ, mỗi 3 ngày một lần, và khi lên đời. Quảng cáo thưởng: nước tăng lực. Tắt tiếng khi có quảng cáo. Không có SDK thì game vẫn chạy, không có quảng cáo.

Ngôn ngữ: người chơi lần đầu luôn thấy tiếng Anh (khán giả CrazyGames phần lớn nói tiếng Anh), đổi sang tiếng Việt bằng nút "VI". Lựa chọn được lưu; bản lưu cũ giữ ngôn ngữ đang dùng.

## Mục tiêu cân bằng

Đo bằng `python tools/sim.py`. Kết quả gần nhất:

| Hạng | Người mới (3 lần bấm/giây, bỏ bữa, không nghỉ) | Người quen (4 lần bấm/giây, ăn cơm gà, nghỉ khi Mỏi) |
|---|---|---|
| 2 | ngày 2, phút 2 | ngày 2, phút 2 |
| 3 | ngày 3, phút 6 | ngày 3, phút 5 |
| 4 | ngày 4, phút 9 | ngày 4, phút 8 |
| 5 | ngày 14, phút 42 | ngày 11, phút 33 |
| 6 | ngày 32, 1h45 | ngày 25, 1h28 |

Sim giả định bấm mọi khách, kể cả ăn mọi chiếc bánh; khách xoay vòng đúng tỉ lệ. So với khi chưa có khách: gần như không đổi (hạng 6 chậm 5–6 phút, sớm hơn 1–2 ngày), vì quà thể lực làm ngày dài hơn (người mới 3 → 3,4 phút, người quen 3,3 → 3,7 phút) còn bánh làm tăng cân. Phần calo từ cú bấm (người mới, hạng 1 → 5): 76%, 55%, 48%, 39%, 37%.

- Một ngày dài ít nhất 2 phút chơi ở mọi hạng.
- Hạng 2 trong khoảng 2 phút, hạng 4 dưới 10 phút; hạng 5 → 6 khoảng 1 giờ (trước là 1,5 giờ, đoạn dễ bỏ cuộc nhất); hạng 6 sau khoảng 1,5 giờ.
- Cú bấm chiếm 40–55% calo từ hạng 2 trở đi.
- Người nghỉ hợp lý lên hạng sớm ngày hơn người không nghỉ.
- Người tập đều không bị cân nặng chặn quá 1–3 ngày.
