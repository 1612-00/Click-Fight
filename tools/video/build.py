"""Dựng video CrazyGames và các bản có tiếng từ các cảnh đã quay."""

import json
import os
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
RAW = HERE / 'raw'
ASSETS = HERE.parent.parent / 'assets'
STORE = ASSETS / 'original' / 'store'
FONT = Path(os.environ.get('GYM_GOD_VIDEO_FONT', 'C:/Windows/Fonts/segoeuib.ttf'))
LANDSCAPE_COVER = 'cover-1920x1080.png'
LANDSCAPE_SOUND = 'video-landscape-with-sound.mp4'


def take(scene, start, end, caption=''):
    assert 0 <= start < end <= scene['end'], (scene['file'], start, end)
    return RAW / scene['file'], start, end - start, caption


def timeline(scenes, cover=None):
    workout, arena, champion = (scenes[key] for key in ('workout', 'arena', 'champion'))
    start = workout['start'] + .05
    cut = workout['rankUp'] + .1
    battle = [
        take(arena, arena['versus'] + .29, arena['versus'] + 1.23, 'THE ACCOUNTANT'),
        take(arena, arena['fight'] + .1, arena['end'] - .08, 'WIN YOUR FIRST DUEL'),
    ]
    gym_god = take(champion, champion['start'] + .23, champion['end'] - .12, 'HOW FAR CAN YOU GO?')
    if cover:
        return [
            (STORE / cover, 0, 1, ''),
            take(workout, start, workout['end'] - .12),
            *battle,
            gym_god,
        ]
    return [
        take(champion, champion['start'] + .55, champion['start'] + 1.73, 'AFTER HOURS'),
        take(workout, start, cut, 'TAP TO TRAIN'),
        take(workout, cut, workout['end'] - .12, 'LEVEL UP'),
        *battle,
        gym_god,
    ]


def social_layout():
    labels = [
        'pad=1080:1920:72:242:color=0x18291F',
        'drawtext=fontfile=segoe.ttf:text=FROM DESK TO:fontsize=48:fontcolor=0xF0C16B:x=72:y=56',
        'drawtext=fontfile=segoe.ttf:text=GYM GOD:fontsize=100:fontcolor=0xF8F2E5:x=68:y=104',
        'drawbox=x=72:y=222:w=110:h=5:color=0xE6AF55:t=fill',
    ]
    return ','.join(labels)


def sound_cues(scenes, clips):
    events = {
        'rankup': (scenes['workout'], scenes['workout']['rankUp'] + .1),
        'win': (scenes['arena'], scenes['arena']['win']),
    }
    cues = {}
    position = 0
    for file, start, duration, _ in clips:
        for name, (scene, moment) in events.items():
            if file == RAW / scene['file'] and start <= moment < start + duration:
                cues[name] = position + moment - start
        position += duration
    assert cues.keys() == events.keys(), cues
    return cues


def mix_audio(first_input, duration, cues):
    inputs = ['-i', str(ASSETS / 'music/gym.mp3')]
    filters = [
        f'[{first_input}:a]atrim=duration={duration:.3f},asetpts=PTS-STARTPTS,loudnorm=I=-19:TP=-2:LRA=8,'
        f'aresample=48000,aformat=channel_layouts=stereo,afade=d=0.18,'
        f'afade=t=out:st={duration - .55:.3f}:d=0.55[music]'
    ]
    for i, (name, cue) in enumerate(cues.items(), first_input + 1):
        inputs += ['-i', str(ASSETS / f'music/{name}.mp3')]
        filters.append(
            f'[{i}:a]atrim=duration=1.75,asetpts=PTS-STARTPTS,loudnorm=I=-15:TP=-2:LRA=8,'
            f'aresample=48000,aformat=channel_layouts=stereo,afade=t=out:st=1.1:d=0.65,'
            f'adelay={round(cue * 1000)}:all=1[{name}]'
        )
    filters.append('[music][rankup][win]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.89:level=0[a]')
    return inputs, filters


