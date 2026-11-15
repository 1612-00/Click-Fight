"""Đóng gói bản upload CrazyGames: python tools/dist.py
Chỉ lấy những gì game tải: index.html và ảnh/nhạc đã build trong assets/<nhóm>/ (webp, mp3).
Bỏ hết ảnh gốc (assets/original, hơn 160 MB), .git, tools, docs, prototype.
Ra dist/gym-god/ (thư mục) và dist/gym-god.zip (file để upload)."""
import os, re, shutil, sys, zipfile

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'dist', 'gym-god')
ZIP = OUT + '.zip'
KEEP = ('.webp', '.mp3')

html = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
groups = sorted(set(re.findall(r'assets/([a-z]+)/', html)) - {'original'})   # thư mục game thật sự dùng

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
shutil.copy2(os.path.join(ROOT, 'index.html'), OUT)
files = ['index.html']
for g in groups:
    for f in sorted(os.listdir(os.path.join(ROOT, 'assets', g))):
        if f.endswith(KEEP):
            os.makedirs(os.path.join(OUT, 'assets', g), exist_ok=True)
            shutil.copy2(os.path.join(ROOT, 'assets', g, f), os.path.join(OUT, 'assets', g, f))
            files.append(f'assets/{g}/{f}')

with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(os.path.join(OUT, f), f)   # index.html nằm ở gốc file zip

size = sum(os.path.getsize(os.path.join(OUT, f)) for f in files)
print(f'{len(files)} file, {size / 1e6:.1f} MB ({", ".join(groups)})')
print(f'Upload: {os.path.relpath(ZIP, ROOT)} ({os.path.getsize(ZIP) / 1e6:.1f} MB)')
assert size < 20e6, 'Quá 20 MB: CrazyGames sẽ không đưa game lên trang chủ điện thoại'
