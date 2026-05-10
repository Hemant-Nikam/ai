graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

n = len(graph)

selected = [False] * n

start = 0

selected[start] = True

print("Edge : Weight")

# MST has n-1 edges
for i in range(n - 1):

    minimum = 999

    x = 0
    y = 0

    for j in range(n):

        if selected[j]:

            for k in range(n):

                # Edge exists and node not selected
                if not selected[k] and graph[j][k]:

                    if graph[j][k] < minimum:

                        minimum = graph[j][k]

                        x = j
                        y = k

    print(x, "-", y, ":", graph[x][y])

    selected[y] = True