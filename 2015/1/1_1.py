import time

with open("2015/1/input.txt", mode="r") as file:
    instructions = ""
    for line in file:
        instructions += line


part1_start_time = time.time()

floor = 0
for char in instructions:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -=1

print(floor)

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")