print("Enter puzzle input:")

instructions = input()
current_position_santa = [0,0]
current_position_robo = [0,0]
visited_positions = set()
visited_positions.add(tuple(current_position_santa))

for i, step in enumerate(instructions):
    current_position = current_position_santa if i % 2 == 0 else current_position_robo
    if step == "^":
        current_position[1] += 1
    if step == "v":
        current_position[1] -= 1
    if step == ">":
        current_position[0] += 1
    if step == "<":
        current_position[0] -= 1

    visited_positions.add(tuple(current_position))

print("Houses visited: " + str(len(visited_positions)))

