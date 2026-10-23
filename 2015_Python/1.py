print("Enter puzzle input:")

instructions = input()
floor = 0
hit_basement = False

for i, c in enumerate(instructions):
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

    if floor < 0 and not hit_basement:
        print("First character that causes him to enter the basement: " + str(i + 1))
        hit_basement = True
        
print("Floor: " + str(floor))

