graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# DFS
visited = []

def dfs(node):

    if node not in visited:

        print(node, end=" ")

        visited.append(node)

        for i in graph[node]:

            dfs(i)


# Recursive BFS
visited_bfs = []

def bfs(queue):

    if not queue:
        return

    node = queue.pop(0)

    if node not in visited_bfs:

        print(node, end=" ")

        visited_bfs.append(node)

        for i in graph[node]:

            queue.append(i)

    bfs(queue)


# Main
print("DFS:")

dfs('A')

print("\n")

print("BFS:")

bfs(['A'])