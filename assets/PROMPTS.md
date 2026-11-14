# Bộ prompt tạo ảnh cho Gym God (dùng với ChatGPT)

Prompt viết bằng tiếng Anh vì công cụ tạo ảnh hiểu tiếng Anh chính xác hơn. Bạn chỉ cần sao chép từng khối và dán.

## Cách làm

1. Mở **một cuộc trò chuyện mới** cho mỗi nhóm ảnh (nhân vật / nền / icon). Không trộn các nhóm.
2. Dán prompt số 1 của nhóm. Tạo lại cho đến khi ưng ý, vì ảnh đầu tiên quyết định phong cách cho cả nhóm.
3. Dán lần lượt các prompt tiếp theo **trong cùng cuộc trò chuyện đó** để giữ đúng nhân vật và nét vẽ.
4. Nếu nhân vật bị lệch (khác mặt, khác tóc), đính kèm lại ảnh `rank1.png` và viết thêm: `Use the attached image as the character reference.`
5. Tải ảnh về, đổi tên đúng như bảng dưới, thả vào thư mục `assets/original`.
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

# Phần 3: Màn nhà và món ăn

Lưu vào `assets/original/` đúng tên file, rồi chạy `python assets/build.py`. Đính kèm `original/bg1.png` làm ảnh tham chiếu phong cách cho nền, và một icon bài tập bất kỳ (ví dụ `original/icon-tay.png`) cho món ăn.

## `bg3.png` — nền nhà buổi tối (ngang 3:2, 1536x1024)

```
Anime-style 2D game background, same art style, line weight and colour palette as the attached reference image. A small, cosy modern apartment at night: living room on the left with a sofa, a low table and a TV, an open kitchenette on the right with a fridge, a rice cooker and a small dining table. Warm yellow lamp light, city lights visible through a window, a yoga mat rolled up in a corner, a pair of dumbbells on the floor. The centre of the floor is empty and clear so a character can stand there. No people, no text, no logos, no UI. Landscape 3:2.
```

## Ba món ăn (vuông 1:1, nền trong suốt)

Phần chung, dán trước mỗi prompt:

```
Game icon, chunky cartoon style with thick dark outlines, same style as the attached reference icon. Single object centred, slight 3/4 top-down view, soft shading, transparent background, no text, no border, no shadow on the ground. Square 1:1.
```

- `food-healthy.png`: `A healthy meal tray: a bowl of white rice, sliced boiled chicken breast, steamed green vegetables and a small bowl of clear soup.`
- `food-protein.png`: `A high-protein meal: grilled chicken breast, two boiled eggs cut in half, and a shaker bottle of whey protein next to the plate.`
- `food-junk.png`: `A junk food combo: a tall cup of bubble milk tea with tapioca pearls and a straw, next to a paper bucket of crispy fried chicken.`
