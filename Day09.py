import itertools
import sys
from collections import deque


def main() -> int:
    data = open("input.txt").read().strip()
    arr = list(map(int, list(data)))
    ps = [0] + list(itertools.accumulate(arr))
    used = []
    free = []
    seg_id = 0
    for i, v in enumerate(arr):
        if i % 2 == 0:
            used.append((seg_id, ps[i], ps[i] + v))
            seg_id += 1
        elif v > 0:
            free.append([ps[i], v])
    res = ['.'] * ps[-1]
    q = deque(used)
    while q:
        seg_id, start, end = q.popleft()
        for i in range(start, end):
            res[i] = seg_id
    l, r = 0, ps[-1] - 1
    while l < r:
        while l < r and res[l] != '.':
            l += 1
        while l < r and res[r] == '.':
            r -= 1
        if l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
    print(sum(i * int(v) for i, v in enumerate(res) if v != '.'))

    def find_free_seg(length, max_idx):
        for i, (start, size) in enumerate(free):
            if start >= max_idx:
                return -1
            if size >= length:
                return i
        return -1

    res = ['.'] * ps[-1]
    q = deque(used)
    while q:
        seg_id, start, end = q.popleft()
        for i in range(start, end):
            res[i] = seg_id
    q = deque(used)
    while q:
        seg_id, start, end = q.pop()
        seg_length = end - start
        free_index = find_free_seg(seg_length, start)
        if free_index != -1:
            free_start, free_size = free[free_index]
            for i in range(free_start, free_start + seg_length):
                res[i] = seg_id
            for i in range(start, end):
                res[i] = '.'
            if free_size == seg_length:
                free.pop(free_index)
            else:
                free[free_index][0] += seg_length
                free[free_index][1] -= seg_length
    print(sum(i * int(v) for i, v in enumerate(res) if v != '.'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
