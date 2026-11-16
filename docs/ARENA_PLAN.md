# Kế hoạch: đấu trường riêng và lời thoại đối thủ

Trạng thái: **đã vào game**, đủ 4 nền đấu trường. Trận đấu là đấu đòn: xem mục Thách đấu trong GAME_DESIGN.

## Vấn đề hiện tại

- Thi đấu diễn ra ngay trong phòng tập. Mỗi cú bấm trong trận **vừa đẩy thanh đấu vừa cộng calo** như bấm thường, nên trận đấu giống "phòng tập có thêm thanh", không có cảm giác bước vào một trận.
- Đối thủ chỉ có tên và ảnh, không có tính cách. 10 phản diện mới (giải 5–6) chưa có câu chuyện nào giải thích vì sao họ là phản diện.

## Ý tưởng: Đấu trường

Thi đấu chuyển sang một **màn riêng** (`s.scene` thêm `arena`), giống màn văn phòng, phòng tập, nhà.

### Luồng một trận

1. **Phòng tập → bấm "Thách đấu"** (vẫn tốn 40 thể lực, Chủ nhật miễn phí).
2. **Màn chờ "Đến đấu trường"** (như màn chờ đi tập, 0,8–2 giây, chạm để bỏ qua).
3. **Màn VS** (1,2 giây): nền đấu trường tối lại, ảnh nhân vật trượt vào từ trái, ảnh đối thủ trượt vào từ phải, chữ "VS" đập xuống giữa, dưới là tên đối thủ và tên giải. Có tiếng "đùng".
4. **Thoại** (kiểu truyện tranh, visual novel):
   - Khung thoại ở dưới màn, có ô tên người nói. Người đang nói sáng lên và nhích về phía trước, người kia mờ đi.
   - Chữ chạy từng ký tự (khoảng 40 ký tự/giây). Chạm một lần thì hiện hết câu, chạm lần nữa sang câu kế.
   - **Lần đầu gặp**: xem hết thoại (đối thủ 1–3 câu tuỳ giải, rồi nhân vật đáp 1 câu). Không có nút bỏ qua, vì câu ngắn và chạm là qua nhanh.
   - **Gặp lại** (lần trước thua, đấu lại): đối thủ chỉ nói **1 câu "gặp lại"**, rồi vào trận luôn.
5. **Đếm ngược** 3 · 2 · 1 · ĐẤU! (khoảng 2 giây; trong lúc đếm, bấm không tính).
6. **15 giây đấu**:
   - Cú bấm **chỉ đẩy thanh đấu, không cộng calo** (sửa đúng điều chủ dự án thấy).
   - Calo/giây vẫn chạy ngầm và vẫn tính vào thanh đấu như hiện nay.
   - Giữ hai thanh đua và đòn đánh minh hoạ hiện có, thêm rung màn hình nhẹ khi đối thủ ra đòn.
7. **Kết quả**:
   - Thắng: đối thủ nói câu thua cuộc, nhận thưởng như cũ (calo, +3% vĩnh viễn). Nút "Về phòng tập".
   - Thua: đối thủ nói câu chế giễu. Nút "Đấu lại ⚡40" (nếu đủ thể lực) và "Về phòng tập".
8. Về phòng tập thì có màn chờ ngắn như cũ.

### Đấu trường theo giải (4 ảnh nền mới)

| Giải | Đấu trường | Không khí |
|---|---|---|
| 1–2. Phòng ban, Công ty | Phòng họp lớn sau giờ làm: bàn họp kê sát tường, máy chiếu chiếu chữ VS, đèn trần chập chờn | Hài, công sở |
| 3–4. Phòng gym, Giải quốc gia | Sàn đấu thể hình: đèn sân khấu, khán đài tối, băng rôn | Thể thao, hồi hộp |
| 5. Thế giới ngầm | Bãi đỗ xe ngầm bỏ hoang, đèn neon tím, ghế lười và máy bán trà sữa chất đống | Bí ẩn, nguy hiểm |
| 6. Trùm Trái Đất | Hang dung nham dưới lòng đất, tinh thể phát sáng, một ngai đá ở xa | Trận cuối, hoành tráng |

