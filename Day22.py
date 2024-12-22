from utils import *

with open('input.txt') as f:
    nums = get_ints(f.read())

part1 = 0
part2 = defaultdict(int)
for num in nums:
    a = [num := num ^ (num * 64) % 16777216 ^ (num // 32) % 16777216 ^ (num * 2048) % 16777216 for _ in range(2001)]
    part1 += a[-1]
    diffs = [y % 10 - x % 10 for x, y in itertools.pairwise(a)]
    seen = set()
    for i in range(len(a) - 4):
        cur = tuple(diffs[i:i + 4])
        if cur not in seen:
            seen.add(cur)
            part2[cur] += a[i + 4] % 10

print(part1)
print(max(part2))
