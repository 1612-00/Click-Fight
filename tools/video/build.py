"""Ghép video xem trước cho CrazyGames: python tools/video/build.py

Đầu vào: các đoạn quay trong tools/video/raw do tools/video/record.js tạo (tên file: <hướng>_<cảnh>_<ms bắt đầu>_<ms kết thúc>.webm).
Đầu ra: assets/original/store/video-landscape.mp4 (1920x1080) và video-portrait.mp4 (1080x1620).
Luật CrazyGames: 15-20 giây, tối đa 50 MB, không tiếng, không tua nhanh, khung đầu là ảnh bìa, không màn hình đen, không con trỏ chuột.

Quay ở 1280x720 / 720x1080 (cỡ người chơi thường thấy; 720 rộng thì ra bố cục điện thoại) rồi phóng 1,5 lần,
vì Playwright quay theo pixel CSS, không theo deviceScaleFactor.
Playwright cần ffmpeg ở %LOCALAPPDATA%/ms-playwright/ffmpeg-1013/ffmpeg-win64.exe: chép ffmpeg của máy vào đó là chạy.
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
STORE = HERE.parent.parent / 'assets' / 'original' / 'store'
# (cảnh, mốc, giây lệch, mốc, giây lệch): mốc 's' = lúc bắt đầu thao tác, 'e' = lúc kết thúc. Video sớm hơn mốc khoảng 0,15 giây.
PLAN = [('a', 's', 0.05, 's', 4.65),      # bấm tập, mua Ngực, LỘT XÁC
        ('b', 's', 0.15, 's', 4.55),      # thi đấu Hank the Guard, thắng
        ('c', 's', 0.10, 's', 2.25),      # chọn bữa tối, bấm Đi ngủ (Zzz); màn chờ tối bắt đầu ở s+1,6
        ('c', 'e', -0.72, 'e', 0.70),     # sáng hôm sau ở văn phòng "Day 10" (bỏ các màn chờ tối ở giữa)
        ('d', 's', 0.10, 's', 3.60)]      # thần gym bấm ra số lớn
OUT = {'land': (1920, 1080, 'cover-wide.png', 'video-landscape.mp4'), 'port': (1080, 1620, 'cover-tall.png', 'video-portrait.mp4')}


def latest(o, scene):   # đoạn quay mới nhất của cảnh
    files = sorted((HERE / 'raw').glob(f'{o}_{scene}_*.webm'), key=lambda f: f.stat().st_mtime)
    if not files: raise SystemExit(f'Thiếu đoạn quay {o}_{scene}: chạy tools/video/record.js trước')
    _, _, st, en = files[-1].stem.split('_')
    return files[-1], int(st) / 1000, int(en) / 1000


def build(o):
    w, h, cover, name = OUT[o]
    args = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', '1', '-i', str(STORE / cover)]
    flt = [f'[0:v]scale={w}:{h}:flags=lanczos,setsar=1,fps=30,format=yuv420p[v0]']
    for i, (scene, a, da, b, db) in enumerate(PLAN, 1):
        f, st, en = latest(o, scene)
        t0, t1 = (st if a == 's' else en) + da, (st if b == 's' else en) + db
        args += ['-ss', f'{t0:.3f}', '-t', f'{t1 - t0:.3f}', '-i', str(f)]
        flt.append(f'[{i}:v]setpts=PTS-STARTPTS,scale={w}:{h}:flags=lanczos,setsar=1,fps=30,format=yuv420p[v{i}]')
    n = len(PLAN) + 1
    flt.append(''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[out]')
    out = STORE / name
    subprocess.run(args + ['-filter_complex', ';'.join(flt), '-map', '[out]', '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18',
                           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out)], check=True)
    sec = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(out)], capture_output=True, text=True).stdout)
    mb = out.stat().st_size / 2**20
    assert 15 <= sec <= 20 and mb < 50, (sec, mb)
    print(f'{out.name}: {w}x{h}, {sec:.1f} giây, {mb:.1f} MB')


if __name__ == '__main__':
    for o in OUT: build(o)
