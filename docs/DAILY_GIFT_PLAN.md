# Kế hoạch: Quà mỗi ngày thật

Trạng thái: **đã vào game** (2026-11-20): `gift()` trong `index.html`, bài test nhóm Q và P9, ca Playwright "Quà mỗi ngày". Chưa làm: ảnh `ui-gift` riêng (đang dùng emoji 🎁).

## Vấn đề

Mọi thứ "mỗi ngày" trong game (nhiệm vụ, lịch tuần, khách ghé, sự kiện) tính theo **ngày trong game**, khoảng 2–3 phút một ngày. Không có gì gắn với ngày thật, nên người chơi không có lý do mở lại game vào hôm sau. CrazyGames xét Full Launch dựa nhiều vào tỉ lệ quay lại sau 1 ngày và sau 7 ngày.

## Ý tưởng

Mỗi ngày thật (theo lịch máy người chơi) mở game thì nhận một phần quà, đi theo **vòng 7 ngày**: quà tăng dần, ngày thứ 7 có Sao. Hết vòng thì quay lại ngày 1.

Nhận quà qua **nút 🎁 cố định trên HUD** (cạnh ❓, hiện từ ngày 2 trong game), có chấm đỏ khi quà hôm nay đang chờ; quà không tự bật lên (chủ dự án chốt sau khi chơi thử, 2026-11-20). Bấm nút thì mở **thẻ quyết định đã có** (`ask()`, kiểu trang sổ, có Bắp): tiêu đề "🎁 Quà ngày 3/7", một dải 7 ô (đã nhận ✅, hôm nay 🎁, chưa tới ⬜, ô thứ 7 ⭐), dòng mô tả quà và nút nhận. Đã nhận rồi thì thẻ chỉ cho xem vòng quà và quà ngày mai.

## Phần quà

`Q` = thưởng một nhiệm vụ ngày hiện tại (`qReward()` = max(500, 300 × (calo/giây + 3 × calo/bấm))), khoảng thu nhập của 2 ngày trong game. Dùng `Q` để quà luôn có ý nghĩa ở mọi giai đoạn mà không phá cân bằng.

| Ngày | Quà | Ghi chú |
|---|---|---|
| 1 | 🔥 Q × 0,25 | |
| 2 | 🔥 Q × 0,5 | |
| 3 | 🥤 Nước tăng lực miễn phí: +50% thể lực tối đa ngay | Như quảng cáo thưởng, nhưng không cần xem; có tác dụng cả khi không có SDK |
| 4 | 🔥 Q × 0,75 | |
| 5 | 🍳 Bữa sáng đủ chất: calo +25% tới hết ngày trong game | Ghi vào `s.buff.cal` như sự kiện văn phòng, tự hết khi sang ngày |
| 6 | 🔥 Q × 1 | |
| 7 | ⭐ +1 Sao và 🔥 Q × 1 | Sao vừa là +10% calo vĩnh viễn vừa là tiền học kỹ năng |

Cả vòng cho khoảng 3,5 Q calo, tức khoảng 7 ngày trong game của thu nhập: người chơi 15 phút mỗi ngày (khoảng 40 ngày trong game một tuần) được thêm khoảng 15–20%; người chơi ít hơn được lợi nhiều hơn, đúng nhóm cần kéo lại. Một Sao mỗi tuần nhỏ so với khoảng 21 Sao của đời đầu tới hạng 6.

**Quảng cáo thưởng** (CrazyGames): ở ngày có calo, nút chính là "📺 Nhân đôi" (cộng thêm phần calo đó một lần nữa), nút phụ là "Nhận". Không nhân đôi Sao, nước tăng lực hay bữa sáng. Không có SDK thì chỉ một nút "Nhận". Quà luôn được cộng **ngay khi thẻ hiện** (như thẻ vắng mặt) để đóng game giữa chừng không mất; quảng cáo chỉ cộng thêm.

## Luật

- **Chấm đỏ**: `giftDue()` được xét mỗi tick (100 ms) nên để tab mở qua nửa đêm vẫn thấy ngay. Lần đầu nút có chấm đỏ ở văn phòng, Bắp chỉ nút (`coach('gift')`).
- **Ngày thật**: chuỗi `YYYY-MM-DD` theo giờ máy người chơi (`new Date()` giờ địa phương).
- **Người mới**: chỉ bắt đầu khi đã xong phần dẫn chuyện đầu và tới ngày 2 trong game (vừa ngủ dậy lần đầu), để không chen vào hướng dẫn. Thẻ ngày 1 nói thêm "Mai quay lại nhận quà ngày 2!".
- **Bỏ lỡ ngày**: không mất chuỗi, chỉ không tiến; quà là phần thưởng cho việc quay lại chứ không phạt người bận.
- **Chỉnh đồng hồ**: ngày hôm nay nhỏ hơn ngày đã nhận (đồng hồ bị lùi) thì không có quà và không đổi gì. Chỉnh đồng hồ tới trước để nhận nhiều lần thì cho qua: game chơi một mình, phần quà nhỏ.
- **Nhiều máy**: ngày đã nhận nằm trong bản lưu, đồng bộ qua Data Module, nên không nhận hai lần trên hai máy.

