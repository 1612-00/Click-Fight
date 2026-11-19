"""Mô phỏng nhịp chơi theo ngày trong game: python tools/sim.py
In ra ngày và tổng thời gian chơi khi đạt từng hạng, với ba kiểu nghỉ: không bao giờ nghỉ / nghỉ khi Mỏi (>=40) / nghỉ khi Kiệt sức (>=70).
Người chơi bấm CPS lần/giây cho tới khi hết thể lực, mua thứ còn thiếu mục tiêu (rẻ nhất trước), thách đấu khi thắng được, tối ăn cơm gà.
Các số trong G phải khớp với index.html (EX, RANKS, R, MS, KG, KG_LOSS, FAT, WK, staMax, target, prize, summonCost, MEALS)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
EX = [(15, 1, 0), (100, 0, 1), (1100, 0, 8), (12000, 0, 47), (40000, 12, 0), (130000, 0, 260), (1400000, 0, 1400), (20000000, 0, 7800)]  # giá, +bấm, +giây
MS = [25, 50, 100]
CPS = 4
IDLE = 30   # giây mỗi ngày không bấm: văn phòng, mua bài tập, ở nhà
G = dict(goals=[[0] * 8, [5, 4, 2, 0, 0, 0, 0, 0], [12, 10, 5, 1, 0, 0, 0, 0], [22, 18, 14, 8, 3, 0, 0, 0], [40, 35, 30, 22, 15, 10, 3, 0], [70, 60, 55, 48, 40, 40, 32, 20],
               [85, 75, 70, 64, 55, 55, 45, 32], [100, 92, 88, 80, 70, 70, 60, 44], [120, 112, 106, 98, 88, 86, 76, 58]],   # hạng 7–9
         mults=[1.25, 1.5, 1.75, 2, 2.5, 3, 3.5, 4, 5], R=1.17,
         kg=[999, 999, 999, 84.5, 82, 78, 76, 74, 72], kg_loss=[.3, .3, .3, .4, .5, .6, .7, .8, .9],
         fat=[40, 40, 40, 40, 40, 40, 40, 40, 40], wk=[4, 4, 5, 5, 6, 6, 6, 6, 6], sta0=300, sta_rank=120, sta_cardio=5,   # kg_loss: cân giảm khi dùng đủ thể lực; mệt mỏi cộng đều, thể lực +sta_rank mỗi hạng tới hạng 6
         duel=15, t0=300, tg=2.4, prize=3, win=.03, rivals=30, duel_sta=40, tg2=1.25,   # tg2: phản diện 21–30 chỉ khó hơn x1,25 mỗi người
         s0=5000, sg=2.5, pet=.042, ach=.01, tap=.25,   # tap: mỗi cú bấm thêm tap x calo/giây gốc
         pt=1, pt_day=3, pt_gap=60, pt_life=8, pt_tap=5, pt_sta=.3, pt_cps=60, pt_taps=30,   # khách ghé phòng tập (index.html: PT); pt = tỉ lệ bấm kịp
         kg0=85, night=0, hands=0, fee=1,   # hands: thử thách Chỉ dùng tay; fee: hệ số giá bài tập (Phòng gym tăng giá)   # cân lúc bắt đầu (lên đời giữ cân nặng), cân cộng thêm mỗi tối
         cr_tap=7, cr_sec=10, cr_cal=2, cr_lose=.1, ck_cal=1.5, ck_kg=.1,
         rep_every=30, rep_p=.5, rep_x=5, rep_max=10, rep_wait=.4)   # Rep hoàn hảo (index.html: REP); rep_p = tỉ lệ PERFECT, rep_wait = giây dừng tay chờ vòng


def rep_gain(g):
    """Calo thêm trung bình mỗi vòng, tính bằng số cú bấm: PERFECT với xác suất p, chuỗi k PERFECT liên tiếp (phân phối hình học) cho x(rep_x + k - 1), tối đa rep_max."""
    p = g['rep_p']
    return sum(p * (1 - p) * p ** (k - 1) * (min(g['rep_x'] + k - 1, g['rep_max']) - 1) for k in range(1, 200)) + p ** 200 * (g['rep_max'] - 1)
# Khách xoay vòng theo đúng tỉ lệ thay cho ngẫu nhiên: PT 50% (f bấm x5, s thể lực, c calo), crush 30% (65% được: R bấm x7 / C calo x2; còn lại L mất thể lực), bánh 20% (K, luôn ăn)
VIS = 'fscfsRCLKK'


def run(g, rest_at=40, meal='h', limit=400):
    lv = [0] * 8; cal = t = 0.0; wins = summons = 0; rk = 0; kg = g['kg0']; fat = 0.0; day = 1; week = []; wkb = False; rec = False; today = None
    out = {}; rests = 0; ptc = 0.0; ptn = 0; gm = {}; earned = [0.0] * len(g['goals']); tapped = [0.0] * len(g['goals'])   # calo theo hạng: tổng / từ cú bấm   # gm: ngày đủ mục tiêu nhóm cơ của từng hạng (để biết cân nặng chặn bao lâu)
    top = len(g['goals']) - 1   # hạng cao nhất (chỉ số)
    foe = lambda i: g['t0'] * g['tg'] ** min(i, 19) * g['tg2'] ** max(0, i - 19)   # mục tiêu đối thủ i: từ đối thủ 21 (phản diện) chỉ tăng tg2 lần mỗi người
    boost = lambda l: 2 ** sum(l >= m for m in MS)

    def rates():
        m = g['mults'][rk] * (1 + g['win'] * wins) * (1 + g['ach'] * min(16, rk * 2 + wins // 4 + summons // 5 + 3)) * (1.1 if wkb else 1) * (1.2 if 68 <= kg <= 72 else 1) * {'p': 1.25, 'j': 1.1}.get(today, 1)
        pb = 1 + g['pet'] * summons
        base = sum(e[2] * l * boost(l) for e, l in zip(EX, lv))
        click = (1 + sum(e[1] * l * boost(l) for e, l in zip(EX, lv)) + base * g['tap']) * m * pb * (1.25 if rec else 1) * (1.5 if today == 'j' else 1)
        return (0 if g['hands'] else base * m * pb), click   # thử thách Chỉ dùng tay: không có calo/giây, cú bấm vẫn ăn 25% calo/giây gốc

    def shop():
        nonlocal cal, summons, rk
        while True:
            while rk < top and all(l >= x for l, x in zip(lv, g['goals'][rk + 1])) and kg <= g['kg'][rk + 1]: rk += 1
            if rk == top: return
            if all(l >= x for l, x in zip(lv, g['goals'][rk + 1])): gm.setdefault(rk + 1, (day, t))
            miss = [i for i in range(8) if lv[i] < g['goals'][rk + 1][i]]
            if not miss:   # chỉ còn kẹt cân nặng: mua thứ rẻ nhất để tăng thu nhập
                miss = list(range(8))
            i = min(miss, key=lambda i: EX[i][0] * g['R'] ** lv[i]); c = EX[i][0] * g['R'] ** lv[i] * g['fee']
            sc = g['s0'] * g['sg'] ** summons
            if rk >= 4 and sc <= c * 2 and cal >= sc: cal -= sc; summons += 1; continue
            if cal < c: return
            cal -= c; lv[i] += 1

    while day <= limit and rk < top:
        flv = 3 if fat >= 100 else 2 if fat >= 70 else 1 if fat >= 40 else 0
        cap = int((g['sta0'] + g['sta_rank'] * min(rk, 5) + g['sta_cardio'] * lv[7]) * [1, .75, .5, .5][flv] * (.8 if kg > 90 else 1) * ({'h': 1.1, 'j': 1.5}.get(today, 1)))
        r0 = rk; used = 0; pv = 0; sunday = (day - 1) % 7 == 6
        pps, click = rates(); cal += pps * IDLE; t += IDLE; earned[rk] += pps * IDLE
        if fat >= 100 or fat >= rest_at:
            rests += 1; lazy = fat < 40; rec_next = not lazy; kg += .3 if lazy else .1; fat = max(0, fat - 60)
        else:
            sta = cap
            while sta >= 1:
                pps, click = rates()
                if rk >= 3 and wins < g['rivals'] and (sunday or sta >= g['duel_sta']) and g['duel'] * (pps + CPS * click) >= foe(wins):
                    if not sunday: sta -= g['duel_sta']; used += g['duel_sta']
                    cal += foe(wins) * g['prize'] * (2 if sunday else 1) + g['duel'] * pps; t += g['duel'] + 6; wins += 1   # cú bấm trong trận không ra calo; +6 giây VS, thoại, đếm ngược
                else:
                    n = min(10, int(sta)); sta -= n; used += n; cal += n * click + pps * n / CPS; t += n / CPS; earned[rk] += n * click + pps * n / CPS; tapped[rk] += n * click
                    ptc += n / CPS
                    rings = n / g['rep_every'] * (rk >= 1); x = rings * rep_gain(g) * click   # Rep hoàn hảo: tính trung bình thay cho từng vòng
                    cal += x; earned[rk] += x; tapped[rk] += x; t += rings * g['rep_wait'] * (g['rep_p'] > 0)   # không bắt vòng thì không phải dừng tay
                    if ptc >= g['pt_gap'] * 1.5 and g['pt'] and rk >= 1 and pv < g['pt_day']:   # khách đến sau trung bình 1,5 x gap giây ở phòng tập
                        ptc = 0; ptn += 1; pv += 1; k = VIS[ptn % len(VIS)]; x = 0; bonus = (pps * g['pt_cps'] + click * g['pt_taps']) * g['pt']
                        if k in 'fR':   # bấm nhân: PT x5 trong 8 giây, crush x7 trong 10 giây
                            mx, sec = (g['pt_tap'], g['pt_life']) if k == 'f' else (g['cr_tap'], g['cr_sec'])
                            x = min(sta, sec * CPS) * click * (mx - 1) * g['pt']; tapped[rk] += x
                        elif k == 's': sta += int(cap * g['pt_sta'] * g['pt'])
                        elif k == 'c': x = bonus
                        elif k == 'C': x = bonus * g['cr_cal']
                        elif k == 'L': sta -= int(sta * g['cr_lose'] * g['pt'])
                        elif k == 'K': x = bonus * g['ck_cal']; kg += g['ck_kg'] * g['pt']
                        cal += x; earned[rk] += x
                shop()
            frac = min(1, used / max(1, cap)); rec_next = False
            kg -= g['kg_loss'][rk] * frac; fat = min(100, max(0, fat + (g['fat'][r0] * frac if r0 >= 2 else 0) - 5))
        frac = min(1, used / max(1, cap)); week.append(1 if frac >= .5 else 0)
        if len(week) >= 7: wkb = r0 >= 2 and sum(week) >= g['wk'][r0]; week = []
        nxt = None
        kg += g['night']   # thử thách Mùa tiệc cưới: +0,2 kg mỗi tối
        if rk >= 1 and meal: nxt = meal; kg += {'h': -.1, 'p': 0, 'j': .2}[meal]
        kg = min(120, max(68, kg)); rec = rec_next; today = nxt; day += 1
        shop()
        if rk not in out and rk > 0:
            for r in range(1, rk + 1): out.setdefault(r, (day, t, kg))
    return out, dict(day=day, t=t, kg=kg, wins=wins, summons=summons, rests=rests, lv=lv, rk=rk, gm=gm, earned=sum(earned), share=[tp / e for tp, e in zip(tapped, earned) if e])


def fmt(s): return f'{int(s // 3600)}h{int(s % 3600 // 60):02d}m' if s >= 3600 else f'{int(s // 60)}m{int(s % 60):02d}s'


def report(name, **over):
    g = {**G, **over}
    print(name, over or '')
    for label, ra in (('không nghỉ', 999), ('nghỉ khi Mỏi', 40), ('nghỉ khi Kiệt sức', 70)):
        out, e = run(g, ra)
        print(f'  {label:18}', '  '.join(f'H{r + 1}: ngày {d} ({fmt(t)}, {k:.1f}kg)' for r, (d, t, k) in sorted(out.items())),
              f"| cuối: hạng {e['rk'] + 1}, ngày {e['day']}, nghỉ {e['rests']}, đấu {e['wins']}, gọi {e['summons']}, {fmt(e['t'] / max(1, e['day'] - 1))}/ngày"
              + ' | bấm: ' + ' '.join(f'{x:.0%}' for x in e['share']))


if __name__ == '__main__':
    report('HIỆN TẠI')
    if '-x' in sys.argv:   # thử phương án: python tools/sim.py -x
        for v in (.05, .3): report('THỬ', tap=v)
        report('THỬ', pt=0)
