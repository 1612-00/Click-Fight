# Kế hoạch: hộp thoại và thông báo ra dáng game

Trạng thái: **đã vào game** (bước 1–6, theo cả ba phương án đề xuất ở mục "Cần chủ dự án quyết định"). Chưa làm: 3 biểu cảm riêng của Bắp (đang dùng `pet-dog`), số calo vắng mặt đếm lên, cân trên thẻ nhân viên nhấp xanh/đỏ, cờ 🇻🇳/🇬🇧 (Windows không vẽ cờ emoji), thanh âm lượng kiểu vạch máy tập, nút xoá có vòng tiến độ (đang dùng thanh đỏ chạy ngang). Bảng dưới là hiện trạng **trước khi** làm.

## Hiện trạng

| Thành phần | Dùng ở đâu | Trông như thế nào | Vấn đề |
|---|---|---|---|
| `#modal` qua `ask(text, yes)` | Về nhà khi còn thể lực (`qHome`), Về nhà nghỉ (`qRest`), Lên đời (`qAsc`), bắt đầu / bỏ thử thách (`qCh`, `qQuit`), Xoá tiến trình (`qReset`) | Thẻ be nhỏ giữa màn, một dòng chữ, hai nút "Huỷ / Đồng ý", nền mờ xám | Giống hộp `confirm()` của trang web. Việc nhỏ (về nhà) và việc rất lớn (xoá cả tiến trình) trông y như nhau. Không nói rõ mất gì, được gì. |
| `#setBox` (⚙️) | Âm lượng nhạc, hiệu ứng, ngôn ngữ | Thẻ "Settings" kiểu biểu mẫu web | Đúng chức năng nhưng như trang cài đặt của website. |
| `#toast` qua `toast()` / `toastLater()` | Khoảng 20 chỗ: lên hạng, mở tính năng, thắng/thua, nhiệm vụ, thành tựu, khách ghé, sự kiện, bữa tối, kỹ năng, calo lúc vắng mặt, báo cáo buổi sáng | Một khung be giống nhau giữa màn, tự tắt sau 2,2 giây (6 giây nếu mở tính năng) | Tin lớn (LỘT XÁC, mở tính năng) và tin vặt (nhiệm vụ) trông như nhau; tin dài (báo cáo sáng, mở tính năng) tắt trước khi đọc xong; che giữa màn khi đang bấm. |
| `#guide` (Bắp dẫn chuyện) | Hướng dẫn | Hộp thoại dưới màn, bảng tên, chó con | **Đã ra dáng game**, dùng làm mẫu cho phần còn lại. |

## Hướng thiết kế

Nguyên tắc: thông báo nằm **trong thế giới game** (trên bàn, trên cửa, do Bắp nói) hoặc theo **ba tầng rõ ràng** như game di động; không còn khung web giữa màn.

### 1. Một "khung game" dùng chung: `sheet()`

Thay `ask()` bằng một hàm `sheet({icon, title, body, lose, keep, actions, danger})` cho mọi hộp cần người chơi quyết định:

- Khung như **trang sổ tập** (giống bảng bài tập đã có): giấy kem, băng dính ở đầu, viền đậm, tiêu đề trên một tấm biển (cùng kiểu biển trên cửa chuyển cảnh).
- Bên trái là Bắp với biểu cảm theo tình huống (lo lắng khi xoá tiến trình, hào hứng khi lên đời); thiếu ảnh thì dùng `pet-dog` như hướng dẫn.
- Hai cột ngắn có icon: **Mất** (calo, cấp bài tập…) / **Giữ** (Sao, bạn tập, trận thắng…), lấy từ chữ đã có trong hướng dẫn Lên đời.
- Nút to, dày, nhún khi bấm (cùng kiểu nút "Đến phòng tập"); nút chính màu xanh, nút huỷ màu giấy.
- Vào: khung rơi xuống và nảy nhẹ, tiếng "bộp" giấy (`noise`), nền tối dần có viền tối góc (vignette) thay cho nền xám mờ phẳng.
- Bàn phím: Enter = nút chính, Esc = huỷ, Tab chỉ đi trong khung; trả focus về nút đã mở khung.
- **Xoá tiến trình**: nút đỏ phải **giữ 1,5 giây** (vòng tiến độ chạy quanh nút) thay vì bấm một lần; khó bấm nhầm mà không cần hỏi hai lần.

### 2. Việc nhỏ không cần hộp: bấm hai lần

"Về nhà" khi còn thể lực và "Về nhà nghỉ" không mở hộp nữa. Bấm lần đầu: nút đổi chữ thành "Chắc chưa? Bấm lần nữa" (lắc nhẹ, viền vàng) trong 3 giây; bấm lần nữa mới đi. Không che màn, không ngắt nhịp chơi.

### 3. Thông báo theo ba tầng

