import heapq
import time

# Grid size
size = 5

# Positions
start = (0, 0)
treasure = (4, 4)
exit = (0, 4)

# Monsters
monsters = [(0,3), (3,1), (4,1)]

# Directions
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

# Heuristic
def h(a, b):

    return abs(a[0]-b[0]) + abs(a[1]-b[1])


# A* Algorithm
def astar(start, goal):

    open = []

    heapq.heappush(open, (0, start))

    came = {start: None}

    cost = {start: 0}

    while open:

        current = heapq.heappop(open)[1]

        if current == goal:
            break

        for d in dirs:

            nx = current[0] + d[0]
            ny = current[1] + d[1]

            next = (nx, ny)

            # Inside grid and not monster
            if 0 <= nx < size and 0 <= ny < size and next not in monsters:

                new_cost = cost[current] + 1

                if next not in cost or new_cost < cost[next]:

                    cost[next] = new_cost

                    # f(n)=g(n)+h(n)
                    priority = new_cost + h(goal, next)

                    heapq.heappush(open, (priority, next))

                    came[next] = current

    # No path
    if goal not in came:
        return []

    # Create path
    path = []

    current = goal

    while current:

        path.append(current)

        current = came[current]

    path.reverse()

    return path


# Draw grid
def draw(player, show_exit=False):

    for i in range(size):

        for j in range(size):

            if (i,j) == player:
                print("P", end=" ")

            elif (i,j) in monsters:
                print("M", end=" ")

            elif (i,j) == treasure and not show_exit:
                print("T", end=" ")

            elif (i,j) == exit and show_exit:
                print("E", end=" ")

            else:
                print(".", end=" ")

        print()

    print()


# Move player
def move(path, show_exit=False):

    for p in path:

        draw(p, show_exit)

        time.sleep(0.5)


# Main
print("Treasure Hunt Started!\n")

# Go to treasure
path1 = astar(start, treasure)

if path1:

    move(path1)

    print("Treasure Collected!\n")

    time.sleep(1)

    # Go to exit
    path2 = astar(treasure, exit)

    if path2:

        move(path2, True)

        print("Escaped Successfully!")

    else:
        print("No path to exit!")

else:
    print("No path to treasure!")