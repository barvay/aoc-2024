from utils import *

g = defaultdict(set)
for line in open("input.txt"):
    u, v = line.strip().split('-')
    g[u].add(v)
    g[v].add(u)

part1 = set()
for u in g:
    for v in g[u]:
        for w in g[v]:
            if u in g[w] and any(x.startswith('t') for x in [u, v, w]):
                part1.add(tuple(sorted([u, v, w])))
print(len(part1))


def bron_kerbosch(r, p, x):
    if not p and not x:
        yield r
    else:
        for v in p.copy():
            yield from bron_kerbosch(r | {v}, p & g[v], x & g[v])
            p.remove(v)
            x.add(v)


print(max((','.join(sorted(c)) for c in bron_kerbosch(set(), set(g), set())), key=len))