| Tầng | Dùng cho | Trông như thế nào | Tắt |
|---|---|---|---|
| **Nhỏ** | Nhiệm vụ xong, thành tựu, mua mốc x2, kết quả khách ghé, sự kiện, bữa tối, kỹ năng | Dải nhỏ trượt xuống từ dưới HUD (như huy hiệu thành tựu của game): icon trong ô tròn + một dòng chữ; nhiều tin thì xếp chồng tối đa 3, tin cũ trôi lên | Tự tắt 2,5 giây, không chặn bấm |
| **Lớn** | Lên hạng, thắng/thua trận, lên đời, hoàn thành thử thách | Băng rôn ngang màn có tia sáng (dùng `.rays` sẵn có), chữ to "LỘT XÁC!", hạng mới và hệ số calo | Tự tắt 2,5 giây; chạm để tắt sớm |
| **Mở khoá** | Lần đầu lên hạng có tính năng mới | **Thẻ tính năng** ngay sau băng rôn: icon tính năng (icon tab đã có), tên và một câu; Bắp giới thiệu | Chờ người chơi bấm "Tuyệt!" (đọc kịp, thay cho 6 giây hiện nay) |

### 4. Đưa thông báo vào thế giới game

- **Báo cáo buổi sáng** (cân nặng hôm qua, mệt mỏi, tổng kết tuần, cân kiểm tra): viết lên **tờ giấy ghi chú trên bàn văn phòng** (`#postIt` đã có) trong buổi sáng đó, thay cho toast 4,5 giây; cân nặng trên thẻ nhân viên nhấp xanh/đỏ.
- **Calo lúc vắng mặt**: thẻ "Lúc bạn vắng mặt" kiểu hoá đơn có số calo đếm lên và nút "Nhận" (tiếng xu). Về sau có thể thêm nút "x2 bằng quảng cáo" của CrazyGames.

### 5. Cài đặt thành menu tạm dừng

- Khung `sheet()` với tiêu đề "Tạm nghỉ" / "Paused"; nhạc nhỏ lại (`muffle`) như khi mở hướng dẫn.
- Âm lượng: giữ thanh 10 nấc nhưng là các vạch to như vạch đo của máy tập, nút −/+ dày.
- Ngôn ngữ: hai nút có cờ nhỏ 🇻🇳 / 🇬🇧.
- Với CrazyGames: gọi `gameplayStop()` khi mở, `gameplayStart()` khi đóng (đúng luật SDK, chịu được `CG === null`).
- Chuyển nút "Xoá toàn bộ tiến trình" từ tab Lên đời vào đây (cuối menu, chữ nhỏ), dùng nút giữ 1,5 giây.

## Ảnh

Không bắt buộc: thiếu ảnh thì dùng `pet-dog` và khung CSS. Nên có 3 biểu cảm của Bắp cho hộp quyết định và thẻ mở khoá: prompt ở `assets/PROMPTS.md` **Nhóm 17** (`pet-bap-worry`, `pet-bap-cheer`, `pet-bap-wave`).

## Các bước

| Bước | Nội dung |
|---|---|
| 1 | `sheet()` + nền vignette + phím; chuyển Lên đời, thử thách, Xoá tiến trình sang (Xoá: nút giữ 1,5 giây). Bỏ `#modal`. |
| 2 | Bấm hai lần cho Về nhà / Về nhà nghỉ. |
| 3 | Ba tầng thông báo: thay `toast()` bằng `note()` (nhỏ), `banner()` (lớn), `unlockCard()` (mở khoá); đổi ~20 chỗ gọi. |
| 4 | Báo cáo buổi sáng lên tờ ghi chú; thẻ calo lúc vắng mặt. |
| 5 | Cài đặt thành menu tạm dừng, chuyển nút Xoá tiến trình vào. |
| 6 | Âm thanh mở/đóng, giảm chuyển động, điện thoại 375×812, hai ngôn ngữ; cập nhật GAME_DESIGN, TEST_PLAN (nhóm A cho Xoá tiến trình vì chạm tới bản lưu), CRAZYGAMES. |

Bước 1–3 thay đổi cảm giác nhiều nhất.

## Cần chủ dự án quyết định

1. **Về nhà**: bấm hai lần (đề xuất) hay vẫn giữ hộp hỏi nhưng làm đẹp?
2. **Thẻ mở khoá**: chờ người chơi bấm (đề xuất, vì có chữ cần đọc) hay tự tắt?
3. **Nút Xoá tiến trình**: chuyển vào menu cài đặt (đề xuất) hay giữ ở tab Lên đời?

## Không làm

- Không đổi luật, con số, phần thưởng hay thời điểm lưu.
- Không dùng `confirm()` / `alert()` (bị chặn trong iframe cổng game).
- Không thêm thư viện.
