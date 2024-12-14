import time

part1_start_time = time.time()

with open("2015/2/input.txt", mode="r") as file:
    wrapping_paper_surface = 0
    for line in file:
        numbers = [int(number) for number in line.split('x')]
        numbers.sort()
        wrapping_paper_surface += 2 * numbers[0] * numbers[1] + 2 * numbers[1] * numbers[2] + 2 * numbers[2] * numbers[0] + numbers[0] * numbers[1]
    print(wrapping_paper_surface)

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")



part2_start_time = time.time()

with open("2015/2/input.txt", mode="r") as file:
    ribbon_length = 0
    for line in file:
        numbers = [int(number) for number in line.split('x')]
        numbers.sort()
        ribbon_length += 2 * numbers[0] + 2 * numbers[1] + numbers[0] * numbers[1] * numbers[2]
    print(ribbon_length)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")