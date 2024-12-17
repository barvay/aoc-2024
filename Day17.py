from utils import *

with open("input.txt") as f:
    a = get_ints(f.readline())[0]
    b = get_ints(f.readline())[0]
    c = get_ints(f.readline())[0]
    program = get_ints(f.read())


def run(ra, rb=0, rc=0):
    ip = 0
    out = []
    while ip < len(program):
        combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: ra, 5: rb, 6: rc}
        opcode = program[ip]
        operand = program[ip + 1]
        match opcode:
            case 0:
                ra //= 2 ** combo[operand]
            case 1:
                rb ^= operand
            case 2:
                rb = combo[operand] % 8
            case 3:
                if ra:
                    ip = operand
                    continue
            case 4:
                rb ^= rc
            case 5:
                out.append(combo[operand] % 8)
            case 6:
                rb = ra // 2 ** combo[operand]
            case 7:
                rc = ra // 2 ** combo[operand]
        ip += 2
    return out


print(','.join(map(str, run(a, b, c))))

ans = []
cur = [(1, 0)]
for i, a in cur:
    for a in range(a, a + 8):
        if run(a) == program[-i:]:
            cur.append((i + 1, a * 8))
            if i == len(program):
                ans.append(a)
print(min(ans))