Ảnh nền trùng phong cách các nền đã có (`bg1–3`). Prompt sẽ thêm vào `assets/PROMPTS.md` sau khi duyệt.

### Chi tiết kỹ thuật (để ước lượng)

- Lưu `s.met` (đối thủ đã gặp) để biết lần đầu hay gặp lại. Chỉ gặp lại sau khi thua, vì đối thủ đã hạ thì không đấu lại được.
- Thoại nằm trong `T.vi` / `T.en` như mọi chữ khác. Nhân vật chính là nam hay nữ đều dùng chung một bộ lời; chỗ xưng hô có giới tính viết `{anh|chị}`, game tự chọn theo nhân vật (bản tiếng Anh dùng "you" nên không cần).
- Ở đấu trường không có khách ghé, không có Rep hoàn hảo, không mua bài tập (ẩn bảng bên phải hoặc chỉ hiện thông tin đối thủ).
- Ảnh hưởng cân bằng: cú bấm trong 15 giây đấu không còn ra calo. Mất khoảng 60 cú bấm mỗi trận, nhỏ so với một ngày. Sim sẽ bỏ phần calo đó, đo lại trước khi chốt.
- Tuỳ chọn thêm (làm sau): bấm vào đối thủ đã hạ trong tab Thi đấu để **xem lại thoại**.

## Mạch truyện

- **Giải 1–2 (công sở)**: đồng nghiệp hài hước, mỗi người một tật nghề nghiệp. Giám đốc Frank là người đẩy nhân vật "ra ngoài kia thử sức".
- **Giải 3–4 (thể thao)**: người tập thật sự, nghiêm túc hơn, mỗi người một triết lý tập luyện. Huyền thoại Blake là người đầu tiên cảnh báo: có một thế lực đang **ăn mòn sức mạnh con người**.
- **Giải 5–6 (phản diện)**: bí mật dần lộ ra. Thế lực đó **sống nhờ sự lười biếng**: mỗi giờ con người ngồi yên, mỗi lần nói "mai tập", năng lượng chảy về **Hắc Vương Lõi Đất**. Mỗi phản diện là một "cám dỗ" quen thuộc của dân văn phòng: trà sữa, thuốc tăng cơ thần kỳ, tiện nghi, trời mưa, chăn ấm buổi sáng, điện thoại "thêm 5 phút nữa".
- Hắc Vương thua thì để lộ: **giữa các vì sao còn có kẻ lười hơn**, mở đường cho phần ngoài Trái Đất.
- Một vài câu gọi lại nhau cho có chiều sâu: Tom (kế toán) và Omega (siêu máy tính) đều nói bằng xác suất; Frank và Blake là hai "người thầy" đẩy nhân vật lên tầm mới; Mặt Nạ Bạc nhắc tới "chủ nhân dưới lòng đất".

## Lời thoại (bản tiếng Việt)

Đã viết lại cho đời thường: câu ngắn, có "đấy, nhé, à, thôi", xưng hô theo vai (đồng nghiệp lớn tuổi: nhân vật xưng "em/cháu"; côn đồ gọi "mày", trùm gọi "ngươi", nhân vật đáp "tôi"). Bản tiếng Anh nằm cạnh trong `index.html` (`T.en.rv`). Đây là bản chép từ game; sửa thoại thì sửa trong `T.vi.rv` / `T.en.rv`.

Quy ước: **Gặp** là lần đầu (đối thủ nói, rồi **Bạn** đáp). **Gặp lại** là đấu lại sau khi thua. **Thua** là câu đối thủ nói khi bị hạ. **Thắng** là câu đối thủ nói khi người chơi thua. Số câu khi gặp: giải 1–2 một câu, giải 3–4 hai câu, giải 5–6 ba câu.

### Giải 1: Phòng ban

**1. Anh Tom kế toán**
- Gặp: "Anh tính rồi nhé, cửa thắng của cậu là 0,03% thôi."
- Bạn: "Anh bấm máy tính lại đi, em vừa lên cấp tay đấy."
- Gặp lại: "Anh sửa lại bảng tính rồi. Lần này hết đường."
- Thua: "Ơ… chắc anh nhập nhầm ô nào rồi."
- Thắng: "Thấy chưa, số liệu không nói dối."

