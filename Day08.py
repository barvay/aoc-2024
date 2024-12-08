import sys
from itertools import combinations
from collections import defaultdict


def part_one(arr: list[str]) -> int:
    coords = defaultdict(list)
    for i, row in enumerate(arr):
        for j, char in enumerate(row):
            if char not in {'.', '#'}:
                coords[char].append((i, j))
    res = set()
    h, w = len(arr), len(arr[0])
    for pos in coords.values():
        for (x1, y1), (x2, y2) in combinations(pos, 2):
            dx, dy = x2 - x1, y2 - y1
            x, y = x1 - dx, y1 - dy
            if 0 <= x < h and 0 <= y < w:
                res.add((x, y))
            x, y = x2 + dx, y2 + dy
            if 0 <= x < h and 0 <= y < w:
                res.add((x, y))
    return len(res)


def part_two(arr: list[str]) -> int:
    coords = defaultdict(list)
    for i, row in enumerate(arr):
        for j, char in enumerate(row):
            if char not in {'.', '#'}:
                coords[char].append((i, j))
    res = set()
    h, w = len(arr), len(arr[0])
    for pos in coords.values():
        for (x1, y1), (x2, y2) in combinations(pos, 2):
            dx, dy = x2 - x1, y2 - y1
            x, y = x1, y1
            while 0 <= x < h and 0 <= y < w:
                res.add((x, y))
                x -= dx
                y -= dy
            x, y = x2, y2
            while 0 <= x < h and 0 <= y < w:
                res.add((x, y))
                x += dx
                y += dy
    return len(res)


def main() -> int:
    with open("input.txt") as f:
        data = [line.strip() for line in f]
    print(part_one(data))
    print(part_two(data))
    return 0


if __name__ == '__main__':
    sys.exit(main())
