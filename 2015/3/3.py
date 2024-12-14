import time

with open("2015/3/input.txt", mode="r") as file:
    directions = ""
    for line in file:
        directions += line

part1_start_time = time.time()

unique_house_coordinates = set()
unique_house_coordinates.add((0,0))
current_position = (0 , 0)

for direction in directions:
    if direction == ">":
        current_position = (current_position[0] + 1 ,current_position[1])
    elif direction == "v":
        current_position = (current_position[0],current_position[1] - 1)
    elif direction == "<":
        current_position = (current_position[0] - 1 ,current_position[1])
    elif direction == "^":
        current_position = (current_position[0],current_position[1] + 1)
    unique_house_coordinates.add(current_position)

print(len(unique_house_coordinates))


part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")


part2_start_time = time.time()

unique_house_coordinates = set()
unique_house_coordinates.add((0,0))
santa_current_position = (0 , 0)
robot_santa_current_position = (0 , 0)
santa_turn = True

for direction in directions:
    if santa_turn:
        if direction == ">":
            santa_current_position = (santa_current_position[0] + 1 ,santa_current_position[1])
        elif direction == "v":
            santa_current_position = (santa_current_position[0],santa_current_position[1] - 1)
        elif direction == "<":
            santa_current_position = (santa_current_position[0] - 1 ,santa_current_position[1])
        elif direction == "^":
            santa_current_position = (santa_current_position[0],santa_current_position[1] + 1)
        unique_house_coordinates.add(santa_current_position)
    else:
        if direction == ">":
            robot_santa_current_position = (robot_santa_current_position[0] + 1 ,robot_santa_current_position[1])
        elif direction == "v":
            robot_santa_current_position = (robot_santa_current_position[0],robot_santa_current_position[1] - 1)
        elif direction == "<":
            robot_santa_current_position = (robot_santa_current_position[0] - 1 ,robot_santa_current_position[1])
        elif direction == "^":
            robot_santa_current_position = (robot_santa_current_position[0],robot_santa_current_position[1] + 1)
        unique_house_coordinates.add(robot_santa_current_position)
    santa_turn = not santa_turn

print(len(unique_house_coordinates))


part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")