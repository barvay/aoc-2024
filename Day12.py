from collections import deque

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]
h, w = len(data), len(data[0])
seen = set()
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def area_perimeter(x, y, z):
    q = deque([(x, y)])
    a, p = 0, 0
    while q:
        cx, cy = q.popleft()
        if (cx, cy) in seen:
            continue
        seen.add((cx, cy))
        a += 1
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] == z:
                    q.append((nx, ny))
                else:
                    p += 1
            else:
                p += 1
    return a, p


def area_sides(x, y, z):
    temp = [[0] * (w + 2) for _ in range(h + 2)]
    q = deque([(x, y)])
    a = 0
    while q:
        cx, cy = q.popleft()
        if (cx, cy) in seen:
            continue
        seen.add((cx, cy))
        temp[cx + 1][cy + 1] = 1
        a += 1
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] == z:
                    q.append((nx, ny))
    s = 0
    for i in range(1, len(temp)):
        prev_t, prev_b = 0, 0
        for t, b in zip(temp[i - 1], temp[i]):
            if t != b and (prev_t != t or prev_b != b):
                s += 1
            prev_t, prev_b = t, b
    for i in range(1, len(temp[0])):
        prev_l, prev_r = 0, 0
        for l, r in zip([row[i - 1] for row in temp], [row[i] for row in temp]):
            if l != r and (prev_l != l or prev_r != r):
                s += 1
            prev_l, prev_r = l, r
    return a, s


ans = 0
for i, row in enumerate(data):
    for j, val in enumerate(row):
        if (i, j) not in seen:
            area, sides = area_sides(i, j, val)  # or area_perimeter(i, j, val) for part 1
            ans += area * sides
print(ans)
