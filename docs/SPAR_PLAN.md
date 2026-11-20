# Kế hoạch: Võ đài hằng ngày

Trạng thái: **đã vào game** (2026-11-20): `SPAR`, `drawSpar()`, `startDuel(i, true)` trong `index.html`; Võ đài có trong `tools/sim.py` (tham số `spar`). Sim có chuỗi độ khó: hạng 6 gần như không đổi, hạng 9 (nghỉ khi Mỏi) 21h35 → 20h43 (−4%); xem bảng mục tiêu cân bằng trong GAME_DESIGN. Chưa thử tay chuỗi 8 (120%) trên điện thoại thật.

## Vấn đề

Đối thủ thứ i cần 300 × 2,4^i calo trong 15 giây: mỗi người khó gấp 2,4 lần người trước, nhanh hơn sức người chơi tăng ở cuối game. Theo `tools/sim.py`, người chơi dừng ở **18 trận thắng từ khoảng hạng 6 tới hết game** (hơn 15 giờ chơi). Suốt thời gian đó tab Thi đấu chỉ còn một nút đỏ không thắng nổi: đấu trường, 30 bộ thoại và nhạc trận đấu gần như không được dùng, và nhiệm vụ "Đấu 1 trận" chỉ còn cách đấu thua để hoàn thành.

## Ý tưởng

Mỗi ngày trong game có **một trận tập ở Võ đài** với một đối thủ **đã hạ**. Sức đối thủ tính theo sức hiện tại của người chơi nên trận luôn thắng được nếu bấm đều tay. Thắng thì nhận calo, không tăng số trận thắng và không cộng +3% vĩnh viễn: Võ đài là chỗ luyện tập hằng ngày, không thay cho việc vượt giải.

Dùng lại toàn bộ đấu trường đã có: `arenaOpen()` (VS), `talk()`, `countdown()`, `fight()`, `duelEnd()`, nền theo giải, ảnh và thoại của đối thủ.

## Luật

- **Mở**: cùng lúc với Thi đấu (hạng 4) và đã thắng ít nhất 1 đối thủ.
- **Đối thủ hôm nay**: đối thủ đã hạ thứ `ngày trong game % số trận thắng`, nên đổi mỗi ngày và xoay vòng qua mọi người đã hạ.
- **Chi phí**: 40 thể lực như thách đấu (20 với kỹ năng Đấu tiết kiệm), Chủ nhật miễn phí.
- **Mục tiêu**: `15 × (calo/giây + 3 × calo/bấm) × độ khó` calo trong 15 giây. **Độ khó tăng dần theo chuỗi ngày thắng liên tiếp**: 0,8 + 0,05 × chuỗi, tối đa 1,2 (chuỗi 0: 80% sức của người bấm đều 3 lần/giây; chuỗi 8 trở lên: 120%, tức phải bấm khoảng 3,6 lần/giây). Một ngày tập mà không thắng Võ đài (thua, hoặc không đấu) thì chuỗi về 0. Thưởng tính theo mục tiêu nên chuỗi càng dài thưởng càng lớn. Tính lúc bắt đầu trận (bữa tối, sự kiện, PT bấm x5… đều có tác dụng).
- **Thưởng khi thắng**: mục tiêu × 3 (cùng hệ số với đối thủ thật), Chủ nhật x2. Không đổi `s.wins`, không +3%.
- **Thua**: không mất gì thêm ngoài thể lực; đấu lại được trong ngày (lại tốn thể lực).
- **Mỗi ngày một lần thắng**: thắng rồi thì thẻ Võ đài ghi "✓ Hẹn mai" tới sáng hôm sau.
- **Nhiệm vụ**: trận Võ đài tính vào nhiệm vụ "Đấu 1 trận" (`bump('duel')`).
- **Thoại**: đối thủ nói câu gặp lại (`rv[i][2]`), vào trận; thắng thì câu thua cuộc (`rv[i][3]`), thua thì câu chế giễu (`rv[i][4]`). Không lặp thoại lần đầu.
- **Thử thách**: chạy bình thường; luật thử thách tác động qua calo/giây và calo/bấm nên mục tiêu tự điều chỉnh theo.

## Cân bằng (đo bằng bản sim có Võ đài, mỗi ngày tập đủ thắng một trận)

| Thưởng | Hạng 6 | Hạng 8 | Hạng 9 (nghỉ khi Mỏi) |
|---|---|---|---|
| Không có Võ đài (hiện tại) | ngày 25, 1h16 | ngày 84, 5h14 | ngày 309, 21h35 |
| Mục tiêu × 2 | ngày 25, 1h18 | ngày 82, 5h16 | ngày 297, 21h21 |
| **Mục tiêu × 3 (đề xuất)** | ngày 25, 1h18 | ngày 80, 5h10 | ngày 290, 20h51 (−3%) |
| Mục tiêu × 5 | ngày 24, 1h12 | ngày 77, 4h56 | ngày 277, 19h52 (−8%) |

Với x3, hạng 2–6 gần như không đổi; cuối game nhanh hơn khoảng 3%. Mục đích là cho người chơi việc đáng làm mỗi ngày ở tab Thi đấu, không phải rút ngắn game. Khi làm thật, thêm Võ đài vào `tools/sim.py` (như bản thử) và cập nhật bảng mục tiêu cân bằng trong GAME_DESIGN.

