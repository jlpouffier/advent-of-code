import time

# The cache will be a dictionary of dictionary like that
# chache[stone][iteration] = number of stones
cache = {}

def is_even_digit_stone(stone):
    digit_count = len(str(stone))
    return digit_count % 2 == 0

def split_stone(stone):
    mid = len(str(stone)) // 2
    return int(str(stone)[:mid]) , int(str(stone)[mid:])

# Blink a stone, only once.
# Store all the business logic of the blink
def blink(stone):
    new_stones = []
    if stone == 0:
        new_stones.append(1)
    elif is_even_digit_stone(stone):
        new_stones.extend(split_stone(stone))
    else:
        new_stones.append(2024 * stone)
    return new_stones

def compute_number_stones(stone, iteration):
    # If cached, returned cached solution
    if stone in cache and iteration in cache[stone]:
        return cache[stone][iteration]
    
    # Initialize the cache[stone] dict
    elif stone not in cache:
        cache[stone] = {}
    
    # Stop the recursion
    if iteration == 0:
        return 1

    # Blink and recurse
    new_stones = blink(stone)
    nb_stones = 0
    for sub_stone in new_stones:
        nb_stones += compute_number_stones(sub_stone, iteration - 1)
    cache[stone][iteration] = nb_stones
    return nb_stones

with open("2024/11/input.txt", mode="r") as file:
    for line in file:
        stones = [int(number) for number in line.split(' ')]

part2_start_time = time.time()

total_stone_nb = 0
for stone in stones:
    total_stone_nb += compute_number_stones(stone, 75)
print(total_stone_nb)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")