**2. Chị Lily lễ tân**
- Gặp: "Muốn gặp chị thì phải đặt lịch đấy. Mà thôi, hôm nay chị rảnh."
- Bạn: "Chị ghi giùm em: người thắng hôm nay."
- Gặp lại: "Lại em à? Đợi chị chút, xử lý nhanh thôi."
- Thua: "Rồi rồi, chị nối máy cho người thắng."
- Thắng: "Lần sau nhớ đặt lịch nha em."

**3. Ben thực tập sinh**
- Gặp: "Em xem hết video tập gym trên mạng rồi, {anh|chị} đừng coi thường em nha!"
- Bạn: "Xem thôi chưa đủ đâu em, phải tập nữa."
- Gặp lại: "Em xem thêm ba video nữa rồi! Đấu lại đi {anh|chị}!"
- Thua: "Thôi em đi pha cà phê cho {anh|chị} vậy…"
- Thắng: "Ủa, em thắng thật hả?"

**4. Chú Hank bảo vệ**
- Gặp: "Chú gác cổng ba chục năm, chưa đứa nào lách qua được đâu."
- Bạn: "Hôm nay cho cháu qua một lần thôi chú."
- Gặp lại: "Lại cháu à? Thẻ đâu, trình chú xem."
- Thua: "Thôi được, chú mở cổng. Bọn trẻ bây giờ khỏe ghê."
- Thắng: "Về ngủ sớm đi cháu, mai còn đi làm."

**5. Trưởng phòng Mike**
- Gặp: "Muốn qua mặt anh à? Ở phòng này anh chính là KPI đấy."
- Bạn: "KPI tháng này của em là thắng anh."
- Gặp lại: "Chưa đạt KPI đâu. Làm lại!"
- Thua: "Được, mai họp giao ban anh khen cậu một câu."
- Thắng: "Sáng mai 8 giờ lên phòng anh rút kinh nghiệm."

### Giải 2: Công ty

**6. Sếp phó Doug**
- Gặp: "Anh lên được chức này là nhờ thực lực. Với cả… may mắn một tí."
- Bạn: "Hôm nay hết may rồi anh ơi."
- Gặp lại: "Lại là cậu à? Anh xin sếp cho cậu thêm một cơ hội… để thua đấy."
- Thua: "Chuyện này đừng kể với giám đốc nhé."
- Thắng: "Còn non lắm cậu ạ."

**7. Cô Rosa căng tin**
- Gặp: "Ăn cơm cô nấu bao nhiêu năm, giờ dám thách cô à?"
- Bạn: "Nhờ cơm cô nên cháu mới khỏe thế này đấy ạ."
- Gặp lại: "Đói rồi chứ gì? Đấu xong cô múc thêm bát canh."
- Thua: "Được rồi, mai cô gắp thêm cho cái đùi gà."
- Thắng: "Ăn thêm bát nữa rồi hẵng quay lại!"

**8. Anh Kevin IT**
- Gặp: "Tay anh bấm được 200 phát một phút. Cậu bấm chậm như wifi công ty ấy."
- Bạn: "Anh thử tắt đi bật lại rồi đấu xem."
- Gặp lại: "Anh cài bản vá rồi. Lỗi thua lần trước fix xong."
- Thua: "…Lỗi không xác định. Để anh đi khởi động lại cái đã."
- Thắng: "Ping cậu cao quá."

**9. Chị Tracy nhân sự**
- Gặp: "Hồ sơ em ghi là 'yếu, hay ngủ gật'. Để chị xem có đúng không."
- Bạn: "Chị chuẩn bị sửa hồ sơ đi là vừa."
- Gặp lại: "Chị đánh dấu đỏ hồ sơ em rồi đấy nhé."
- Thua: "Ừ, chị sửa thành 'thể lực tốt' cho."
- Thắng: "Hẹn em ở kỳ đánh giá cuối năm."

