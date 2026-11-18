# Bộ prompt tạo ảnh cho Gym God (dùng với ChatGPT)

Prompt viết bằng tiếng Anh vì công cụ tạo ảnh hiểu tiếng Anh chính xác hơn. Bạn chỉ cần sao chép từng khối và dán.

## Cách làm

1. Mở **một cuộc trò chuyện mới** cho mỗi nhóm ảnh (nhân vật / nền / icon). Không trộn các nhóm.
2. Dán prompt số 1 của nhóm. Tạo lại cho đến khi ưng ý, vì ảnh đầu tiên quyết định phong cách cho cả nhóm.
3. Dán lần lượt các prompt tiếp theo **trong cùng cuộc trò chuyện đó** để giữ đúng nhân vật và nét vẽ.
4. Nếu nhân vật bị lệch (khác mặt, khác tóc), đính kèm lại ảnh `rank1.png` và viết thêm: `Use the attached image as the character reference.`
5. Tải ảnh về, đổi tên đúng như bảng dưới, thả vào đúng thư mục con của `assets/original/`: `char` (rank, c2-rank…), `bg`, `icon`, `pet`, `rival`, `food`, `scene`, `ui` (ui-*, tab-*), `store` (cover-*, logo).
6. Chạy `python assets/build.py` để nén thành file `.webp` mà game dùng (tự tách nền ô caro giả nếu có).

## Tên file và quy cách

| File | Nội dung | Khung ảnh | Nền |
|---|---|---|---|
| `rank1.png` … `rank6.png` | Nhân vật 6 hạng | Dọc 1024×1536 | Trong suốt |
| `bg1.png` | Nền văn phòng (hạng 1–3) | Ngang 1536×1024 | Kín |
| `bg2.png` | Nền phòng gym (hạng 4–6), không bắt buộc | Ngang 1536×1024 | Kín |
| `icon-tay.png`, `icon-vai.png`, `icon-nguc.png`, `icon-bung.png`, `icon-mat.png`, `icon-chan.png`, `icon-lung.png`, `icon-cardio.png` | Icon 8 bài tập | Vuông 1024×1024 | Trong suốt |

Kiểm tra nhanh trước khi lưu ảnh nhân vật:

- Thấy đủ từ đỉnh đầu đến đế giày, không bị cắt.
- Nhân vật đứng giữa, nhìn thẳng, chân sát mép dưới.
- Không có chữ, không có bóng dưới đất, không có hào quang (game tự vẽ các thứ đó).
- Nền trong suốt thật (ô caro khi xem trước). Nếu ChatGPT không ra nền trong suốt, thay câu `transparent background` bằng `flat pure magenta (#FF00FF) background` và báo tôi để tôi tách nền.

Thiếu ảnh nào thì game vẫn chạy với hình vẽ code cho phần đó, nên bạn có thể thả ảnh vào dần.

---

## Nhóm 1: Nhân vật (6 ảnh, cùng một cuộc trò chuyện)

### rank1.png — dán nguyên khối này trước

```
Create a 2D game character sprite. Portrait canvas 1024x1536, transparent background.

ART STYLE: clean modern anime style for a mobile game. Crisp dark outlines of even thickness, soft cel shading with two tones, bright saturated colors, slightly chibi proportions (about 4.5 heads tall), big expressive eyes. Flat, readable shapes. No painterly texture, no photorealism.

CHARACTER (keep identical in every image of this chat): a Vietnamese male office worker, about 28 years old. Short messy black hair with a side part, round face, thick round black glasses, small nose. Outfit base: white long-sleeve dress shirt, red necktie, navy blue slacks, brown belt with a gold buckle, dark brown leather shoes, a blue office lanyard with a blank ID card.

FRAMING RULES (apply to every image of this chat):
- Full body, from the top of the hair to the soles of the shoes, nothing cropped.
- Standing, facing the viewer straight on, centered horizontally.
- The character fills about 85% of the canvas height; feet rest near the bottom edge with a small margin.
- Single character only. No ground shadow, no floor, no background, no glow or aura, no text, no logo, no border, no extra props floating around.

STAGE 1 of 6 — "Burnt-out office worker": weak and out of shape. Slouching posture, rounded shoulders, a big soft pot belly pushing the shirt out, thin arms and thin legs. Shirt wrinkled and half untucked, tie loosened and crooked. Dark eye bags, tired worried expression, one sweat drop on the forehead. Arms hanging limply at his sides.
```

### rank2.png

```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 2 of 6 — "Casual beginner": the body is almost the same as stage 1 (still a pot belly, still thin arms), but he stands a little straighter. Sleeves rolled up to the elbows, a red sweatband on his forehead, still wearing glasses. Holding a plastic water bottle in one hand like a dumbbell. Hopeful, slightly nervous smile.
```

### rank3.png

```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 3 of 6 — "Amateur gymgoer": noticeably slimmer belly, straighter back, arms and legs starting to show some muscle. Shirt tucked in neatly, sleeves rolled up, tie tidy, still wearing glasses and the red sweatband. Holding a small dumbbell in one hand, the other hand in a fist of determination. Confident friendly smile, no eye bags.
```

### rank4.png

```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 4 of 6 — "Toned body": fit athletic build, flat stomach, broad shoulders, defined forearms. No glasses anymore. The white shirt now fits tightly over his chest and arms, sleeves rolled up, tie neat. Standing tall with one hand on his hip and the other giving a thumbs up. Bright confident grin.
```

### rank5.png

```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 5 of 6 — "Six-pack loading": muscular build with big arms, wide chest and a narrow waist. No glasses. The white shirt is unbuttoned and open, showing defined abs; sleeves torn off at the shoulders; the red tie hangs loose around his neck. Flexing one bicep while the other fist rests on his hip. Cocky smirk, sharp eyebrows.
```

### rank6.png

```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 6 of 6 — "Office gym god": huge heroic bodybuilder physique, massive shoulders and arms, powerful legs, still clearly the same face and hairstyle. No glasses. Shirtless with only a torn white collar and cuffs left, the red tie worn as a headband with the ends flying, navy slacks, belt and shoes unchanged, lanyard still around his neck. Arms crossed over his chest in a power stance, feet apart. Fierce proud smile. Remember: no glow, no aura, no background effects.
```

---

## Nhóm 2: Nền (cuộc trò chuyện mới)

### bg1.png

```
Create a 2D game background. Landscape canvas 1536x1024, fully painted, no transparency.

ART STYLE: clean modern anime background art for a mobile game, soft cel shading, slightly muted and darker colors so that a bright character placed in front stands out.

SCENE: an open-plan office in the evening, seen straight on at eye level. Rows of desks with monitors, office chairs, a water cooler, potted plants, and large windows showing a city skyline at dusk with purple and orange sky.

LAYOUT RULES:
- The floor takes up the bottom 40% of the image and is plain and uncluttered (simple carpet or tiles).
- The middle third of the image is kept open and simple, with furniture pushed to the left and right sides, because a character will stand in the center.
- No people, no characters, no animals.
- No readable text, no logos, no brand names, no UI elements, no border.
```

### bg2.png (không bắt buộc)

```
Same art style, same canvas and layout rules as the previous image.

SCENE: a modern gym in the evening, seen straight on at eye level. Dumbbell racks, weight benches, a squat rack, punching bag and mirrors along the back wall, large windows showing the same city skyline at dusk. Rubber gym floor, plain and uncluttered. Furniture and equipment pushed to the left and right sides, center kept open. No people, no text, no logos.
```

---

## Nhóm 3: Icon bài tập (cuộc trò chuyện mới, 8 ảnh)

### icon-tay.png — dán nguyên khối này trước

```
Create a 2D game icon. Square canvas 1024x1024, transparent background.

ART STYLE (keep identical for every icon of this chat): clean modern anime mobile game icon, crisp dark outline of even thickness, soft cel shading with two tones, bright saturated colors, simple readable shape that is still clear when shrunk to 64 pixels.

ICON RULES (apply to every icon of this chat):
- One single subject, centered, filling about 80% of the canvas.
- No background, no frame, no badge shape behind it, no ground shadow, no text, no numbers, no logo.
- Skin tone, when skin is shown: light warm tan.

SUBJECT: a flexed muscular arm curling a plastic water bottle like a dumbbell.
```

### 7 icon còn lại — dán từng khối, lưu đúng tên file ghi phía trên

`icon-vai.png`
```
Same art style and icon rules as the first icon. SUBJECT: a pair of strong shoulders and arms pressing a dumbbell overhead, seen from the front, cropped at the chest, no face.
```

`icon-nguc.png`
```
Same art style and icon rules as the first icon. SUBJECT: a muscular male chest in a white tank top, seen from the front, cropped from neck to ribs, no face.
```

`icon-bung.png`
```
Same art style and icon rules as the first icon. SUBJECT: a six-pack abdomen, seen from the front, cropped from below the chest to the waistband, no face.
```

`icon-mat.png`
```
Same art style and icon rules as the first icon. SUBJECT: one big bright anime eye with a sparkle, next to a pair of round black glasses taken off and set aside.
```

`icon-chan.png`
```
Same art style and icon rules as the first icon. SUBJECT: a muscular leg in navy shorts and a sneaker, bent in a squat position, seen from the side, cropped at the hip.
```

`icon-lung.png`
```
Same art style and icon rules as the first icon. SUBJECT: a wide muscular back doing a pull-up on a bar, seen from behind, cropped at the waist, head only as a simple black-haired shape.
```

`icon-cardio.png`
```
Same art style and icon rules as the first icon. SUBJECT: a red running sneaker in mid-stride with small speed lines and a few sweat drops.
```


