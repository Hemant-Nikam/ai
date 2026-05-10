graph = [
    [0, 4, 1, 0],
    [4, 0, 2, 5],
    [1, 2, 0, 8],
    [0, 5, 8, 0]
]

n = len(graph)

source = 0

distance = [999] * n

visited = [False] * n

distance[source] = 0


for i in range(n):

    minimum = 999
    u = 0

    # Find nearest node
    for j in range(n):

        if not visited[j] and distance[j] < minimum:

            minimum = distance[j]
            u = j

    visited[u] = True

    # Update neighbors
    for v in range(n):

        if graph[u][v] and not visited[v]:

            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:

                distance[v] = new_distance


print("Shortest Distances:")

for i in range(n):

    print(source, "->", i, "=", distance[i])