## Quảng cáo thưởng (gộp đề xuất C)

- Thắng Võ đài: nút "📺 x2 thưởng" cạnh "Về phòng tập", xem hết thì cộng thêm đúng phần thưởng một lần nữa.
- Không thêm quảng cáo cho trận với đối thủ thật (giữ cảm giác vượt giải là thành tích thật).
- Không có SDK thì không có nút.

## Giao diện

- **Tab Thi đấu**: thẻ đầu danh sách, trên giải 1: "🥊 Võ đài hôm nay", ảnh đối thủ, dòng "Mục tiêu 🔥 X / 15s", dòng "+Y 🔥", nút "Tập đấu ⚡40" (Chủ nhật không ghi ⚡). Thắng rồi: nút "✓ Hẹn mai", mờ. Chưa hạ ai: thẻ ẩn.
- **Đấu trường**: biển tên giải thay bằng "🥊 Võ đài hằng ngày"; còn lại như trận thường. Kết quả dùng băng rôn đã có ("THẮNG!" kèm "+Y 🔥", không ghi +3%).
- **Hướng dẫn**: mục `spar` cho Bắp (một câu), gọi `coach('spar')` lần đầu thẻ Võ đài hiện.

## Bản lưu

Thêm hai trường vào `fresh()` và `load()`: `spar` = ngày trong game của lần thắng Võ đài gần nhất (số nguyên ≥ 0, mặc định 0); `sparN` = chuỗi ngày thắng liên tiếp (số nguyên 0–8, mặc định 0). Bản lưu cũ không có thì Võ đài mở ngay, chuỗi 0. Chạy lại nhóm A.

## Các bước

| Bước | Nội dung |
|---|---|
| 1 | Trường `spar`; hàm `sparFoe()`, `sparTarget()`; `duel` mang cờ `spar` để `duelEnd()` phát thưởng đúng loại |
| 2 | Thẻ Võ đài trong `drawRivals()`; `startDuel(i, spar)` dùng câu gặp lại và biển "Võ đài hằng ngày" |
| 3 | Nút "📺 x2 thưởng" sau khi thắng (chỉ khi có SDK) |
| 4 | Chữ vi/en, mục hướng dẫn `spar`; thêm Võ đài vào `tools/sim.py` |
| 5 | Kiểm thử: nhóm A, nhóm J, các bài mới bên dưới, 375×812, hai ngôn ngữ |
| 6 | Cập nhật GAME_DESIGN (mục Thách đấu và bảng cân bằng), TEST_PLAN, CRAZYGAMES, BACKLOG |

## Bài kiểm thử dự kiến

| Mã | Bước | Kết quả mong muốn |
|---|---|---|
| J14 | Hạng 4, chưa thắng ai. Thắng Tom. | Trước: không có thẻ Võ đài. Sau: thẻ "🥊 Võ đài hôm nay" với Tom, Bắp giới thiệu một lần. |
| J15 | Bấm "Tập đấu", thắng. | Trừ 40 thể lực; đấu trường ghi "Võ đài hằng ngày", câu gặp lại; thắng: thưởng đúng mục tiêu × 3, số trận thắng và hệ số calo không đổi, nhiệm vụ "Đấu 1 trận" xong. Thẻ thành "✓ Hẹn mai". |
| J16 | Thua một trận Võ đài, rồi đấu lại. | Thua: câu chế giễu, không thưởng. Đấu lại được, tốn thể lực lần nữa. |
| J18 | Thắng Võ đài 3 ngày liền, ngày thứ 4 không đấu, ngày thứ 5 đấu. | Mục tiêu và thưởng tăng mỗi ngày thắng (x0,8 → x0,85 → x0,9); ngày thứ 5 về lại x0,8. |
| J17 | Ngủ sang ngày mới (có ≥ 2 trận thắng). | Võ đài mở lại, đối thủ đổi theo ngày. Chủ nhật: không tốn thể lực, thưởng x2. |
| P10 | Trên CrazyGames: thắng Võ đài, bấm "📺 x2 thưởng"; lần khác bỏ ngang. | Xem hết: cộng thêm đúng phần thưởng. Bỏ ngang: chỉ có thưởng gốc. Trận với đối thủ thật không có nút này. |

## Đã chốt (2026-11-20)

1. **Hệ số thưởng**: x3 như đối thủ thật.
2. **Số lần mỗi ngày**: một lần thắng mỗi ngày trong game.
3. **Độ khó**: tăng dần theo số ngày thắng liên tiếp (công thức ở mục Luật). Bảng cân bằng trên đo với độ khó cố định 80%; khi làm phải đo lại bằng sim có chuỗi, và thử tay xem chuỗi 8 (120%) có quá khó trên điện thoại không.

## Không làm

- Không có đối thủ mới hay ảnh mới.
- Không cho Võ đài tăng số trận thắng hay +3% vĩnh viễn.
- Không đổi công thức đối thủ thật (300 × 2,4^i); nếu sau này thấy người chơi bỏ game vì kẹt ở đối thủ 19, đó là việc cân bằng riêng.
