import networkx as nx

with open("input.txt") as file:
    g = nx.Graph(line.strip().split('-') for line in file.readlines())

cliques = list(nx.enumerate_all_cliques(g))
part1 = sum(
    len(clique) == 3 and any(node.startswith('t') for node in clique)
    for clique in cliques
)
print(part1)
part2 = max(
    (','.join(sorted(clique)) for clique in cliques),
    key=lambda clique: len(clique)
)
print(part2)