---

# Phần 2: Bạn tập, đối thủ và nhân vật mới

Cách làm giống phần 1: mỗi nhóm một cuộc trò chuyện mới, dán prompt đầu tiên trước, các prompt sau dán trong cùng cuộc trò chuyện. Để nét vẽ khớp với ảnh đã có, **đính kèm `original/rank1.png` vào tin nhắn đầu tiên của mỗi cuộc trò chuyện**; prompt đầu của mỗi nhóm đã có sẵn câu yêu cầu vẽ theo ảnh đính kèm.

Lưu ảnh vào `assets/original` với đúng tên file, rồi chạy `python assets/build.py`.

Thứ tự nên làm: bạn tập (8 ảnh) → đối thủ (20 ảnh) → nhân vật mới (18 ảnh). Hai nhóm đầu thay cho emoji đang dùng trong game; nhóm nhân vật mới cần tôi viết thêm phần chọn nhân vật sau khi có ảnh.

| File | Nội dung | Khung ảnh | Nền |
|---|---|---|---|
| `pet-dog.png`, `pet-cat.png`, `pet-ham.png`, `pet-frog.png`, `pet-ape.png`, `pet-roo.png`, `pet-tiger.png`, `pet-dragon.png` | 8 bạn tập | Vuông 1024×1024 | Trong suốt |
| `rival-01.png` … `rival-20.png` | Chân dung 20 đối thủ | Vuông 1024×1024 | Trong suốt |
| `c2-rank1.png` … `c2-rank6.png`, `c3-…`, `c4-…` | 3 nhân vật mới, mỗi người 6 hạng | Dọc 1024×1536 | Trong suốt |

---

## Nhóm 4: Bạn tập (cuộc trò chuyện mới, đính kèm rank1.png)

### pet-dog.png — dán nguyên khối này trước

```
Create a 2D game icon. Square canvas 1024x1024, real transparent background (alpha channel). Do not draw a checkerboard pattern.

ART STYLE (keep identical for every image of this chat): match the art style of the attached image: clean modern anime mobile game art, crisp dark outline of even thickness, soft cel shading with two tones, bright saturated colors. The subject is a cute chibi animal mascot with a big head, big sparkling eyes and a small body, clearly readable when shrunk to 64 pixels.

ICON RULES (apply to every image of this chat):
- One single animal, full body, centered, filling about 80% of the canvas, facing the viewer or three-quarter view.
- Every animal wears a small red sweatband, like a tiny gym buddy.
- No background, no frame, no ground shadow, no text, no numbers, no logo.

SUBJECT: a happy shiba-colored puppy jogging on its hind legs, tongue out, wearing tiny running shoes.
```

### 7 bạn tập còn lại

`pet-cat.png`
```
Same art style and icon rules as the first image. SUBJECT: a calm orange tabby cat sitting in a yoga lotus pose with its eyes closed and paws together, on a small rolled-out yoga mat.
```

`pet-ham.png`
```
Same art style and icon rules as the first image. SUBJECT: a chubby golden hamster sprinting inside a small exercise wheel, cheeks puffed, determined face.
```

`pet-frog.png`
```
Same art style and icon rules as the first image. SUBJECT: a bright green frog doing a deep squat with a tiny barbell across its shoulders, serious face.
```

`pet-ape.png`
```
Same art style and icon rules as the first image. SUBJECT: a friendly muscular gorilla lifting a heavy dumbbell overhead with one arm, proud grin.
```

`pet-roo.png`
```
Same art style and icon rules as the first image. SUBJECT: an energetic kangaroo in a boxing stance wearing red boxing gloves, one fist forward.
```

`pet-tiger.png`
```
Same art style and icon rules as the first image. SUBJECT: a stern but cute tiger coach standing upright with arms crossed, a whistle around its neck and a stopwatch in one paw.
```

`pet-dragon.png`
```
Same art style and icon rules as the first image. SUBJECT: a small golden eastern dragon with a muscular chest flexing both arms like a bodybuilder, tiny wings spread, confident smile. It should look the most impressive and legendary of all the mascots.
```

---

## Nhóm 5: Đối thủ (cuộc trò chuyện mới, đính kèm rank1.png)

Nếu cuộc trò chuyện dài quá làm nét vẽ lệch dần, mở cuộc trò chuyện mới ở đầu mỗi giải (ảnh 06, 11, 16), đính kèm lại `rank1.png` và dán lại khối đầu tiên, chỉ thay dòng SUBJECT.

### rival-01.png — dán nguyên khối này trước

```
Create a 2D game character portrait. Square canvas 1024x1024, real transparent background (alpha channel). Do not draw a checkerboard pattern.

ART STYLE (keep identical for every image of this chat): match the art style of the attached image: clean modern anime mobile game art, crisp dark outline of even thickness, soft cel shading with two tones, bright saturated colors, slightly chibi proportions with big expressive eyes.

PORTRAIT RULES (apply to every image of this chat):
- Bust portrait: head, shoulders and upper chest only, facing the viewer, centered, filling about 85% of the canvas.
- All characters are Vietnamese adults. Each one must look clearly different from the others (hair, face shape, outfit, expression).
- A confident "rival" expression: smirk, raised eyebrow or competitive grin.
- No background, no frame, no ground shadow, no text, no name tag text, no logo.

SUBJECT: a male accountant in his thirties, neat side-parted hair, thin rectangular glasses, light blue shirt with a calculator in the chest pocket.
```

### 19 đối thủ còn lại — mỗi khối một ảnh

Mỗi prompt bắt đầu bằng cùng một câu, chỉ khác phần SUBJECT:

```
Same art style and portrait rules as the first image. SUBJECT: <dán mô tả ở bảng dưới>
```

| File | SUBJECT |
|---|---|
| `rival-02.png` | a cheerful female receptionist in her twenties, hair in a neat bun, headset microphone, white blouse with a small scarf. |
| `rival-03.png` | a young male intern about 20 years old, messy hair, oversized shirt, backpack straps on his shoulders, nervous but eager grin. |
| `rival-04.png` | a stocky security guard uncle about 50, short gray hair, thick mustache, dark blue guard uniform with a cap. |
| `rival-05.png` | a male team leader about 40, slicked-back hair, crisp white shirt, dark vest, holding a coffee mug at chest height. |
| `rival-06.png` | a deputy boss about 45, round face, short beard, brown suit jacket, gold-rimmed glasses, smug smile. |
| `rival-07.png` | a strong canteen lady about 50, hair under a white kitchen cap, apron, holding a ladle over her shoulder, warm but tough smile. |
| `rival-08.png` | an IT guy about 30, long messy hair tied back, black hoodie, headphones around his neck, sleepy smirk. |
| `rival-09.png` | an HR woman about 35, sharp bob haircut, red lipstick, gray blazer, holding a clipboard, raised eyebrow. |
| `rival-10.png` | a company director about 55, silver hair, expensive black suit, red tie, arms crossed, intimidating calm smile. |
| `rival-11.png` | a gym rookie about 22, buzz cut, brand-new bright tank top, towel around his neck, overexcited grin. |
| `rival-12.png` | a female fitness coach about 30, high ponytail, sports jacket zipped halfway, whistle around her neck, confident smile. |
| `rival-13.png` | a huge male weightlifter about 35, shaved head, thick neck, black sleeveless shirt, chalk on his shoulders, fierce grin. |
| `rival-14.png` | a serene female yoga master about 28, long braid, pastel yoga top, eyes half closed, small knowing smile. |
| `rival-15.png` | a gym owner about 45, tanned, short spiky hair, gold chain, tight polo shirt over big muscles, wide business smile. |
| `rival-16.png` | a male wrestler about 30, cauliflower ears, short mohawk, red wrestling singlet straps, aggressive grin. |
| `rival-17.png` | a female calisthenics athlete about 25, short undercut hair, athletic crop top, chalky hands gripping a bar above her head, proud smirk. |
| `rival-18.png` | a giant strongman about 40, big braided beard, bald head, leather lifting belt strap over one shoulder, booming laugh. |
| `rival-19.png` | a national champion about 28, handsome, styled black hair, gold medal around his neck, national team jacket, cool confident smile. |
| `rival-20.png` | a legendary old master about 65, long white hair tied back, white beard, still incredibly muscular, simple dark training robe, calm piercing eyes. He should look the most powerful of all. |

---

## Nhóm 6: Nhân vật mới (mỗi nhân vật một cuộc trò chuyện mới, đính kèm rank1.png)

Mỗi nhân vật: dán khối "ảnh hạng 1" của người đó trước, rồi dán lần lượt **5 prompt dùng chung** ở cuối mục này. Lưu thành `c2-rank1.png` … `c2-rank6.png` (tương tự với `c3`, `c4`).

### c2-rank1.png — Nữ nhân viên kế toán

```
Create a 2D game character sprite. Portrait canvas 1024x1536, real transparent background (alpha channel). Do not draw a checkerboard pattern.

ART STYLE: match the art style of the attached image exactly: clean modern anime mobile game art, crisp dark outlines of even thickness, soft cel shading with two tones, bright saturated colors, slightly chibi proportions (about 4.5 heads tall), big expressive eyes.

CHARACTER (keep identical in every image of this chat): a Vietnamese female office worker, about 27 years old. Shoulder-length black hair in a low ponytail with a few loose strands, round face, large round glasses. Outfit base: pale pink long-sleeve blouse, navy blue knee-length pencil skirt, black flat shoes, a blue office lanyard with a blank ID card.

FRAMING RULES (apply to every image of this chat):
- Full body, from the top of the hair to the soles of the shoes, nothing cropped.
- Standing, facing the viewer straight on, centered horizontally.
- The character fills about 85% of the canvas height; feet rest near the bottom edge with a small margin.
- Single character only. No ground shadow, no floor, no background, no glow or aura, no text, no logo, no border.

STAGE 1 of 6 — "Burnt-out office worker": weak and out of shape. Slouching posture, rounded shoulders, a soft round belly, thin arms and legs. Blouse wrinkled and half untucked. Dark eye bags, tired worried expression, one sweat drop on the forehead. Arms hanging limply, one hand holding an empty coffee cup.
```

