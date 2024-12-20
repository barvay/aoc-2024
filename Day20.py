from utils import *

with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

n, m = len(grid), len(grid[0])
g = defaultdict(list)
for x in range(n):
    for y in range(m):
        if grid[x][y] != '#':
            if grid[x][y] == 'E':
                end = (x, y)
            for dx, dy in adj4:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                    g[(x, y)].append((nx, ny))

sp = defaultdict(int)
q = deque([end])
while q:
    node = q.popleft()
    for nx, ny in g[node]:
        if (nx, ny) not in sp:
            sp[(nx, ny)] = sp[node] + 1
            q.append((nx, ny))

ans = 0
lim = 20  # 2 for part 1
for x, y in g:
    shortcuts = []
    for dx in range(-lim, lim + 1):
        diff = lim - abs(dx)
        for dy in range(-diff, diff + 1):
            if dx != 0 or dy != 0:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                    shortcuts.append((nx, ny))
    for dx, dy in shortcuts:
        if sp[(x, y)] - (sp[(dx, dy)] + abs(x - dx) + abs(y - dy)) >= 100:
            ans += 1

print(ans)
