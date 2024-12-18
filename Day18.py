from utils import *

with open("input.txt") as f:
    pos = [get_ints(line) for line in f]

w, h = 71, 71
part1 = [['.' for _ in range(w)] for _ in range(h)]
part2 = [row[:] for row in part1]
lim = 1024
for i in range(lim):
    part1[pos[i][1]][pos[i][0]] = '#'


def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in adj4:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    return -1


start = (0, 0)
end = (70, 70)
print(bfs(part1, start, end))
i = 0
while bfs(part2, start, end) != -1:
    part2[pos[i][1]][pos[i][0]] = '#'
    i += 1
print(','.join(map(str, pos[i - 1])))