### c3-rank1.png — Chú bảo vệ

Dùng nguyên khối trên, chỉ thay hai đoạn CHARACTER và STAGE 1 bằng:

```
CHARACTER (keep identical in every image of this chat): a Vietnamese male security guard, about 50 years old. Short gray hair, thick gray mustache, kind tired eyes, square face. Outfit base: dark blue short-sleeve guard uniform shirt with shoulder straps, dark blue trousers, black belt, black boots, a guard cap, a whistle on a cord around his neck.

STAGE 1 of 6 — "Burnt-out guard": weak and out of shape. Slouching posture, a big round belly straining the uniform buttons, thin arms and legs. Cap crooked, shirt half untucked. Sleepy half-closed eyes, yawning, one sweat drop on the forehead. Arms hanging limply at his sides.
```

### c4-rank1.png — Cậu thực tập sinh

Dùng nguyên khối trên, chỉ thay hai đoạn CHARACTER và STAGE 1 bằng:

```
CHARACTER (keep identical in every image of this chat): a Vietnamese male intern, about 20 years old. Fluffy messy brown-black hair covering his forehead, big anxious eyes, thin face, square thin-framed glasses. Outfit base: oversized light gray hoodie over a white shirt collar, black slim trousers, white sneakers, a green office lanyard with a blank ID card, a small backpack.

STAGE 1 of 6 — "Frail intern": extremely skinny and frail instead of chubby. Hunched posture, narrow shoulders, stick-thin arms and legs, hoodie hanging loose on him. Dark eye bags, nervous expression, one sweat drop on the forehead. Both hands gripping his backpack straps.
```

### 5 prompt dùng chung cho hạng 2–6 (dán lần lượt trong cuộc trò chuyện của từng nhân vật)

Hạng 2
```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 2 of 6 — "Casual beginner": the body is almost the same as stage 1, but the posture is a little straighter. Sleeves rolled up, a red sweatband on the forehead, still wearing glasses if the character has them. Holding a plastic water bottle in one hand like a dumbbell. Hopeful, slightly nervous smile.
```

Hạng 3
```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 3 of 6 — "Amateur gymgoer": visibly healthier body, straighter back, arms and legs starting to show some muscle tone. Outfit worn neatly, sleeves rolled up, red sweatband on. Holding a small dumbbell in one hand, the other hand in a fist of determination. Confident friendly smile, no eye bags.
```

Hạng 4
```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 4 of 6 — "Toned body": fit athletic build, flat stomach, strong shoulders, defined forearms. No glasses anymore. The same base outfit now fits snugly over an athletic body, sleeves rolled up, red sweatband on. Standing tall with one hand on the hip and the other giving a thumbs up. Bright confident grin.
```

Hạng 5
```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 5 of 6 — "Six-pack loading": clearly muscular and athletic, strong arms, narrow waist. No glasses. The base outfit is modified for training: sleeves torn off at the shoulders and the top shortened or opened to show a toned, defined stomach, in a sporty and tasteful way. Red sweatband on. Flexing one bicep while the other fist rests on the hip. Cocky smirk.
```

Hạng 6
```
Same character, same art style, same canvas and framing rules as the first image.

STAGE 6 of 6 — "Gym god": the peak heroic athlete version of this character, very powerful shoulders, arms and legs, still clearly the same face and hairstyle. No glasses. A sleeveless, battle-worn sporty version of the base outfit in the same colors, lanyard or whistle still around the neck, the red sweatband now a long headband with the ends flying. Arms crossed in a power stance, feet apart. Fierce proud smile. Remember: no glow, no aura, no background effects.
```


---

# Phần 3: Ảnh còn thiếu (34 ảnh)

Cả 34 ảnh của phần này đã có và đã nối vào game. Prompt giữ lại để tạo lại ảnh khi cần. Ảnh lưu vào thư mục con tương ứng của `assets/original/` rồi chạy `python assets/build.py`.

| Nhóm | Số ảnh | Tên file | Khung | Nền | Ưu tiên |
|---|---|---|---|---|---|
| 7. Nền nhà | 1 | `bg3.png` | Ngang 1536×1024 | Kín | Cao |
| 8. Món ăn | 9 | `food-*.png` | Vuông 1024×1024 | Trong suốt | Cao |
| 9. Màn chờ chuyển cảnh | 6 | `scene-*.png` | Vuông 1024×1024 | Trong suốt | Vừa |
| 10. Icon giao diện | 14 | `ui-*.png`, `tab-*.png` | Vuông 1024×1024 | Trong suốt | Vừa |
| 11. Ảnh bìa và logo | 4 | `cover-*.png`, `logo.png` | Xem từng ảnh | Kín | Trước khi đăng game |

`cover-*` và `logo` (thư mục `original/store`) chỉ dùng cho trang CrazyGames, không nằm trong game.

---

## Nhóm 7: Nền nhà (cuộc trò chuyện mới, đính kèm `original/bg1.png`)

### bg3.png

```
Create a 2D game background. Landscape canvas 1536x1024, fully painted, no transparency. Use the attached image as the art style reference: same clean modern anime background art, same line weight, same slightly muted and darker colors so that a bright character placed in front stands out.

SCENE: a small, cosy modern apartment at night, seen straight on at eye level. Living area on the left with a sofa, a low table and a TV. Open kitchenette on the right with a fridge, a rice cooker and a small dining table. Warm yellow lamp light, a window showing the same city skyline at night, a rolled-up yoga mat in a corner, a pair of dumbbells on the floor near the wall.

LAYOUT RULES:
- The floor takes up the bottom 40% of the image and is plain and uncluttered (wooden floor or a simple rug).
- The middle third of the image is kept open and simple, with furniture pushed to the left and right sides, because a character will stand in the center.
- No people, no characters, no animals.
- No readable text, no logos, no brand names, no UI elements, no border.
```

---

## Nhóm 8: Món ăn (cuộc trò chuyện mới, đính kèm `original/icon-tay.png`, 9 ảnh)

### food-h.png (Cơm gà luộc) — dán nguyên khối này trước

```
Create a 2D game icon. Square canvas 1024x1024, transparent background. Use the attached image as the art style reference.

ART STYLE (keep identical for every icon of this chat): clean modern anime mobile game icon, crisp dark outline of even thickness, soft cel shading with two tones, bright saturated appetizing colors, simple readable shape that is still clear when shrunk to 64 pixels.

ICON RULES (apply to every icon of this chat):
- One single dish or combo, centered, filling about 80% of the canvas, seen from a slight 3/4 top-down angle.
- No background, no frame, no badge shape behind it, no table, no ground shadow, no text, no numbers, no logo, no brand names.
- No hands, no people.

SUBJECT: a healthy meal on a tray: a bowl of white rice, sliced boiled chicken breast, steamed green vegetables and a small bowl of clear soup.
```

### 8 món còn lại — dán từng khối, lưu đúng tên file ghi phía trên

`food-h2.png` (Salad cá hồi)
```
Same art style and icon rules as the first icon. SUBJECT: a salmon salad bowl: fresh green lettuce, slices of pink grilled salmon, cherry tomatoes, cucumber and a lemon wedge.
```

`food-h3.png` (Yến mạch chuối)
```
Same art style and icon rules as the first icon. SUBJECT: a bowl of oatmeal topped with banana slices, a few blueberries and a drizzle of honey, with a spoon in the bowl.
```

`food-p.png` (Ức gà, trứng)
```
Same art style and icon rules as the first icon. SUBJECT: a high-protein plate: a grilled chicken breast with grill marks, two boiled eggs cut in half, and a few broccoli florets.
```

`food-p2.png` (Bò bít tết)
```
Same art style and icon rules as the first icon. SUBJECT: a thick juicy beef steak on a black cast-iron sizzling plate, with a fried egg and a few french fries on the side, a little steam rising.
```

`food-p3.png` (Sinh tố whey)
```
Same art style and icon rules as the first icon. SUBJECT: a plastic protein shaker bottle filled with a creamy chocolate shake, next to a scoop of protein powder and half a banana.
```

`food-j.png` (Trà sữa, gà rán)
```
Same art style and icon rules as the first icon. SUBJECT: a tall cup of bubble milk tea with black tapioca pearls and a wide straw, next to a paper bucket of crispy golden fried chicken.
```

`food-j2.png` (Pizza phô mai)
```
Same art style and icon rules as the first icon. SUBJECT: a cheese pizza with one slice being pulled away, long strings of melted cheese stretching, pepperoni on top.
```

`food-j3.png` (Mì tôm trứng)
```
Same art style and icon rules as the first icon. SUBJECT: a steaming bowl of instant ramen noodles with a soft egg yolk on top, chopped green onions, and chopsticks resting on the bowl.
```

---

## Nhóm 9: Màn chờ chuyển cảnh (cuộc trò chuyện mới, đính kèm `original/rank1.png`, 6 ảnh)

Hiện ở giữa màn hình tối trong 2–3 giây, phía trên dòng chữ "Khò khò...", "Đi đến công ty...". Nhân vật vẽ kiểu chibi cho dễ thương và khỏi phải khớp với hình theo hạng.

