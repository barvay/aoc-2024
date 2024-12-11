import sys


def main() -> int:
    with open("input.txt") as f:
        data = list(map(int, f.read().strip().split()))

    def sim(n, blinks, mem):
        if (n, blinks) in mem:
            return mem[(n, blinks)]
        if blinks == 0:
            return 1
        if n == 0:
            res = sim(1, blinks - 1, mem)
        elif len(str(n)) % 2 == 0:
            m = len(str(n)) // 2
            l = int(str(n)[:m])
            r = int(str(n)[m:])
            res = sim(l, blinks - 1, mem) + sim(r, blinks - 1, mem)
        else:
            res = sim(n * 2024, blinks - 1, mem)
        mem[(n, blinks)] = res
        return res

    mem = {}
    ans = 0
    lim = 75  # 25 for part 1
    for cur in data:
        ans += sim(cur, lim, mem)
    print(ans)
    return 0


if __name__ == '__main__':
    sys.exit(main())
