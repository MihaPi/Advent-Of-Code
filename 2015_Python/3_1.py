print("Enter puzzle input:")

instructions = input()
current_position = [0,0]
visited_positions = set()
visited_positions.add(tuple(current_position))

for i in instructions:
    if i == "^":
        current_position[1] += 1
    if i == "v":
        current_position[1] -= 1
    if i == ">":
        current_position[0] += 1
    if i == "<":
        current_position[0] -= 1

    visited_positions.add(tuple(current_position))
            
print("Houses visited: " + str(len(visited_positions)))