### scene-sleep.png (Khò khò) — dán nguyên khối này trước

```
Create a 2D game illustration sticker. Square canvas 1024x1024, transparent background. Use the attached image as the character reference: a young Asian office worker with messy black hair and round glasses.

ART STYLE (keep identical for every image of this chat): cute chibi version of the character (big head, small body, about 2.5 heads tall), clean modern anime mobile game art, crisp dark outline of even thickness, soft cel shading, bright colors.

RULES (apply to every image of this chat):
- One small self-contained scene, centered, filling about 80% of the canvas.
- No background, no frame, no ground shadow, no text, no letters, no numbers, no logo.

SUBJECT: the character sleeping soundly in bed under a blanket, mouth slightly open, glasses on the bedside table, a small crescent moon and a few stars floating above. No "Z" letters.
```

### 5 ảnh còn lại

`scene-morning.png` (Buổi sáng)
```
Same art style, same character and rules as the first image. SUBJECT: the character sitting up in bed stretching both arms with a big yawn, messy bed hair, a bright cheerful sun rising behind him, a ringing alarm clock next to him.
```

`scene-commute.png` (Đi đến công ty)
```
Same art style, same character and rules as the first image. SUBJECT: the character in white shirt and red tie riding a small motor scooter, wearing a helmet, a briefcase strapped behind him, looking sleepy, small speed lines behind the scooter.
```

`scene-work.png` (Đang làm việc)
```
Same art style, same character and rules as the first image. SUBJECT: the character sitting at an office desk typing on a computer, a tall pile of paper documents next to him, a cup of coffee, a tired but determined face.
```

`scene-gym.png` (Đi đến phòng tập)
```
Same art style, same character and rules as the first image. SUBJECT: the character walking energetically to the right with a gym bag over his shoulder and a water bottle in his hand, tie loosened, an excited determined smile.
```

`scene-home.png` (Đi về nhà)
```
Same art style, same character and rules as the first image. SUBJECT: the character walking home tired but happy, a towel around his neck, gym bag in hand, a small cozy house with a lit window next to him under an evening moon.
```

---

## Nhóm 10: Icon giao diện (cuộc trò chuyện mới, đính kèm `original/icon-tay.png`, 14 ảnh)

Thay cho emoji trên thanh chỉ số, các tab và nhiệm vụ. Icon hiện rất nhỏ (20–40 pixel) nên hình phải thật đơn giản.

### ui-cal.png (Calo) — dán nguyên khối này trước

```
Create a 2D game UI icon. Square canvas 1024x1024, transparent background. Use the attached image as the art style reference.

ART STYLE (keep identical for every icon of this chat): clean modern anime mobile game icon, thick crisp dark outline of even thickness, flat cel shading with two tones and one small highlight, bright saturated colors. Extremely simple bold silhouette that is still clear when shrunk to 24 pixels.

ICON RULES (apply to every icon of this chat):
- One single object, centered, filling about 85% of the canvas, seen straight on.
- No background, no frame, no badge or circle behind it, no ground shadow, no text, no letters, no numbers, no logo.

SUBJECT: a bold orange and yellow flame, the calorie currency of the game.
```

### 13 icon còn lại

Với mỗi dòng, dán: `Same art style and icon rules as the first icon. SUBJECT:` rồi tới phần mô tả ở cột cuối.

| File | Dùng cho | Mô tả (SUBJECT) |
|---|---|---|
| `ui-star.png` | Sao lên đời | `a chunky golden five-pointed star with a small sparkle.` |
| `ui-sta.png` | Thể lực | `a bold yellow lightning bolt.` |
| `ui-fat.png` | Mệt mỏi | `a round tired face, light warm tan skin, half-closed eyes, a blue sweat drop on the forehead and a small puff of breath.` |
| `ui-kg.png` | Cân nặng | `a bathroom weighing scale seen from the front top, light blue, with a round dial that has a needle but no numbers.` |
| `ui-day.png` | Ngày | `a desk calendar page with a red top strip and two binder rings, the page is blank white.` |
| `ui-trophy.png` | Thành tựu | `a golden trophy cup with two handles on a small dark base.` |
| `ui-drink.png` | Nước tăng lực | `a slim energy drink can, electric blue with a yellow lightning bolt shape on it, no words.` |
| `ui-tap.png` | Nhiệm vụ bấm | `a hand with the index finger pointing and tapping, light warm tan skin, three small impact lines at the fingertip.` |
| `ui-clock.png` | Nhiệm vụ thời gian chơi | `a round stopwatch with a red button on top, plain white face with one hand, no numbers.` |
| `tab-ex.png` | Tab Bài tập | `a single heavy dumbbell, dark grey weights and a silver handle, tilted slightly.` |
| `tab-duel.png` | Tab Thách đấu | `two red boxing gloves bumping into each other with a small yellow impact star between them.` |
| `tab-pet.png` | Tab Bạn tập | `a cute orange animal paw print with pink toe pads.` |
| `tab-quest.png` | Tab Nhiệm vụ | `a brown clipboard holding a white sheet with three green check marks and three short grey lines.` |

---

## Nhóm 12: Khách ghé phòng tập (cuộc trò chuyện mới, đính kèm `original/rank1.png`, 3 ảnh)

Game tự vẽ vòng tròn màu và viền trắng bao quanh, nên ảnh chỉ cần người/vật, nền trong suốt, không khung. Ảnh hiện nhỏ (76–110px), nên chỉ lấy **từ ngực trở lên** và nét phải thật đậm. Thả vào `assets/original/icon/`, chạy `python assets/build.py`, rồi báo để nối ảnh vào game.

### icon-vis-pt.png (PT, vòng vàng) — dán nguyên khối này trước

```
Create a 2D game icon of a character bust. Square canvas 1024x1024, transparent background. Use the attached image as the art style reference: same clean modern anime mobile game style, crisp dark outlines of even thickness, two-tone cel shading, bright saturated colors, big expressive eyes.

ICON RULES (apply to every icon of this chat):
- Head and upper chest only, facing the viewer, centered, filling about 85% of the canvas. The head is large and easy to read when shrunk to 64 pixels.
- Single subject. No background, no frame, no circle or badge behind it, no ground shadow, no text, no letters, no numbers, no logo.

SUBJECT: a friendly, very muscular Vietnamese personal trainer, about 30 years old. Short undercut black hair, a red sports cap worn backwards, a tight black tank top showing big shoulders, a silver whistle on a red cord around the neck. Big confident grin, winking, one hand giving a thumbs up next to his face.
```

### icon-vis-crush.png (Crush, vòng hồng)

```
Same art style and icon rules as the first icon.

SUBJECT: the office crush, a pretty Vietnamese woman about 26 years old. Long glossy black hair in a high ponytail, a pastel pink sports jacket over a white top, a small towel over one shoulder. Shy sweet smile with rosy cheeks, one hand giving a small wave. Two tiny pink hearts floating near her head.
```

### icon-vis-cake.png (Bánh sinh nhật, vòng xanh)

```
Same art style and icon rules as the first icon, but the subject is an object instead of a person: one single object, centered, filling about 85% of the canvas.

SUBJECT: a small round birthday cake seen slightly from above, white frosting with pink drips, strawberries on top and one lit candle with a bright yellow flame, on a small paper plate. Looks extremely tempting.
```

## Nhóm 13: Kỹ năng Sao và Thử thách (cuộc trò chuyện mới, đính kèm `original/icon-tay.png`, 13 ảnh)

Icon hiện trong ô vuông 60px ở tab Lên đời, nền ô tối, nên vật thể phải sáng màu, nét đậm, thật đơn giản. Thả vào `assets/original/icon/`, chạy `python assets/build.py`, rồi báo để nối ảnh vào game.

### icon-sk-gold.png (Cú bấm vàng) — dán nguyên khối này trước

```
Create a 2D game icon. Square canvas 1024x1024, transparent background. Use the attached image as the art style reference.

ART STYLE (keep identical for every icon of this chat): clean modern anime mobile game icon, crisp dark outline of even thickness, soft cel shading with two tones, bright saturated colors, simple readable shape that is still clear when shrunk to 48 pixels. The icon will sit on a dark tile, so keep the subject bright with a strong outline.

ICON RULES (apply to every icon of this chat):
- One single subject, centered, filling about 80% of the canvas.
- No background, no frame, no badge or circle behind it, no ground shadow, no text, no letters, no numbers, no logo.
- Skin tone, when skin is shown: light warm tan.

SUBJECT: a golden hand with the index finger pressing down, shining like polished gold, with three small sparkles and short impact lines at the fingertip.
```

### 12 icon còn lại — dán từng khối trong cùng cuộc trò chuyện, lưu đúng tên file ghi phía trên

**Kỹ năng, nhánh 💪 Sức mạnh**

`icon-sk-mem.png` (Ký ức cơ bắp)
```
Same art style and icon rules as the first icon. SUBJECT: a cute pink cartoon brain with a flexed muscular arm on each side, lifting itself proudly, one small sparkle.
```

`icon-sk-crit.png` (Bấm chí mạng)
```
Same art style and icon rules as the first icon. SUBJECT: a jagged comic-book explosion burst in red, orange and yellow, with a fist punching out of its center.
```

**Kỹ năng, nhánh ⚡ Bền bỉ**

`icon-sk-lung.png` (Phổi thép)
```
Same art style and icon rules as the first icon. SUBJECT: a pair of stylized cartoon lungs made of shiny steel-blue metal with rivets, a small white puff of air above them.
```