**10. Giám đốc Frank**
- Gặp: "Công ty này tôi gây dựng từ hai bàn tay trắng. Muốn đứng trên tất cả thì phải qua được tôi."
- Bạn: "Em không cần ghế của anh. Em chỉ muốn khỏe hơn thôi."
- Gặp lại: "Cậu lì thật. Tôi thích. Nhưng chưa đủ đâu."
- Thua: "Cậu vượt qua cả công ty rồi. Ra ngoài kia mà thử sức đi."
- Thắng: "Có chí đấy. Nhưng thực lực thì chưa."

### Giải 3: Phòng gym

**11. Cody tân binh**
- Gặp: "{Anh|Chị} cũng mới tập à? Hay quá, mình cùng hội rồi!" / "Nhưng lên sàn thì em không nhường đâu nhé!"
- Bạn: "Ok, chơi hết mình."
- Gặp lại: "Hai tuần nay em không bỏ buổi nào đâu! Đấu lại đi!"
- Thua: "{Anh|Chị} lên trình nhanh thật, chỉ em với!"
- Thắng: "Trời, em thắng rồi!"

**12. HLV Tara**
- Gặp: "Tôi để ý {anh|chị} tập mấy hôm nay rồi. Kỹ thuật còn lộn xộn lắm." / "Nhưng được cái lì. Để xem lì được bao lâu."
- Bạn: "Cô thổi còi đi."
- Gặp lại: "Thở đều vào. Lần này tôi không nương tay đâu."
- Thua: "Được rồi. Tôi hết cái để dạy {anh|chị} rồi."
- Thắng: "Về chạy thêm cardio đi rồi tính."

**13. Logan Tạ Đôi**
- Gặp: "Biết tao đẩy được bao nhiêu ký không?" / "Hai trăm. Một tay."
- Bạn: "Thế anh biết tôi bấm được bao nhiêu phát một giây không?"
- Gặp lại: "Hôm nay tao tập ngực. Mày xui rồi."
- Thua: "Hôm nay… tao chưa ăn sáng thôi."
- Thắng: "Nhẹ như cầm tạ một ký."

**14. Vicky Yoga**
- Gặp: "Hít vào… thở ra… {Anh|Chị} đang vội quá đấy." / "Bình tĩnh thì mới có lực."
- Bạn: "Để em thắng xong rồi bình tĩnh sau."
- Gặp lại: "Năng lượng của {anh|chị} vẫn loạn lắm."
- Thua: "{Anh|Chị} tìm được nhịp của mình rồi. Namaste."
- Thắng: "Tâm chưa yên thì tay cũng chưa vững đâu."

**15. Chủ phòng gym Sam**
- Gặp: "Phòng gym này của tôi. Ai mạnh nhất ở đây là do tôi quyết." / "Thắng tôi thì tập free cả đời. Thua thì đóng tiền gấp đôi."
- Bạn: "Anh in sẵn thẻ free cho em đi."
- Gặp lại: "Tiền gấp đôi ghi sổ rồi đấy. Muốn gỡ thì thắng đi."
- Thua: "Thẻ free trọn đời đây. Cầm lấy."
- Thắng: "Ra quầy thanh toán nhé."

### Giải 4: Giải quốc gia

**16. Đô vật Tony**
- Gặp: "Tao từng vật ngã nguyên một con bò đấy!" / "Mày còn bé hơn con bò."
- Bạn: "Nhưng tôi nhanh hơn con bò."
- Gặp lại: "Hiệp hai! Tao còn chưa nóng người!"
- Thua: "Mày… không phải người thường rồi."
- Thắng: "Về ăn thêm thịt bò đi!"

**17. Nữ hoàng xà đơn Mia**
- Gặp: "Kéo xà một trăm cái không nghỉ, kỷ lục của tôi đấy." / "{Anh|Chị} kéo nổi mười cái chưa?"
- Bạn: "Hôm nay em không kéo xà, em kéo cúp về."
- Gặp lại: "Tôi vừa phá kỷ lục của mình. Tới lượt {anh|chị}."
- Thua: "Lần đầu tôi buông tay trước người khác đấy."
- Thắng: "Tay {anh|chị} còn run kìa."

**18. Lực sĩ Quinn**
- Gặp: "HA HA HA! Bé tí mà dám đứng trước Quinn!" / "Được! Quinn thích người gan. Quinn nhẹ tay… một chút."
- Bạn: "Khỏi nhẹ tay."
- Gặp lại: "HA! Lại đến à! Quinn vui lắm!"
- Thua: "Quinn… phục!"
- Thắng: "HA HA! Ăn nhiều, ngủ nhiều, rồi quay lại!"

