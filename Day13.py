from utils import *

with open("input.txt") as f:
    data = [line.strip() for line in f if line.strip()]
ans = 0
for i in range(0, len(data), 3):
    ax, ay = get_ints(data[i])
    bx, by = get_ints(data[i + 1])
    resx, resy = get_ints(data[i + 2])
    resx, resy = resx + 10 ** 13, resy + 10 ** 13  # Uncomment for part 2, comment out for part 1
    det = ax * by - ay * bx
    j = (resx * by - resy * bx) / det
    k = (ax * resy - ay * resx) / det
    if j.is_integer() and k.is_integer():
        ans += 3 * int(j) + int(k)
print(ans)