`icon-sk-calm.png` (Hồi phục nhanh)
```
Same art style and icon rules as the first icon. SUBJECT: a green leaf and a small blue water drop together, with a soft circular arrow around them meaning recovery.
```

`icon-sk-spar.png` (Đấu tiết kiệm)
```
Same art style and icon rules as the first icon. SUBJECT: one red boxing glove resting on top of a small stack of three gold coins.
```

**Kỹ năng, nhánh 🌟 Lối sống**

`icon-sk-inv.png` (Đầu tư dài hạn)
```
Same art style and icon rules as the first icon. SUBJECT: a small green potted plant whose leaves are shaped like an upward arrow, a gold coin in the pot soil.
```

`icon-sk-fan.png` (Khách quen)
```
Same art style and icon rules as the first icon. SUBJECT: a gym membership card in bright orange with a small dumbbell symbol and a red heart, tilted slightly.
```

`icon-sk-away.png` (Ngủ ngon)
```
Same art style and icon rules as the first icon. SUBJECT: a fluffy white pillow with a yellow crescent moon resting on it and two small stars above.
```

**Thử thách**

`icon-ch-tap.png` (Chỉ dùng tay)
```
Same art style and icon rules as the first icon. SUBJECT: two open hands, palms facing the viewer, wrapped in white gym tape, with small sweat drops.
```

`icon-ch-fee.png` (Phòng gym tăng giá)
```
Same art style and icon rules as the first icon. SUBJECT: a big red price tag hanging from a heavy dumbbell, a bold upward red arrow on the tag, no numbers.
```

`icon-ch-party.png` (Mùa tiệc cưới)
```
Same art style and icon rules as the first icon. SUBJECT: a tall white wedding cake with pink ribbons and two small toasting champagne glasses in front of it, a little confetti.
```

`icon-ch-boss.png` (Sếp soi)
```
Same art style and icon rules as the first icon. SUBJECT: the stern face of a bald office boss with thick eyebrows and a red necktie, peeking over the top edge of a big pair of binoculars, cropped at the shoulders.
```

## Nhóm 14: Hạng 7–9 và phản diện Trái Đất (16 ảnh: 6 nhân vật, 10 phản diện)

Từ hạng 7, nhân vật có **sức mạnh siêu nhân**; đối thủ từ số 21 là **phản diện trên Trái Đất** (giải 5 "Thế giới ngầm", giải 6 "Trùm Trái Đất"). Ngoài Trái Đất để dành cho lần mở rộng sau.

Thiếu ảnh hạng mới thì game tạm dùng ảnh hạng 6; thiếu ảnh phản diện thì hiện emoji. Ảnh lưu vào `assets/original/char/` (nhân vật) và `assets/original/rival/` (phản diện), rồi chạy `python assets/build.py`.

### 14a. Nam, hạng 7–9 (cuộc trò chuyện mới, đính kèm `original/char/rank6.png` và `original/char/rank1.png`)

`rank7.png` — khối đầu tiên, dán cùng hai ảnh đính kèm:

```
The two attached images show the same 2D game character at stage 1 and stage 6 of his growth. Keep his face, hairstyle and art style identical.

ART STYLE: clean modern anime mobile game art, crisp dark outlines of even thickness, soft cel shading with two tones, bright saturated colors, slightly chibi proportions (about 4.5 heads tall), big expressive eyes.

FRAMING RULES (apply to every image of this chat):
- Portrait canvas 1024x1536, real transparent background (alpha channel). Do not draw a checkerboard pattern.
- Full body, from the top of the hair to the soles of the shoes, nothing cropped. If there is a cape, keep it inside the canvas.
- Standing, facing the viewer straight on, centered horizontally, feet near the bottom edge with a small margin.
- The character fills about 85% of the canvas height.
- Single character only. No ground shadow, no floor, no background, no big glow or aura around the body (the game draws its own aura), no text, no logo.

STAGE 7 of 9 — "Office superhuman": the stage 6 body, now awakened with a first superpower. Small crackling electric-blue sparks around both fists only, kept tight to the hands. The red tie is now tied around his neck as a short flowing scarf. Torn white shirt collar and cuffs, navy slacks, belt and shoes as before, the office lanyard ID card now shows a simple lightning bolt shape. One fist raised toward the sky, the other at his side. Determined heroic grin, eyes shining.
```

`rank8.png`
```
Same character, same art style, same canvas and framing rules.

STAGE 8 of 9 — "City hero": a full superhero suit designed from his office clothes: a navy bodysuit with white shirt-collar details at the neck, a red chest emblem shaped like a necktie, white gloves, navy boots with red trim, a long red cape. Small electric sparks around the fists only. Standing tall with both fists on his hips, chest out, cape flowing behind him. Confident heroic smile.
```

`rank9.png`
```
Same character, same art style, same canvas and framing rules.

STAGE 9 of 9 — "Guardian of Earth": the ultimate form. Navy and gold armored hero suit over the same muscular body, gold shoulder guards, a round chest emblem showing a small blue-and-green planet Earth, a long deep red cape with a subtle star pattern on the inside, gold-trimmed boots and gloves. The red tie is now a red headband with long flying ends. Arms crossed, feet apart, calm and unbeatable expression. Remember: no big glow or aura, no background.
```

### 14b. Nữ, hạng 7–9 (cuộc trò chuyện mới, đính kèm `original/char/c2-rank6.png` và `original/char/c2-rank1.png`)

`c2-rank7.png`: dán lại khối đầu tiên của 14a, chỉ đổi câu đầu thành:

```
The two attached images show the same 2D game character at stage 1 and stage 6 of her growth. Keep her face, hairstyle and art style identical.
```

và thay đoạn STAGE 7 bằng:

```
STAGE 7 of 9 — "Office superhuman": the stage 6 body, now awakened with a first superpower. Small crackling electric-blue sparks around both fists only, kept tight to the hands. A short red scarf tied around the neck, flowing. Battle-worn sleeveless sporty version of her pink and navy outfit, lanyard ID card now showing a simple lightning bolt shape. One fist raised toward the sky, the other at her side. Determined heroic grin, eyes shining.
```

`c2-rank8.png`
```
Same character, same art style, same canvas and framing rules.

STAGE 8 of 9 — "City hero": a full superhero suit designed from her office clothes: a navy bodysuit with pale pink panels and a white blouse-collar detail at the neck, a red chest emblem shaped like a lightning bolt, white gloves, navy boots with pink trim, a long red cape. Ponytail kept. Small electric sparks around the fists only. Standing tall with both fists on her hips, cape flowing behind her. Confident heroic smile.
```

`c2-rank9.png`
```
Same character, same art style, same canvas and framing rules.

STAGE 9 of 9 — "Guardian of Earth": the ultimate form. Navy, pink and gold armored hero suit, gold shoulder guards, a round chest emblem showing a small blue-and-green planet Earth, a long deep red cape with a subtle star pattern on the inside, gold-trimmed boots and gloves, a red headband with long flying ends, ponytail flowing. Arms crossed, feet apart, calm and unbeatable expression. Remember: no big glow or aura, no background.
```

### 14c. Phản diện 21–30 (cuộc trò chuyện mới, đính kèm `original/char/rank1.png`)

Phản diện vẽ cùng phong cách và cùng khung chân dung với 20 đối thủ cũ, để thẻ đối thủ trông đồng bộ. Tất cả là nhân vật tự nghĩ ra, không giống phản diện của truyện, phim hay game nào.

`rival-21.png` — dán nguyên khối này trước
```
Create a 2D game character portrait. Square canvas 1024x1024, real transparent background (alpha channel). Do not draw a checkerboard pattern.

ART STYLE (keep identical for every image of this chat): match the art style of the attached image: clean modern anime mobile game art, crisp dark outline of even thickness, soft cel shading with two tones, bright saturated colors, slightly chibi proportions with big expressive eyes.

PORTRAIT RULES (apply to every image of this chat):
- Bust portrait: head, shoulders and upper chest only, facing the viewer, centered, filling about 85% of the canvas.
- These are original comic-book super villains who threaten planet Earth. They are menacing but still fun and colorful, suitable for all ages: no blood, no gore, no weapons pointed at the viewer.
- Each one must look clearly different from the others (silhouette, colors, outfit, expression). Some are not fully human.
- A villainous expression: evil grin, narrowed eyes or cold stare.
- No background, no frame, no ground shadow, no text, no logo.

SUBJECT: "Iron Jaw the Enforcer", a hulking underworld bodyguard about 40, buzz cut, a shiny steel jaw plate, tiny round dark sunglasses, black suit jacket stretched over huge shoulders, a thick gold chain, cracking his knuckles near his chin.
```

Các phản diện còn lại, mỗi khối một ảnh, cùng câu mở đầu `Same art style and portrait rules as the first image. SUBJECT:` rồi tới mô tả:

| File | Tên trong game | SUBJECT |
|---|---|---|
| `rival-22.png` | Bà trùm Hổ Mang | `"The Cobra Queen", an elegant underworld boss woman about 45, sleek black hair in a high bun held by two golden snake hairpins, emerald green high-collar coat with scale patterns, a small green cobra coiled on her shoulder, cold smile.` |
| `rival-23.png` | Tiến sĩ Độc Dược | `"Dr. Toxin", a mad scientist about 50, wild spiky white hair, round goggles with green lenses pushed up on his forehead, purple lab coat with stains, holding a bubbling green flask near his face, maniacal grin.` |
| `rival-24.png` | Gã Máy Xúc | `"Bulldozer the Cyborg", a giant half-machine brute, one arm replaced by a yellow construction-machine claw arm raised beside his head, orange hard hat welded to his head, one red glowing robotic eye, angry snarl.` |
| `rival-25.png` | Ông trùm Mặt Nạ Bạc | `"The Silver Mask Kingpin", the boss of the underworld, a tall man in a white tuxedo with a purple flower, face hidden behind a smooth silver mask with a thin smile carved on it, slicked-back black hair, gloved fingers pressed together.` |
| `rival-26.png` | Tướng Bão Tố | `"General Tempest", a storm villain in a dark gray military greatcoat with silver lightning-shaped epaulettes, long white hair whipping sideways in the wind, eyes glowing pale blue, a small storm cloud swirling above one hand.` |
| `rival-27.png` | Nữ hoàng Băng Giá | `"The Frost Empress", a regal ice villain woman, pale blue skin, a crown of jagged ice crystals, long silver-white hair, a high-collared white and icy blue gown, frost forming on her shoulders, haughty cold stare.` |
| `rival-28.png` | Titan Dung Nham | `"The Magma Titan", a huge humanoid made of cracked black volcanic rock with glowing orange lava in the cracks, glowing yellow eyes, small flames on top of the head like hair, roaring with the mouth open.` |
| `rival-29.png` | Siêu máy tính Omega | `"Omega the Machine Mind", a sleek chrome android head and shoulders, a transparent dome on top showing a glowing blue circuit brain, a single red horizontal visor eye, thin cables on the neck, emotionless smile.` |
| `rival-30.png` | Hắc Vương Lõi Đất | `"The Core King", the final villain of Earth, a giant demonic king from the planet's core, dark crimson skin, a crown of black rock with glowing magma gems, four short horns, a heavy black and gold armored cape collar, burning orange eyes. He must look the most powerful of all villains.` |

## Nhóm 15: Nền đấu trường (cuộc trò chuyện mới, đính kèm `original/bg/bg1.png`, 4 ảnh)

Đấu trường là màn riêng khi thách đấu: nhân vật đứng bên trái, đối thủ bên phải, khung thoại ở dưới. Thiếu ảnh thì game dùng nền màu. Lưu vào `assets/original/bg/` đúng tên dưới đây (bắt đầu bằng `bg` để `build.py` nén như ảnh nền), rồi chạy `python assets/build.py`.

### bg-arena1.png (giải 1–2: phòng họp sau giờ làm) — dán nguyên khối này trước

```
Create a 2D game background. Landscape canvas 1536x1024, fully painted, no transparency. Use the attached image as the art style reference.

ART STYLE (keep identical for every image of this chat): clean modern anime background art for a mobile game, soft cel shading, slightly muted and darker colors so that bright characters placed in front stand out. Dramatic "showdown" lighting.

LAYOUT RULES (apply to every image of this chat):
- This is an arena for a one-on-one fight: one character will stand on the left third, the other on the right third, and a dialogue box will cover the bottom 25%.
- Keep the left third and right third open and simple; the center can have a focal detail in the background.
- The floor takes up the bottom 35% and is plain and uncluttered.
- No people, no characters, no animals.
- No readable text, no logos, no brand names, no UI elements, no border.

SCENE: a large company meeting room after work hours. The long meeting table and chairs are pushed against the walls, a projector on the ceiling throws a bright empty rectangle of light on the back wall, ceiling lights are dimmed with one flickering, city lights through the blinds at night.
```

### 3 nền còn lại — dán từng khối, lưu đúng tên file

`bg-arena2.png` (giải 3–4: sàn đấu thể hình)
```
Same art style and layout rules as the first image. SCENE: a fitness competition stage in a sports hall at night: a raised square platform with a rubber floor, two strong spotlights crossing from above, dark crowd stands in the background as simple silhouettes of empty seats, blank colorful banners hanging from the ceiling, light haze in the air.
```

`bg-arena3.png` (giải 5: Thế giới ngầm)
```
Same art style and layout rules as the first image. SCENE: an abandoned underground parking garage turned into a villains' hideout: concrete pillars, purple and magenta neon tubes, piles of lazy beanbag chairs and stacked bubble tea cups at the sides, a glowing vending machine full of sugary drinks, puddles on the floor reflecting neon light.
```

`bg-arena4.png` (giải 6: Trùm Trái Đất)
```
Same art style and layout rules as the first image. SCENE: a huge cavern deep inside the Earth: rivers of glowing orange lava along the sides, dark volcanic rock, giant glowing red crystals, and far in the center background a massive empty stone throne on a rocky hill, heat shimmer and floating embers.
```

## Nhóm 16: Cửa chuyển cảnh (cuộc trò chuyện mới, đính kèm `original/bg/bg1.png`, `original/bg/bg2.png`, `original/bg/bg3.png`, 3 ảnh)

Khi chuyển màn, hai cánh cửa khép lại che cả khung rồi mở ra (xem `docs/TRANSITION_PLAN.md`). Mỗi ảnh là **một cửa đôi đang đóng, nhìn thẳng, lấp kín cả khung**; game cắt đôi ảnh theo đường giữa để làm hai cánh cửa trượt. Vì vậy khe giữa hai cánh phải nằm **đúng giữa ảnh theo chiều ngang**, và hai nửa trái phải gần như đối xứng. Biển tên nơi đến do game tự vẽ, nên ảnh **không có chữ**.

Ảnh bị cắt khác nhau theo màn hình (máy tính: cắt trên dưới; điện thoại dọc: cắt hai bên), nên tay nắm và chi tiết đẹp nhất nên nằm gần giữa ảnh. Lưu vào `assets/original/bg/` đúng tên (bắt đầu bằng `bg` để `build.py` nén như ảnh nền), rồi chạy `python assets/build.py`. Thiếu ảnh thì game dùng cửa vẽ bằng CSS.

### bg-door-gym.png (cửa phòng tập) — dán nguyên khối này trước

```
Create a 2D game image. Landscape canvas 1536x1024, fully painted, no transparency. Use the attached images as the art style reference (same game, same painter).

ART STYLE (keep identical for every image of this chat): clean modern anime background art for a mobile game, soft cel shading, warm and slightly muted colors, matching the attached backgrounds.

LAYOUT RULES (apply to every image of this chat):
- A closed double door seen straight on, filling the ENTIRE canvas edge to edge: we are standing right in front of it, so no wall, floor or ceiling is visible, only the two door leaves.
- The vertical gap where the two leaves meet is EXACTLY in the horizontal center of the image, perfectly straight and vertical.
- The left and right halves are mirror images of each other (handles, windows and panels symmetric).
- Handles sit close to the center seam, around the vertical middle of the image.
- Flat even lighting, no strong shadows across the seam, no perspective, no tilt.
- No people, no characters, no reflections of people.
- No readable text, no letters, no numbers, no logos, no signs, no UI elements, no border.

SCENE: the entrance doors of a lively neighborhood gym: two tall brushed-steel frame doors with large frosted glass panels, a horizontal black push bar on each leaf near the center, a rubber kick plate at the bottom, warm gym lights glowing softly through the frosted glass, a few faint blurred shapes of dumbbell racks behind the glass.
```

### 2 cửa còn lại — dán từng khối, lưu đúng tên file

`bg-door-home.png` (cửa nhà)
```
Same art style and layout rules as the first image. SCENE: the front door of a cozy small city apartment at evening: two warm honey-colored wooden door leaves with simple square panels, round brass knobs near the center seam, a small frosted glass window high on each leaf with soft yellow light from inside, a little worn doormat edge visible at the very bottom.
```

`bg-door-office.png` (cửa văn phòng)
```
Same art style and layout rules as the first image. SCENE: the glass entrance doors of a modern office floor in the early morning: two tall clear glass leaves with thin silver aluminum frames, long vertical steel pull handles near the center seam, a blurred bright open-plan office with desks and plants behind the glass, soft pale morning sunlight.
```

## Nhóm 11: Ảnh bìa và logo cho CrazyGames (cuộc trò chuyện mới, đính kèm `original/rank1.png`, `original/rank6.png`, `original/bg2.png`)

Không nằm trong game, chỉ dùng cho trang giới thiệu. Trước khi tải lên, xem lại kích thước và quy định về chữ trên ảnh bìa ở trang hướng dẫn nhà phát triển của CrazyGames, vì các con số dưới đây là tôi nhớ lại, chưa đối chiếu. Không cần chạy `build.py` cho nhóm này.

### cover-wide.png — ngang 16:9 (1920×1080)

```
Create a key art illustration for a 2D clicker game called "Gym God". Landscape canvas 16:9, fully painted, no transparency. Use the attached images as references: the two characters are the same man before and after training, and the background image is the art style and setting reference.

ART STYLE: clean modern anime game key art, crisp outlines, vivid cel shading, dramatic rim lighting, high contrast, eye-catching at thumbnail size.

SCENE: split composition. On the left, the weak tired office worker (first reference) slouching in a dim blue-grey office, holding a water bottle like a dumbbell. On the right, the same man transformed into the muscular confident gym god (second reference) flexing in a bright golden-lit gym, with a glowing golden aura and light rays behind him. A diagonal burst of energy and flame shapes separates the two halves. A few flames and dumbbells fly through the air.

RULES: both characters fully visible from the knees up, faces clear. Keep the top center 25% of the image calmer so a title can be placed there. No text, no letters, no logos, no UI, no border.
```

### cover-tall.png — dọc 2:3 (800×1200)

```
Same art style and same two characters as the previous image, portrait canvas 2:3. SCENE: the muscular gym god stands tall in the center flexing, glowing golden aura and light rays behind him; the weak tired office worker version of himself is smaller in the lower left corner, looking up in amazement. Gym background with flames and dumbbells flying. Keep the top 20% calmer for a title. No text, no letters, no logos, no UI, no border.
```