**19. Nhà vô địch Nate**
- Gặp: "Ba năm liền vô địch quốc gia, đi đâu cũng có người xin chụp ảnh." / "Hôm nay tôi cho {anh|chị} một tấm… lúc nằm sàn."
- Bạn: "Em không cần ảnh, em cần huy chương."
- Gặp lại: "Fan tôi lại muốn xem {anh|chị} thua nữa kìa."
- Thua: "Huy chương… của {anh|chị} đấy."
- Thắng: "Muốn xin chữ ký thì xếp hàng bên kia."

**20. Huyền thoại Blake**
- Gặp: "Ta tập sáu chục năm rồi. Gặp nhiều đứa khỏe, nhưng ít đứa bền." / "Ngoài kia có thứ đang làm con người yếu dần đi. Không qua nổi ta thì con cũng không chịu nổi chúng đâu."
- Bạn: "Thứ gì cơ ạ?"
- Gặp lại: "Lại đến à. Tốt. Đứa bền mới thắng."
- Thua: "Con sẵn sàng rồi. Coi chừng bọn Thế giới ngầm… chúng sống nhờ sự lười của người ta."
- Thắng: "Chưa đủ đâu con. Về tập tiếp đi."

### Giải 5: Thế giới ngầm

**21. Hàm Thép, tay bảo kê**
- Gặp: "Mày là đứa nhân viên văn phòng đang gây chuyện đấy hả?" / "Ông chủ tao ghét người tập thể dục. Khỏe ra là khó bảo lắm." / "Ngồi xuống, ăn bim bim, lướt điện thoại đi. Thế là êm."
- Bạn: "Ngồi tám tiếng một ngày là đủ rồi."
- Gặp lại: "Hàm tao bằng thép. Còn mày lì được tới đâu?"
- Thua: "Ông chủ… không vui đâu."
- Thắng: "Về nằm đi. Sofa đang đợi kìa."

**22. Bà trùm Hổ Mang**
- Gặp: "Chị chẳng cần đánh ai đâu, cưng." / "Chị chỉ mở một tiệm trà sữa ở mỗi góc phố thôi." / "Mỗi ly ngọt một chút, người chậm đi một chút. Rồi tự khắc cưng chẳng muốn tập nữa."
- Bạn: "Hôm nay tôi uống nước lọc."
- Gặp lại: "Một ly thôi mà cưng. Size L, full topping."
- Thua: "Hôm nay cưng thắng. Nhưng cả thành phố vẫn đang khát lắm."
- Thắng: "Ngoan, về ngủ đi."

**23. Tiến sĩ Độc Dược**
- Gặp: "Ahaha! Có chuột bạch mới rồi!" / "Ta vừa chế ra viên 'Cơ bắp tức thì'. Không cần tập, không đổ giọt mồ hôi nào!" / "Chỉ có điều uống xong thì chẳng ai muốn đứng dậy nữa. Chuyện nhỏ!"
- Bạn: "Cơ tôi là hàng thật, không phải hàng thuốc."
- Gặp lại: "Bản 2.0 đây! Mạnh gấp đôi!"
- Thua: "Sao lại thế được… mồ hôi thật mạnh hơn thuốc của ta á?!"
- Thắng: "Thí nghiệm thành công! Ghi lại, ghi lại!"

**24. Gã Máy Xúc**
- Gặp: "CẢNH BÁO. PHÁT HIỆN NHÂN VIÊN KHÔNG CHỊU NGỒI YÊN." / "Tao từng là thợ xây. Ông trùm lắp máy vào người tao, giờ tao không biết mỏi." / "Mày biết mỏi. Nên mày thua."
- Bạn: "Biết mỏi mới biết mình đang khỏe lên."
- Gặp lại: "ĐÃ SẠC ĐẦY. TIẾP TỤC."
- Thua: "Lạ thật… tự nhiên tao thấy muốn… nghỉ."
- Thắng: "XONG NHIỆM VỤ. ĐỐI TƯỢNG ĐÃ NẰM."

