from utils import *

with open("input.txt") as file: a, b = file.read().split('\n\n')
x = defaultdict(int, {wire: int(value) for wire, value in (line.split(': ') for line in a.split('\n'))})
y1 = deque(line.split(' ') for line in b.split('\n') if line)
y2 = y1.copy()

while y1:
    input1, operator, input2, _, output = y1.popleft()
    if input1 in x and input2 in x:
        if operator == 'AND':
            x[output] = x[input1] & x[input2]
        elif operator == 'OR':
            x[output] = x[input1] | x[input2]
        elif operator == 'XOR':
            x[output] = x[input1] ^ x[input2]
    else:
        y1.append([input1, operator, input2, _, output])

z_wires = {wire: value for wire, value in x.items() if wire.startswith('z')}
part1 = ''.join(str(value) for wire, value in sorted(z_wires.items(), reverse=True))
print(int(part1, 2))

part2 = set()
high_z = max(z_wires.keys())
for src1, operator, src2, _, result in y2:
    if result.startswith("z") and operator != "XOR" and result != high_z:
        part2.add(result)
    if operator == "XOR" and result[0] not in "xyz" and src1[0] not in "xyz" and src2[0] not in "xyz":
        part2.add(result)
    if operator == "AND" and "x00" not in [src1, src2]:
        for sub_src1, sub_operator, sub_src2, _, sub_result in y2:
            if (result == sub_src1 or result == sub_src2) and sub_operator != "OR":
                part2.add(result)
    if operator == "XOR":
        for sub_src1, sub_operator, sub_src2, _, sub_result in y2:
            if (result == sub_src1 or result == sub_src2) and sub_operator == "OR":
                part2.add(result)
print(",".join(sorted(part2)))
