import time

with open("2015/1/input.txt", mode="r") as file:
    instructions = ""
    for line in file:
        instructions += line


part2_start_time = time.time()

floor = 0
index = 1
for char in instructions:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -=1
    if floor < 0:
        print(index)
        break
    index += 1

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")