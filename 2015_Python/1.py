print("Enter puzzle input:")

instructions = input()
current_floor = 0

floors = list(map(lambda x: 1 if x is "(" else -1, list(instructions)))

for i, floor in enumerate(floors):
    current_floor += floor
    if current_floor < 0:
        print("First character that causes him to enter the basement: " + str(i + 1))
        break

print("Floor: " + str(sum(floors)))
