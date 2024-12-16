with open("input.txt") as f:
    part1, moves = f.read().split("\n\n")
part1 = [list(line.strip()) for line in part1.split('\n')]
moves = moves.replace('\n', '')
dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}
part2 = []
for row in part1:
    nrow = []
    for char in row:
        if char == '#':
            nrow.extend(['#', '#'])
        elif char == 'O':
            nrow.extend(['[', ']'])
        elif char == '.':
            nrow.extend(['.', '.'])
        elif char == '@':
            nrow.extend(['@', '.'])
    part2.append(nrow)
for i, row in enumerate(part1):
    for j, cell in enumerate(row):
        if cell == '@':
            cx, cy = i, j
for move in moves:
    dx, dy = dirs[move]
    nx, ny = cx + dx, cy + dy
    while part1[nx][ny] == 'O':
        nx += dx
        ny += dy
    if part1[nx][ny] == '#':
        continue
    else:
        part1[cx][cy] = '.'
        if part1[cx + dx][cy + dy] == 'O':
            part1[nx][ny] = 'O'
        part1[cx + dx][cy + dy] = '@'
        cx += dx
        cy += dy
ans = 0
for i, row in enumerate(part1):
    for j, cell in enumerate(row):
        if cell == 'O':
            ans += 100 * i + j
print(ans)
for i, row in enumerate(part2):
    for j, cell in enumerate(row):
        if cell == '@':
            cx, cy = i, j
for move in moves:
    dx, dy = dirs[move]
    to_move = [(cx, cy)]
    i = 0
    cant_move = False
    while i < len(to_move):
        x, y = to_move[i]
        nx, ny = x + dx, y + dy
        if part2[nx][ny] in "O[]":
            if (nx, ny) not in to_move:
                to_move.append((nx, ny))
            if part2[nx][ny] == '[' and (nx, ny + 1) not in to_move:
                to_move.append((nx, ny + 1))
            if part2[nx][ny] == ']' and (nx, ny - 1) not in to_move:
                to_move.append((nx, ny - 1))
        elif part2[nx][ny] == '#':
            cant_move = True
            break
        i += 1
    if cant_move:
        continue
    temp = [row[:] for row in part2]
    for x, y in to_move:
        temp[x][y] = '.'
    for x, y in to_move:
        temp[x + dx][y + dy] = part2[x][y]
    part2 = temp
    cx += dx
    cy += dy
ans = 0
for i, row in enumerate(part2):
    for j, cell in enumerate(row):
        if cell == '[':
            ans += 100 * i + j
print(ans)
