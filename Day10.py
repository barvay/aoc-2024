import sys
from collections import deque


def main() -> int:
    with open("input.txt") as f:
        data = [line.strip() for line in f]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    h, w = len(data), len(data[0])

    def bfs(_y, _x, _v):
        queue = deque([(_y, _x, _v)])
        vis = set()
        res = 0
        while queue:
            y, x, v = queue.popleft()
            if v == '9':
                vis.add((y, x))
                res += 1
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= ny < h and 0 <= nx < w:
                    nv = data[ny][nx]
                    if int(nv) == int(v) + 1:
                        queue.append((ny, nx, nv))
        return res  # return len(vis) for part 1

    ans = 0
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == '0':
                ans += bfs(i, j, value)
    print(ans)
    return 0


if __name__ == '__main__':
    sys.exit(main())
