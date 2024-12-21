from utils import *

NUM_PAD = [
    "789",
    "456",
    "123",
    " 0A"
]

DIR_PAD = [
    " ^A",
    "<v>"
]


def min_path(pad, start, end):
    for y, row in enumerate(pad):
        for x, cell in enumerate(row):
            if cell == start: sx, sy = x, y
            if cell == end: ex, ey = x, y
    paths = []
    q = deque([(sx, sy, "")])
    while q:
        x, y, path = q.pop()
        if (x, y) == (ex, ey):
            paths.append(path + 'A')
            continue
        if ex > x and pad[y][x + 1] != ' ': q.append((x + 1, y, path + '>'))
        if ey > y and pad[y + 1][x] != ' ': q.append((x, y + 1, path + 'v'))
        if ey < y and pad[y - 1][x] != ' ': q.append((x, y - 1, path + '^'))
        if ex < x and pad[y][x - 1] != ' ': q.append((x - 1, y, path + '<'))
    res = paths[0]
    min_turns = float('inf')
    for path in paths:
        turns = sum(a != b for a, b in zip(path, path[1:]))
        if turns < min_turns:
            res = path
            min_turns = turns
    return res


memo = {}


def solve(path, depth):
    if depth > 25: return len(path)  # if depth > 2: return len(path) for part1
    if (path, depth) in memo: return memo[(path, depth)]
    res = 0
    for start, end in zip('A' + path, path):
        if depth == 0:
            res += solve(min_path(NUM_PAD, start, end), depth + 1)
        else:
            res += solve(min_path(DIR_PAD, start, end), depth + 1)
    memo[(path, depth)] = res
    return res


with open("input.txt") as f: lines = [line.strip() for line in f]

print(sum(solve(line.strip(), 0) * get_ints(line)[0] for line in lines))
