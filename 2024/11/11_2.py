import time

cache = {}

def is_even_digit_number(number):
    digit_count = len(str(number))
    return digit_count % 2 == 0

def split_even_number(number):
    mid = len(str(number)) // 2
    return int(str(number)[:mid]) , int(str(number)[mid:])

def blink(numbers, times = 1):
    print(len(numbers))
    if times == 0:
        return numbers
    else:
        new_numbers = []
        for number in numbers:
            if number in cache:
                new_numbers.extend(cache[number])
            else:
                if number == 0:
                    cache[number] = [1]
                elif is_even_digit_number(number):
                    cache[number] = split_even_number(number)
                else:
                    cache[number] = [2024 * number]
                new_numbers.extend(cache[number])
        return blink(new_numbers, times - 1)

with open("2024/11/test.txt", mode="r") as file:
    for line in file:
        numbers = [int(number) for number in line.split(' ')]

part2_start_time = time.time()

new_numbers = blink(numbers, 75)
print(len(new_numbers))

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")