### cover-square.png — vuông 1:1 (800×800)

```
Same art style and same character as the previous images, square canvas 1:1. SCENE: close-up from the chest up of the muscular gym god flexing one arm with a confident grin, golden aura and light rays behind him, a flame near his fist. Very simple bold composition that is readable as a tiny thumbnail. No text, no letters, no logos, no UI, no border.
```

### logo.png — vuông 1:1 (1024×1024), nền trong suốt

```
Create a game app icon. Square canvas 1024x1024, transparent background. Clean modern anime mobile game style, thick dark outline, bright saturated colors. SUBJECT: a flexed muscular arm in a rolled-up white office shirt sleeve holding a dumbbell, with a bold orange flame behind it. Very simple bold shape, readable at 32 pixels. No text, no letters, no frame.
```

---

# Phần 4: Nhạc nền (5 bài)

Dùng với công cụ tạo nhạc AI (Suno, Udio hoặc tương tự). Kế hoạch kỹ thuật ở `docs/MUSIC_PLAN.md`.

## Cách làm

1. Bật chế độ **Instrumental** (không lời) và chế độ tự nhập phong cách (Custom) nếu công cụ có.
2. Dán khối prompt vào ô mô tả phong cách (Style). Ô lời bài hát để trống.
3. Tạo vài bản, chọn bản **ít giai điệu nổi bật nhất**: nhạc nền lặp hàng chục lần, giai điệu bắt tai sẽ gây mệt.
4. Nghe thử chỗ nối: mở bài hai lần liên tiếp, nếu đoạn cuối sang đoạn đầu bị hẫng thì tạo lại hoặc cắt bài ở cuối một ô nhịp.
5. Cắt đúng độ dài ghi trong bảng (công cụ thường cho bài 2–3 phút; cắt bằng Audacity hoặc trình cắt nhạc online), xuất **MP3 96 kbps**, đặt đúng tên, thả vào `assets/music/`.
6. Trước khi dùng, kiểm tra gói bạn đang dùng của công cụ có cho **dùng thương mại** không.

## Tên file và quy cách

| File | Phát khi | Độ dài sau khi cắt | Lặp | Nhịp |
|---|---|---|---|---|
| `office.mp3` | Màn văn phòng | 60–90 giây | Có | 70–80 BPM |
| `gym.mp3` | Màn phòng tập | 60–90 giây | Có | 125–130 BPM |
| `home.mp3` | Màn nhà | 60–90 giây | Có | 80–90 BPM |
| `duel.mp3` | 15 giây thi đấu | 16–32 giây | Có | 150–160 BPM |
| `sleep.mp3` | Chuỗi màn chờ khi đi ngủ | 9 giây | Không | Tự do |

Yêu cầu chung cho bài lặp: bắt đầu và kết thúc cùng một mức năng lượng, không có đoạn dạo đầu lặng dần hay đoạn kết nhỏ dần, không có lời, không có tiếng người.

## office.mp3 — văn phòng cuối ngày

```
Instrumental lo-fi hip hop background music for a casual mobile game. Slow and sleepy, 75 BPM. Soft dusty drum loop, warm mellow electric piano chords, gentle upright bass, faint vinyl crackle, very subtle keyboard typing and office ambience in the background. Mood: tired office worker at the end of a long workday, calm, slightly melancholic but cosy. Minimal melody, steady groove, no build-ups, no drops, seamless loop, same energy from start to finish. No vocals, no voice samples.
```

## gym.mp3 — phòng tập

```
Instrumental upbeat workout background music for a casual mobile clicker game. Energetic and motivating, 128 BPM. Punchy electronic drums with a four-on-the-floor kick, bouncy synth bass, bright plucky synth stabs, light chiptune-style arpeggio on top, hand claps. Mood: fun cartoon gym training montage, positive, driving, makes you want to tap fast. Keep it light and playful, not aggressive, not dark. Simple repetitive hook that does not get annoying, steady energy with no long breakdowns, seamless loop. No vocals, no voice samples.
```

## home.mp3 — nhà buổi tối

```
Instrumental cosy evening background music for a casual mobile game. Relaxed and warm, 85 BPM. Soft fingerpicked acoustic guitar, gentle felt piano, light brushed percussion, warm pad underneath, a hint of music-box sparkle. Mood: coming home after the gym, cooking dinner in a small apartment at night, peaceful and content. Minimal melody, soothing, steady and even, seamless loop, same energy from start to finish. No vocals, no voice samples.
```

## duel.mp3 — thi đấu

```
Instrumental intense short battle loop for a casual mobile game. Fast and exciting, 155 BPM. Driving rock drums with fast hi-hats, distorted rhythm guitar chugs, pumping synth bass, urgent brass-like synth hits, rising tension. Mood: cartoon boss fight against a rival at the gym, competitive, hyped, a race against the clock, but still fun and not scary. Starts at full energy immediately with no intro, short repeating phrase, seamless loop. No vocals, no voice samples.
```

## sleep.mp3 — đi ngủ rồi trời sáng (9 giây, không lặp)

```
Instrumental 10-second jingle for a mobile game, in two halves. First half: a soft sleepy music-box lullaby, slow and quiet, with a gentle descending melody, like falling asleep. Second half: the same melody brightens and rises with warm strings, a soft chime and a cheerful little flourish, like sunrise and waking up refreshed. Ends cleanly on a bright resolved chord. No drums, no vocals, no voice samples, no snoring sounds.
```

Bài này công cụ sẽ tạo dài hơn 10 giây. Chọn bản có đoạn ru ngủ rồi sáng lên rõ nhất, cắt lấy khoảng 9 giây: khoảng 4 giây ru ngủ, 5 giây sáng dần.

## Đợt 2: nhạc lớn lên theo hạng và đoạn nhạc thưởng (5 file)

| File | Phát khi | Độ dài sau khi cắt | Lặp | Nhịp |
|---|---|---|---|---|
| `gym2.mp3` | Phòng tập, hạng 4–6 | 60–90 giây | Có | 120–126 BPM |
| `gym3.mp3` | Phòng tập, hạng 7–9 (siêu năng lực). Không bắt buộc: thiếu thì dùng `gym2` | 60–90 giây | Có | 132–138 BPM |
| `rankup.mp3` | Lên hạng, lên đời | 2–3 giây | Không | Tự do |
| `win.mp3` | Thắng trận | 3–4 giây | Không | Tự do |
| `lose.mp3` | Thua trận | 2–3 giây | Không | Tự do |

### Cách để nhạc nghe tự nhiên, bớt "chất AI"

Nhạc AI dễ lộ khi prompt chung chung ("epic, uplifting, motivational"): công cụ sẽ trả về loại nhạc stock nhiều lớp synth, nén chặt, mọi thứ đều to và hoàn hảo. Prompt dưới đây đi theo hướng ngược lại:

- **Ban nhạc nhỏ, nhạc cụ thật, gọi tên cụ thể** (trống jazz, bass điện, kèn trumpet có tắt tiếng…) thay cho "synth", "pad", "orchestral".
- **Mô tả cách thu âm**: thu sống trong một phòng, nghe được không gian phòng, nhạc công chơi cùng lúc, nhịp hơi lệch theo kiểu người chơi, mix khô, không nén chặt.
- **Ô loại trừ** (Exclude styles của Suno, hoặc thêm vào cuối prompt với công cụ khác), dán cho mọi bài:

```
EDM, synth pad, supersaw, cinematic, epic trailer, orchestral hybrid, dubstep, drop, riser, autotune, vocals, choir, heavy sidechain, stock music
```

Khi nghe chọn bản, bỏ những bản có: tiếng "xì xào" kim loại ở dải cao (dấu hiệu AI rõ nhất), nhạc cụ đổi âm sắc giữa chừng, giai điệu lang thang không về chủ âm, đoạn sau to hơn hẳn đoạn đầu. Ưu tiên bản nghe như một ban nhạc thật chơi trong phòng, có chút "thô".

Đoạn ngắn (rankup, win, lose): công cụ không tạo được bài 3 giây. Cách làm: tạo bài bình thường (30 giây trở lên), chọn bản **mở đầu** bằng đúng câu nhạc đó, cắt lấy vài giây đầu, làm nhỏ dần 0,3 giây cuối cho khỏi bị cụt. Nếu câu hay nằm ở **đoạn kết** thì cắt đoạn kết.

### gym2.mp3 — phòng tập, hạng 4–6

```
Instrumental live funk band groove, background music for a cartoon gym game. 124 BPM. Real drum kit played by a human, tight snare with ghost notes, open hi-hat, round electric bass with slap accents, clean rhythm guitar with wah pedal, short three-piece horn section stabs (trumpet, tenor sax, trombone), a little Hammond organ. Recorded live in a small room, warm analog tape sound, dry mix, natural dynamics, slight human timing. Mood: confident, sweaty, grinning, getting stronger. Steady groove, no solos, no build-ups, same energy from start to finish, seamless loop. No vocals.
```

Khác `gym.mp3` (điện tử, vui nhộn) ở chỗ "lớn lên": ban nhạc thật, dày và chắc tay hơn nhưng không ồn hơn. Hạng 4–6 là lúc nhân vật bắt đầu có cơ bắp.

### gym3.mp3 — phòng tập, hạng 7–9 (không bắt buộc)

```
Instrumental 1970s superhero TV show theme style groove, background music for a cartoon gym game. 135 BPM. Live drum kit with big tom fills, driving electric bass, crunchy overdriven electric guitar riff, bold brass section playing short heroic stabs, timpani hits on the downbeat now and then. Recorded live by a real band in a studio room, analog warmth, natural reverb, dynamic, not compressed. Mood: heroic and a bit over the top, the hero has superpowers now, still fun and playful. Short repeating riff, no long melody, no solos, same energy throughout, seamless loop. No vocals.
```

