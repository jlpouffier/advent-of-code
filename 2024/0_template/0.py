import time

with open("2024/9/input.txt", mode="r") as file:
    for line in file:
        print(line)


part1_start_time = time.time()



part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")