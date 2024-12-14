from utils import *

with open("input.txt", 'r') as file:
    part1 = [get_ints(line) for line in file]
    part2 = part1.copy()
w, h = 101, 103
for _ in range(100):
    for i, (cx, cy, dx, dy) in enumerate(part1):
        part1[i] = [(cx + dx) % w, (cy + dy) % h, dx, dy]
tl, tr, bl, br = 0, 0, 0, 0
for cx, cy, _, _ in part1:
    if cy < h // 2:
        if cx < w // 2:
            tl += 1
        elif cx > w // 2:
            tr += 1
    elif cy > h // 2:
        if cx < w // 2:
            bl += 1
        elif cx > w // 2:
            br += 1
print(tl * tr * bl * br)
t = 0
while True:
    temp = [['.' for _ in range(w)] for _ in range(h)]
    for cx, cy, _, _ in part2:
        temp[cy][cx] = '#'
    for i, (cx, cy, dx, dy) in enumerate(part2):
        part2[i] = [(cx + dx) % w, (cy + dy) % h, dx, dy]
    if t == 8149:  # Answer for part 2
        for row in temp:
            print(''.join(row))
        break
    t += 1