### rankup.mp3 — lên hạng (2–3 giây)

```
Instrumental short triumphant fanfare played by a real brass ensemble: trumpets, French horns and trombones, with a snare drum roll and one big crash cymbal on the final chord. Recorded live in a concert hall, natural room reverb, warm and bright, slightly imperfect human playing. Opens immediately with a rising three-note fanfare that lands on a big major chord, like a hero levelling up in a cartoon. No synth, no vocals.
```

Cắt từ đầu bài tới hết hợp âm lớn đầu tiên (cho tiếng ngân tự tắt hoặc làm nhỏ dần). Không nên dài quá 3 giây: lên hạng còn có thông báo và rung màn hình chạy cùng lúc.

### win.mp3 — thắng trận (3–4 giây)

```
Instrumental short victory jingle played by a live small band: punchy brass section, electric guitar, bass and drum kit. Upbeat, celebratory and a little cheeky, like winning a cartoon boxing match. Opens straight away with a bright brass melody of four or five notes, a drum fill, and ends on a strong final hit with cymbal crash. Recorded live in a room, natural and warm, human timing. No synth, no vocals, no crowd.
```

Nên khác `rankup` một chút (có trống và guitar, vui hơn, ít trang trọng hơn), để người chơi phân biệt "thắng trận" với "lên hạng".

### lose.mp3 — thua trận (2–3 giây)

```
Instrumental short comedic fail jingle: a muted trombone plays a slow descending "wah wah wah" phrase, with a soft tuba note and a quiet brushed snare at the end. Recorded live, natural room sound, playful and gentle, cartoon style, a funny "better luck next time" feeling, not sad, not dramatic. No synth, no vocals.
```

Thua là chuyện thường gặp (người chơi thách đấu lại nhiều lần) nên tiếng thua phải **nhẹ và hài**, không làm nản.

### Sau khi có file

Thả vào `assets/music/` đúng tên, báo lại để nối vào game: chọn bài phòng tập theo hạng, đoạn thưởng phát thay cho tiếng bíp `sfx.up` / `sfx.lose` (thiếu file thì vẫn dùng tiếng bíp như hiện tại), đi theo nấc **Âm thanh** chứ không theo nấc Nhạc.


# Phần 5: Hiệu ứng âm thanh và giọng bập bẹ (khách ghé phòng tập)

Mục tiêu: khách ghé (PT, Crush, bánh sinh nhật) có tiếng riêng **lúc xuất hiện** để người chơi để ý dù đang nhìn nhân vật, và có giọng kêu ngắn cho có hồn. Tiếng "vút" và "tích" của vòng PERFECT sẽ làm bằng code (cần khớp thời gian tới từng mili giây), không cần file.

## Công cụ

Dùng công cụ tạo **hiệu ứng âm thanh** từ chữ (ví dụ ElevenLabs Sound Effects, Stable Audio), không dùng công cụ tạo nhạc (Suno, Udio làm tiếng ngắn rất kém). Nếu công cụ có ô độ dài, đặt đúng số giây ghi ở từng khối. Nếu có thanh "bám sát prompt" (prompt influence), kéo lên cao. Trước khi dùng, kiểm tra gói đang dùng có cho **dùng thương mại** không.

Nguồn khác nếu AI làm chưa ưng: thư viện âm thanh CC0 (miễn phí, không cần ghi công). Tiếng còi và kèn tiệc tìm thư viện thường được bản thật hơn AI.

## Nguyên tắc để giọng nghe thật, không "chất AI"

- **Không có câu nói thật.** Chỉ tiếng kêu, tiếng cười, "hey", "hup", "hmph": game song ngữ, và một câu thật nghe lần thứ 50 sẽ rất phiền.
- **Ngắn**: giọng 0,3–0,8 giây. Dài hơn là bắt đầu lộ giọng máy.
- **Thu khô, sát micro**: không vang, không nhạc nền, không tiếng ồn phòng. Game tự trộn với nhạc.
- **Mỗi loại 2–3 biến thể** khác nhau rõ (khác cao độ, khác cảm xúc), game sẽ phát ngẫu nhiên.
- **Khi chọn bản, bỏ những bản có**: tiếng méo kim loại ở cuối, hai giọng chồng nhau, giọng "đọc" như máy đọc, có nhạc hoặc tiếng vang phía sau. Ưu tiên bản nghe như diễn viên lồng tiếng hoạt hình thu một câu ngẫu hứng.

## Tên file và quy cách

| File | Phát khi | Độ dài | Ghi chú |
|---|---|---|---|
| `pt-whistle` | PT xuất hiện | 0,4–0,6 giây | Một tiếng còi, phát cùng giọng PT |
| `pt-1`, `pt-2`, `pt-3` | PT xuất hiện | 0,3–0,7 giây | Giọng huấn luyện viên |
| `crush-1`, `crush-2`, `crush-3` | Crush đi ngang | 0,4–0,8 giây | Giọng chào nhẹ |
| `crush-yes-1`, `crush-yes-2` | Crush đồng ý | 0,5–1 giây | Cười khúc khích vui |
| `crush-no-1`, `crush-no-2` | Crush ngó lơ | 0,4–0,8 giây | "Hừm" tinh nghịch, không gắt |
| `cake-1`, `cake-2` | Bánh sinh nhật xuất hiện | 0,5–1 giây | Kèn tiệc thổi |
| *(không bắt buộc)* `hero-m-1..3`, `hero-f-1..3` | Bấm trúng PERFECT từ chuỗi x3 | 0,2–0,4 giây | Tiếng gắng sức của nhân vật nam / nữ |

Thả file vào `assets/original/sfx/` (WAV hoặc MP3 đều được), đúng tên, báo lại để đổi sang MP3 vào `assets/sfx/` và nối vào game. Cả bộ chỉ khoảng 150–250 KB.

Âm lượng không cần cân tay: game tự cân theo độ to thật của từng file, giống nhạc nền.

## pt-whistle — còi huấn luyện viên (0,5 giây)

```
A single short sharp blast on a referee's pea whistle, like a gym coach calling attention. One blast only, about half a second, natural breathy attack with the pea rattling. Dry close-mic recording, no reverb, no background noise, no music.
```

## pt-1, pt-2, pt-3 — giọng PT (mỗi khối tạo riêng)

```
pt-1: A cheerful muscular male fitness coach, around 30, shouts a short energetic "Hey!" to get someone's attention, big friendly smile in his voice. One word only, under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

```
pt-2: A cheerful muscular male fitness coach, around 30, gives a short punchy motivating grunt "Hup!" like clapping his hands to start a workout. One syllable only, under half a second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

```
pt-3: A cheerful muscular male fitness coach, around 30, lets out a short excited "Yeah!" with a little laugh, hyping someone up. Under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

## crush-1, crush-2, crush-3 — Crush đi ngang (mỗi khối tạo riêng)

```
crush-1: A sweet young woman, around 25, says a soft shy "Hi~" with a light rising tone, as if waving at someone she likes across the gym. One word only, under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

```
crush-2: A sweet young woman, around 25, makes a short curious playful "Hmm?" humming sound, smiling. Under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

```
crush-3: A sweet young woman, around 25, gives a tiny soft giggle, shy and cute, just two or three short notes of laughter. Under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

## crush-yes-1, crush-yes-2 — Crush đồng ý

```
crush-yes-1: A sweet young woman, around 25, laughs happily and brightly, a short delighted giggle, like someone just made her smile. About one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

```
crush-yes-2: A sweet young woman, around 25, says a short pleased "Ooh!" with a smile, pleasantly surprised and impressed. Under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

## crush-no-1, crush-no-2 — Crush ngó lơ

```
crush-no-1: A young woman, around 25, makes a short playful "Hmph!" and turns away, teasing rather than angry, a hint of a smile. Under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

```
crush-no-2: A young woman, around 25, gives a short unimpressed "Mm-mm" with closed lips, playfully saying no. Under one second. Dry close-mic voice recording, no reverb, no music, no background noise.
```

## cake-1, cake-2 — kèn tiệc sinh nhật

```
cake-1: A single paper party horn blower being blown once, the curled paper unrolling with a buzzy kazoo-like "prrrt" toot. Short and funny, under one second. Dry close-mic recording, no reverb, no music, no people.
```

```
cake-2: Two quick toots on a paper party horn blower, cheerful and silly, like a small office birthday surprise. About one second. Dry close-mic recording, no reverb, no music, no people.
```

## hero-m / hero-f — tiếng gắng sức khi PERFECT (không bắt buộc)

Chỉ phát khi chuỗi PERFECT từ x3 trở lên, nên không bị lặp dày. Nếu nghe thử thấy phiền, bỏ hẳn: tiếng "tích" tăng cao độ đã đủ.

```
hero-m-1: A young office man straining while lifting a dumbbell, a short effort grunt "hngh!", determined, slightly comedic. Under half a second. Dry close-mic voice recording, no reverb, no music.
```

```
hero-m-2: A young office man pushing hard through one more rep, a short sharp exhale "hah!", proud. Under half a second. Dry close-mic voice recording, no reverb, no music.
```

```
hero-m-3: A young office man finishing a heavy lift, a short satisfied "hup!", energetic. Under half a second. Dry close-mic voice recording, no reverb, no music.
```

Bản nữ (`hero-f-1..3`): dùng lại ba khối trên, đổi `A young office man` thành `A young office woman`.
