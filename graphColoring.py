graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

colors = [0,0,0,0]

color_names = ["Red", "Green", "Blue"]

m = 3


# Check if color is safe
def safe(node, color):

    for k in range(4):

        if graph[node][k] == 1 and colors[k] == color:
            return False

    return True


# Backtracking
def solve(node):

    if node == 4:
        return True

    for color in range(1, m + 1):

        if safe(node, color):

            colors[node] = color

            if solve(node + 1):
                return True

            colors[node] = 0

    return False


# Main
if solve(0):

    print("Solution Found\n")

    for i in range(4):

        print(
            "Node",
            i,
            "->",
            color_names[colors[i] - 1]
        )

else:
    print("No Solution")