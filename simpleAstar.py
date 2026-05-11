graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

h = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

open = ['A']
g = {'A': 0}
path = {}

goal = 'D'

while open:

    # find smallest f = g + h
    best = open[0]

    for i in open:
        if g[i] + h[i] < g[best] + h[best]:
            best = i

    current = best

    if current == goal:
        break

    open.remove(current)

    for i in graph[current]:

        new_cost = g[current] + 1

        if i not in g or new_cost < g[i]:

            g[i] = new_cost
            path[i] = current

            if i not in open:
                open.append(i)

# print path
node = goal

while node != 'A':
    print(node, end=' <- ')
    node = path[node]

print('A')