def build(scenes, size, out, cover=None):
    social = cover is None
    clips = timeline(scenes, cover)
    w, h = size
    args = ['ffmpeg', '-v', 'error', '-y', '-filter_complex_threads', '2']
    filters = []
    duration_total = sum(clip[2] for clip in clips)
    for i, (file, start, duration, caption) in enumerate(clips):
        if file.suffix == '.png':
            args += ['-loop', '1', '-framerate', '30', '-t', f'{duration:.3f}', '-i', str(file)]
        else:
            args += ['-ss', f'{start:.3f}', '-t', f'{duration:.3f}', '-i', str(file)]
        frame_w, frame_h = (936, 1404) if social else (w, h)
        part = f'[{i}:v]setpts=PTS-STARTPTS,scale={frame_w}:{frame_h}:flags=lanczos,setsar=1,fps=30'
        if social:
            part += ',' + social_layout()
            part += (f",drawtext=fontfile=segoe.ttf:text='{caption}':fontsize=46:"
                     'fontcolor=0xF8F2E5:x=72:y=1690')
        filters.append(part + f',format=yuv420p[v{i}]')

    filters.append(''.join(f'[v{i}]' for i in range(len(clips))) + f'concat=n={len(clips)}:v=1:a=0[v]')
    options = ['-map', '[v]', '-an']
    if social:
        inputs, audio_filters = mix_audio(len(clips), duration_total, sound_cues(scenes, clips))
        args.extend(inputs)
        filters.extend(audio_filters)
        options = ['-map', '[v]', '-map', '[a]', '-c:a', 'aac', '-b:a', '192k', '-shortest']
    subprocess.run(args + ['-filter_complex', ';'.join(filters), *options,
                           '-c:v', 'libx264', '-threads', '4', '-preset', 'medium', '-crf', '18',
                           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out)],
                   check=True, cwd=out.parent)


def probe(file):
    return json.loads(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(file)]))


def add_landscape_sound(source, out, scenes):
    duration = float(probe(source)['format']['duration'])
    clips = timeline(scenes, LANDSCAPE_COVER)
    inputs, filters = mix_audio(1, duration, sound_cues(scenes, clips))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(source), *inputs,
                    '-filter_complex', ';'.join(filters), '-map', '0:v:0', '-map', '[a]',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest',
                    '-movflags', '+faststart', str(out)], check=True)


def verify(out, size, with_audio):
    data = probe(out)
    video = [s for s in data['streams'] if s['codec_type'] == 'video']
    audio = [s for s in data['streams'] if s['codec_type'] == 'audio']
    sec = float(data['format']['duration'])
    assert len(video) == 1 and (video[0]['width'], video[0]['height']) == size
    assert len(audio) == int(with_audio)
    assert 15 <= sec <= 20 and out.stat().st_size < 50_000_000, (out.name, sec, out.stat().st_size)
    print(f'{out.name}: {size[0]}x{size[1]}, {sec:.2f}s, {out.stat().st_size / 1_000_000:.1f} MB', flush=True)


def main():
    manifest = json.loads((RAW / 'trailer-marks.json').read_text(encoding='utf-8'))
    staging = Path(tempfile.mkdtemp(prefix='export-', dir=RAW))
    (staging / 'segoe.ttf').write_bytes(FONT.read_bytes())
    outputs = [
        ('land', (1920, 1080), LANDSCAPE_COVER, 'video-landscape.mp4'),
        ('port', (1080, 1620), 'cover-800x1200.png', 'video-portrait.mp4'),
        ('port', (1080, 1920), None, 'video-social.mp4'),
    ]
    for orientation, size, cover, name in outputs:
        out = staging / name
        build(manifest[orientation], size, out, cover)
        verify(out, size, with_audio=cover is None)
    add_landscape_sound(staging / 'video-landscape.mp4', staging / LANDSCAPE_SOUND, manifest['land'])
    verify(staging / LANDSCAPE_SOUND, (1920, 1080), with_audio=True)
    for name in [output[3] for output in outputs] + [LANDSCAPE_SOUND]:
        (staging / name).replace(STORE / name)
    (staging / 'segoe.ttf').unlink()
    staging.rmdir()


if __name__ == '__main__':
    main()
