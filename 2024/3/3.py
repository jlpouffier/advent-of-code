import re
import math

# Find all multiplications and sums them.
def compute_memory(memory):
    sum_of_products = 0
    multiplications = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",memory)
    for multiplication in multiplications:
        numbers = [int(number) for number in re.findall("[0-9]{1,3}",multiplication)]
        product = math.prod(numbers)
        sum_of_products += product
    return sum_of_products

# part 1
with open("2024/3/input.txt", mode="r") as file:
    memory = ""
    for line in file:
        memory += line
    result1 = compute_memory(memory)
print(result1)

# part 2
with open("2024/3/input.txt", mode="r") as file:
    memory = ""
    for line in file:
        memory += line
    memory_parts = re.split("(do\(\)|don't\(\))", memory)
    do = True
    enabled_memory_parts = []
    disabled_memory_parts = []
    for memory_part in memory_parts:
        if memory_part not in ["do()", "don't()"]:
            if do:
                enabled_memory_parts.append(memory_part)
            else:
                disabled_memory_parts.append(memory_part)
        elif memory_part == "do()":
                do = True
        elif memory_part == "don't()":
                do = False
    result2 = 0
    for memory_part in enabled_memory_parts:
        result2 += compute_memory(memory_part)
print(result2)