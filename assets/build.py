"""Nén ảnh gốc trong assets/original/<nhóm>/*.png thành assets/<nhóm>/*.webp cho game (chạy: python assets/build.py).
Nhóm: char, bg, icon, pet, rival, food, scene, ui. Thư mục original/store (ảnh bìa, logo) chỉ dùng cho trang đăng game nên bỏ qua.
Icon nào bị vẽ dính nền ô caro giả (ảnh RGB không có kênh trong suốt) thì tự tách nền."""
import glob, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'original')


def cut_fake_checker(im):
    """Nền ô caro giả = trắng xen xám nhạt (~230) hoàn toàn không màu. Xoá mọi vùng sáng liền nhau
    mà phần xám của nó đúng tông ô caro; áo trắng có bóng ngả tím nên được giữ."""
    a = np.array(im.convert('RGB')).astype(int)
    lo, hi = a.min(2), a.max(2)
    bg = (hi - lo < 12) & (lo >= 222)
    gray = bg & (lo < 240)
    edge = np.zeros(bg.shape, bool)
    edge[:8] = edge[-8:] = edge[:, :8] = edge[:, -8:] = True
    tone = np.bincount(lo[edge & gray]).argmax()                 # tông xám của ô caro, đo ở viền ảnh
    exact = gray & (hi - lo <= 3) & (abs(lo - tone) <= 3)        # bóng trên áo trắng không bao giờ xám tuyệt đối như vậy
    m = Image.fromarray(bg.astype(np.uint8) * 255)
    cut = np.zeros(bg.shape, bool)
    while True:   # duyệt từng vùng liền nhau
        rest = np.argwhere(np.array(m) == 255)
        if not len(rest):
            break
        y, x = rest[0]
        ImageDraw.floodfill(m, (int(x), int(y)), 200)
        comp = np.array(m) == 200
        if comp.sum() > 400 and exact[comp].sum() > 0.4 * max(gray[comp].sum(), 1) and gray[comp].mean() > 0.2:
            cut |= comp
        m.paste(0, mask=Image.fromarray(comp))
    cut = Image.fromarray(cut.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(5))  # ăn thêm viền sáng
    out = im.convert('RGBA')
    out.putalpha(Image.fromarray(255 - np.array(cut)))
    return out


def cut_bg(im):
    """Ảnh RGB không có kênh trong suốt: nền đen đặc thì tô loang từ 4 góc, còn lại coi là ô caro giả."""
    im = im.convert('RGB')
    if max(im.getpixel((2, 2))) > 12:
        return cut_fake_checker(im)
    m = im.copy()
    seeds = [(0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)]
    dark = Image.fromarray(((np.array(im).max(2) <= 3) * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(41))
    seeds += [(int(x), int(y)) for y, x in np.argwhere(np.array(dark) == 255)[::200]]   # mảng đen tuyệt đối rộng nằm kín giữa nhân vật (vd. giữa hai cánh tay)
    for xy in seeds:
        if m.getpixel(xy) != (255, 0, 255):
            ImageDraw.floodfill(m, xy, (255, 0, 255), thresh=14)   # nét viền nhân vật là nâu sẫm chứ không đen tuyệt đối nên không bị loang vào
    a = np.array(m)
    cut = (a[..., 0] == 255) & (a[..., 1] == 0) & (a[..., 2] == 255)
    cut = Image.fromarray(cut.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(3))
    out = im.convert('RGBA')
    out.putalpha(Image.fromarray(255 - np.array(cut)))
    return out


def save(im, name, **kw):
    os.makedirs(os.path.join(HERE, sub), exist_ok=True)
    path = os.path.join(HERE, sub, name + '.webp')
    im.save(path, 'WEBP', method=6, **kw)
    print(f'{sub}/{name}.webp  {im.size}  {os.path.getsize(path) // 1024} KB')


for f in sorted(glob.glob(os.path.join(SRC, '*', '*.png'))):
    name = os.path.splitext(os.path.basename(f))[0]
    sub = os.path.basename(os.path.dirname(f))
    if sub == 'store':
        continue
    im = Image.open(f)
    if name.startswith('bg'):
        save(im.convert('RGB'), name, quality=82)
    elif 'rank' in name:   # rank1.. và c2-rank1..: giữ nguyên khung để nhân vật không nhảy vị trí giữa các hạng
        im = im.convert('RGBA') if im.mode == 'RGBA' else cut_bg(im)
        save(im.resize((683, 1024), Image.LANCZOS), name, quality=88)
    elif name.startswith(('icon', 'pet', 'rival', 'food', 'ui', 'tab', 'scene')):
        im = im.convert('RGBA') if im.mode == 'RGBA' else cut_bg(im)
        im = im.crop(im.getchannel('A').getbbox())
        side = max(im.size)
        sq = Image.new('RGBA', (side, side))
        sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
        px = 384 if sub in ('rival', 'scene') else 96 if sub == 'ui' else 192   # đối thủ hiện to ở màn đấu, scene ở màn chờ; icon giao diện rất nhỏ
        save(sq.resize((px, px), Image.LANCZOS), name, quality=90)
