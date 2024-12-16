import heapq
from collections import defaultdict

with open("input.txt") as f:
    maze = [line.strip() for line in f]

for i, row in enumerate(maze):
    for j, cell in enumerate(row):
        if cell == 'S':
            sx, sy = i, j
        elif cell == 'E':
            ex, ey = i, j

cur_dir = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_adjs(cur):
    cx, cy, d = cur
    yield 1000, (cx, cy, (d - 1) % 4)
    yield 1000, (cx, cy, (d + 1) % 4)
    dx, dy = dirs[d]
    nx, ny = cx + dx, cy + dy
    if maze[nx][ny] != '#':
        yield 1, (nx, ny, d)


start = (sx, sy, cur_dir)
pq = [(0, start)]
dists = defaultdict(lambda: float('inf'))
from_ = defaultdict(set)
ans = []
dists[start] = 0
while pq:
    dist, cur = heapq.heappop(pq)
    cx, cy, dc = cur
    if (cx, cy) == (ex, ey):
        ans.append(dist)
        pass
    for d, adj in get_adjs(cur):
        new_dist = dist + d
        if new_dist < dists[adj]:
            dists[adj] = new_dist
            heapq.heappush(pq, (new_dist, adj))
            from_[adj].add(cur)
        elif new_dist <= dists[adj]:
            from_[adj].add(cur)

stack = [(ex, ey, 1)]
visited_nodes = set(stack)

while stack:
    current = stack.pop()
    for previous in from_[current]:
        if previous not in visited_nodes:
            visited_nodes.add(previous)
            stack.append(previous)

print(min(ans))
print(len(set(x[:2] for x in visited_nodes)))
