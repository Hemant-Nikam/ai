import pygame
import heapq
import time

pygame.init()

# Window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("A* Treasure Hunt")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Grid settings
rows = 5
cell = 100

# Positions
start = (0, 0)
treasure = (4, 4)
exit_gate = (0, 4)

# Player position
player = [0, 0]

# Monsters
monsters = [(0,3), (3,1), (4,1)]

# Directions
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

# Treasure status
treasure_collected = False


# Draw everything
def draw():

    win.fill(WHITE)

    # Draw grid
    for i in range(rows):

        pygame.draw.line(
            win,
            BLACK,
            (0, i * cell),
            (500, i * cell)
        )

        pygame.draw.line(
            win,
            BLACK,
            (i * cell, 0),
            (i * cell, 500)
        )

    # Draw monsters
    for m in monsters:

        pygame.draw.rect(
            win,
            RED,
            (m[1] * cell, m[0] * cell, cell, cell)
        )

    # Draw treasure
    if not treasure_collected:

        pygame.draw.rect(
            win,
            YELLOW,
            (treasure[1] * cell, treasure[0] * cell, cell, cell)
        )

    # Draw exit gate
    if treasure_collected:

        pygame.draw.rect(
            win,
            GREEN,
            (exit_gate[1] * cell, exit_gate[0] * cell, cell, cell)
        )

    # Draw player
    pygame.draw.rect(
        win,
        BLUE,
        (player[1] * cell, player[0] * cell, cell, cell)
    )

    pygame.display.update()


# Manhattan Distance
def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Algorithm
def astar(start, goal):

    open_list = []

    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_cost = {}

    came_from[start] = None
    g_cost[start] = 0

    found = False

    while open_list:

        current = heapq.heappop(open_list)[1]

        # Goal found
        if current == goal:

            found = True
            break

        # Check neighbors
        for d in directions:

            nx = current[0] + d[0]
            ny = current[1] + d[1]

            next_node = (nx, ny)

            # Inside grid
            if 0 <= nx < 5 and 0 <= ny < 5:

                # Avoid monsters
                if next_node not in monsters:

                    new_cost = g_cost[current] + 1

                    # Better path
                    if next_node not in g_cost or new_cost < g_cost[next_node]:

                        g_cost[next_node] = new_cost

                        # f(n) = g(n) + h(n)
                        priority = new_cost + heuristic(goal, next_node)

                        heapq.heappush(
                            open_list,
                            (priority, next_node)
                        )

                        came_from[next_node] = current

    # No path found
    if not found:
        return []

    # Build final path
    path = []

    current = goal

    while current != start:

        path.append(current)

        current = came_from[current]

    path.append(start)

    path.reverse()

    return path


# Move player
def move(path):

    for p in path:

        player[0] = p[0]
        player[1] = p[1]

        draw()

        print("Player:", player)
        print("----------------")

        time.sleep(0.5)


# Main game
running = True

draw()

# Path to treasure
path1 = astar(start, treasure)

if path1:

    move(path1)

    print("Treasure Collected!")

    treasure_collected = True

    draw()

    time.sleep(1)

    # Path to exit
    path2 = astar(treasure, exit_gate)

    if path2:

        move(path2)

        print("Escaped Successfully!")

    else:
        print("No path to exit!")

else:
    print("No path to treasure!")


# Keep window open
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

pygame.quit()