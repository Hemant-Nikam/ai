edges = [
    [1, 2, 1],
    [1, 3, 4],
    [2, 3, 2],
    [2, 4, 5],
    [3, 4, 3]
]

# Simple sorting
for i in range(len(edges)):

    for j in range(i + 1, len(edges)):

        if edges[i][2] > edges[j][2]:

            edges[i], edges[j] = edges[j], edges[i]


parent = [0, 1, 2, 3, 4]


# Find parent
def find(x):

    while parent[x] != x:

        x = parent[x]

    return x


print("Edge : Weight")

# Kruskal Algorithm
for edge in edges:

    u = edge[0]
    v = edge[1]
    w = edge[2]

    p1 = find(u)
    p2 = find(v)

    # No cycle
    if p1 != p2:

        print(u, "-", v, ":", w)

        # Union
        parent[p1] = p2