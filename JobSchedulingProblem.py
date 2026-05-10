jobs = [
    ["J1", 2, 100],
    ["J2", 1, 50],
    ["J3", 2, 10],
    ["J4", 1, 20]
]

# Sort by profit
for i in range(len(jobs)):

    for j in range(i + 1, len(jobs)):

        if jobs[i][2] < jobs[j][2]:

            jobs[i], jobs[j] = jobs[j], jobs[i]


slots = [False] * 3

result = []

profit = 0


for job in jobs:

    name = job[0]
    deadline = job[1]
    money = job[2]

    # Check slots backward
    for j in range(deadline - 1, -1, -1):

        if not slots[j]:

            slots[j] = True

            result.append(name)

            profit += money

            break


print("Selected Jobs:", result)

print("Total Profit:", profit)