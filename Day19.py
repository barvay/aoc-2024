from utils import *


def ck1(design, a):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and design[j:i] in a:
                dp[i] = True
                break
    return dp[n]


def ck2(design, a):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] > 0 and design[j:i] in a:
                dp[i] += dp[j]
    return dp[n]


if __name__ == "__main__":
    with open("input.txt") as f:
        a, b = f.read().split('\n\n')
        a = a.split(', ')
        b = [line for line in b.splitlines() if line]
    part1, part2 = 0, 0
    for i in b:
        if ck1(i, a):
            part1 += 1
        part2 += ck2(i, a)
    print(part1)
    print(part2)