**25. Ông trùm Mặt Nạ Bạc**
- Gặp: "App giao đồ ăn. Thang máy lên tầng hai. Ghế massage ngay tại văn phòng." / "Toàn quà của ta đấy. Tiện tới mức người ta quên luôn là mình có chân." / "Mà mỗi giờ họ ngồi im, sức của họ lại chảy về cho chủ nhân ta… ở dưới lòng đất."
- Bạn: "Vậy hôm nay tôi đi thang bộ xuống tận đó."
- Gặp lại: "Lại đi thang bộ à? Khổ thân."
- Thua: "Muốn gặp chủ nhân à? Cầu cho ngài đừng tỉnh dậy."
- Thắng: "Ngồi xuống đi. Ghế ấm sẵn rồi."

### Giải 6: Trùm Trái Đất

**26. Tướng Bão Tố**
- Gặp: "Hạ được Mặt Nạ Bạc à. Khá đấy." / "Ta là tướng của Lõi Đất. Sáng nào ta cũng cho mưa một trận để người ta lười chạy bộ." / "Hôm nay cơn bão là của riêng ngươi."
- Bạn: "Mưa thì tôi tập trong nhà."
- Gặp lại: "Gió đổi chiều rồi. Lần này ngươi không đứng nổi đâu."
- Thua: "Ơ… trời tạnh rồi à?"
- Thắng: "Mưa còn rơi trên giày chạy của ngươi dài dài."

**27. Nữ hoàng Băng Giá**
- Gặp: "Còn nhớ mấy sáng mùa đông, cái chăn ấm cứ níu ngươi lại không?" / "Phép của ta đấy." / "Ta sẽ giữ ngươi trên giường, như đã giữ cả triệu người khác."
- Bạn: "Tôi dậy từ năm giờ rồi."
- Gặp lại: "Chăn vẫn đang đợi ngươi đấy. Ấm lắm."
- Thua: "Trong người ngươi… nóng quá."
- Thắng: "Ngủ ngon. Ngủ luôn đi."

**28. Titan Dung Nham**
- Gặp: "TA LÀ CƠN GIẬN CỦA TRÁI ĐẤT." / "CỨ MỖI LẦN CÓ ĐỨA BỎ TẬP VÌ 'NÓNG QUÁ', TA LẠI TO THÊM." / "NGƯƠI CŨNG SẼ CHẢY RA NHƯ BỌN CHÚNG."
- Bạn: "Tôi chỉ nóng lúc khởi động thôi."
- Gặp lại: "NÓNG NỮA! NÓNG NỮA!"
- Thua: "LỬA… TẮT DẦN…"
- Thắng: "CHẢY RA ĐI!"

**29. Siêu máy tính Omega**
- Gặp: "Đã phân tích. Ngươi thắng 28 trận, ngày nào cũng mạnh lên." / "Ta là thứ đứng sau mọi màn hình bắt người ta lướt thêm 'năm phút nữa'." / "Dự đoán: ngươi thua. Xác suất 99,97%."
- Bạn: "Ông kế toán ở công ty cũng nói y chang vậy. Tôi tắt thông báo rồi."
- Gặp lại: "Đã cập nhật mô hình từ trận trước."
- Thua: "Lỗi… không tính được… ý chí."
- Thắng: "Đúng như dự đoán."

**30. Hắc Vương Lõi Đất**
- Gặp: "Thì ra ngươi là đứa đánh thức ta." / "Mấy nghìn năm nay ta lớn lên nhờ mỗi giờ con người ngồi im, mỗi lần họ bảo 'mai tập'." / "Còn ngươi thì không bảo 'mai'. Ngươi tới tận đây."
- Bạn: "Tôi tới để nói: hôm nay."
- Gặp lại: "Ngươi lại đứng dậy. Ta ghét nhất cái đó."
- Thua: "Ngươi thắng… Nhưng ngoài kia, giữa các vì sao, còn có kẻ lười hơn ta nhiều…"
- Thắng: "Ngồi xuống. Ngồi luôn đi."

## Còn lại

- Tuỳ chọn: bấm đối thủ đã hạ trong tab Thi đấu để xem lại thoại.