## Bản lưu

Thêm hai trường vào `fresh()` và `load()`:

| Trường | Kiểu | Mặc định | `load()` chỉ nhận khi |
|---|---|---|---|
| `gd` | chuỗi ngày đã nhận gần nhất | `''` | khớp `/^\d{4}-\d{2}-\d{2}$/` |
| `gn` | số ngày đã nhận trong vòng (0–6) | `0` | số nguyên 0–6 |

Bản lưu cũ không có hai trường này: lần mở đầu sau khi cập nhật nhận quà ngày 1. Ghi `save()` ngay sau khi cộng quà. Chạm tới bản lưu nên phải chạy lại nhóm A.

## Chữ (vi / en)

- Tiêu đề: "🎁 Quà ngày {n}/7" / "🎁 Day {n}/7 gift"
- Mô tả từng quà (7 dòng) / bản tiếng Anh tương ứng.
- "Mai quay lại nhận quà ngày {n}!" / "Come back tomorrow for day {n}!"
- Nút: dùng lại `take` ("Nhận" / "Collect") và `awayX2` ("📺 Nhân đôi" / "📺 Double it").
- Mục hướng dẫn `gift` cho Bắp (một câu), gọi `coach('gift')` lần đầu thẻ hiện.

## Các bước

| Bước | Nội dung |
|---|---|
| 1 | Trường `gd`, `gn` trong `fresh()`/`load()`; hàm `today()` và `giftDue()` |
| 2 | `gift()`: cộng quà, lưu, mở thẻ (dải 7 ô, nút x2); gọi lúc mở game, `arrive()`, `visibilitychange` |
| 3 | Chữ vi/en, mục hướng dẫn, icon 🎁 trong `ICO` nếu muốn ảnh riêng (`ui-gift`, không bắt buộc) |
| 4 | Kiểm thử: nhóm A, các bài mới bên dưới, 375×812, hai ngôn ngữ; thêm ca Playwright giả lập ngày (`Date` giả) |
| 5 | Cập nhật GAME_DESIGN (mục mới), TEST_PLAN, CRAZYGAMES (một dòng tính năng), BACKLOG |

## Bài kiểm thử dự kiến

| Mã | Bước | Kết quả mong muốn |
|---|---|---|
| Q1 | Ván mới, chơi qua dẫn chuyện và ngủ sang ngày 2. | Thẻ "Quà ngày 1/7", Q × 0,25 calo đã cộng, dòng "Mai quay lại…". Tải lại cùng ngày: không có thẻ. |
| Q2 | Đặt `s.gd` thành hôm qua, tải lại. Lặp tới ngày 7. | Mỗi lần đúng quà theo bảng; ngày 7 Sao +1; lần sau quay về ngày 1. |
| Q3 | Đặt `s.gd` thành 3 ngày trước, tải lại. | Tiếp tục đúng ô kế, không mất chuỗi. |
| Q4 | Đặt `s.gd` thành ngày mai (đồng hồ bị lùi), tải lại. | Không có thẻ, `gd`/`gn` không đổi. |
| Q5 | Để tab mở qua nửa đêm (giả lập), quay lại tab. | Thẻ hiện khi quay lại, không cần tải lại. |
| Q6 | Có thẻ vắng mặt và quà cùng lúc; có hướng dẫn đang mở. | Hướng dẫn trước, rồi thẻ vắng mặt, rồi thẻ quà; không chồng lên nhau. |
| P9 | Trên CrazyGames: bấm "📺 Nhân đôi" ở ngày có calo; lần khác bỏ ngang. | Xem hết: cộng thêm đúng phần calo. Bỏ ngang: giữ phần đã cộng. Ngày 3, 5, 7 không có nút nhân đôi cho phần không phải calo. |

## Đã chốt (2026-11-20)

1. **Bỏ lỡ ngày**: không mất chuỗi, chỉ không tiến.
2. **Quà ngày 7**: 1 Sao (kèm Q × 1 calo).
3. **Người mới**: bắt đầu từ ngày 2 trong game.

## Không làm

- Không thông báo đẩy hay nhắc ngoài game (web không làm được mà không xin quyền).
- Không bắt xem quảng cáo để nhận quà.
- Không chống gian lận đồng hồ bằng máy chủ (game không có máy chủ).
