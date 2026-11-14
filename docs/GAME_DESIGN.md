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

1. **Văn phòng**: mở game luôn ở đây. Chỉ có câu nói ngẫu nhiên, ngày/thứ, lịch tuần và các thông số. Hai nút: "Đến phòng tập", "Về nhà nghỉ" (có hộp xác nhận, vì nghỉ là bỏ tập).
2. **Phòng tập**: bấm nhân vật để tập (tốn thể lực), mua bài tập, thách đấu, nhiệm vụ. Nút "Về nhà" có hộp xác nhận.
3. **Nhà**: chọn một bữa tối, xem/gọi bạn tập, bấm "Đi ngủ" sang ngày mới.

Calo/giây chạy ở mọi màn, không tốn thể lực. Tắt game vẫn cộng calo, tối đa 8 giờ. Vắng hơn 24 giờ thật tính là 1 ngày nghỉ.

## Mở tính năng theo hạng

Tính theo hạng cao nhất từng đạt (`unl()`), nên lên đời không bị khoá lại.

| Hạng | Mở |
|---|---|
| 1 | Thể lực, bài tập, thách đấu, nhiệm vụ, bạn tập |
| 2 | Bữa tối ở nhà |
| 3 | Mệt mỏi, lịch tuần và mục tiêu tuần |
| 4 | Cân nặng bắt đầu chặn lên hạng |

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

Calo mỗi cú bấm = (1 + tổng calo/bấm + 5% calo/giây gốc) × các hệ số.

## Hạng

Lên hạng khi đủ cấp tối thiểu của **mọi** bài tập và cân nặng không quá ngưỡng. Đã lên thì không tụt.

| Hạng | Tên | Hệ số calo | Cấp tối thiểu (Tay, Vai, Ngực, Bụng, Mắt, Chân, Lưng, Cardio) | Cân tối đa |
|---|---|---|---|---|
| 1 | Dân văn phòng suy nhược | x1 | — | — |
| 2 | Tập tành cho vui | x1,25 | 10, 8, 5 | không chặn |
| 3 | Gymer nghiệp dư | x1,5 | 25, 20, 15, 10, 5 | không chặn |
| 4 | Body săn chắc | x2 | 40, 35, 30, 22, 15, 10 | 82 kg |
| 5 | Sáu múi lấp ló | x2,5 | 55, 48, 42, 35, 28, 25, 15 | 77 kg |
| 6 | Thần gym công sở | x3 | 70, 60, 55, 48, 40, 40, 32, 20 | 73 kg |

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
- **Lên đời**: nhận Sao = ⌊∛(calo kiếm được trong đời này / 1 triệu)⌋, mỗi Sao +10% calo. Chỉ xoá calo, cấp bài tập và hạng; ngày, cân nặng, mệt mỏi, bạn tập, trận thắng giữ nguyên.

## Chống auto-click

Cú bấm nhân vật phải là cú bấm thật và cách cú trước ít nhất 50 ms (tối đa 20 lần/giây). Thể lực cũng giới hạn tổng số cú bấm mỗi ngày.

## CrazyGames

SDK v3. Lưu qua `SDK.data`. Quảng cáo giữa game: sau khi ngủ, mỗi 3 ngày một lần, và khi lên đời. Quảng cáo thưởng: nước tăng lực. Tắt tiếng khi có quảng cáo. Không có SDK thì game vẫn chạy, không có quảng cáo.

## Mục tiêu cân bằng

Đo bằng `python tools/sim.py`. Kết quả gần nhất (người chơi 4 lần bấm/giây, ăn cơm gà): hạng 6 ở ngày 47–60, khoảng 2h23 chơi, 2,5–3 phút mỗi ngày. Người mới (3 lần bấm/giây): hạng 2 phút thứ 4, hạng 3 phút 16, hạng 4 phút 32.

- Một ngày dài ít nhất 2 phút chơi ở mọi hạng.
- Hạng 2 trong 5 phút đầu; lên hạng 6 quanh ngày 50–60, khoảng 2,5 giờ.
- Người nghỉ hợp lý lên hạng sớm ngày hơn người không nghỉ.
- Người tập đều không bị cân nặng chặn quá 1–3 ngày.
