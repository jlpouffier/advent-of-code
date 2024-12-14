import time

def is_even_digit_number(number):
    digit_count = len(str(number))
    return digit_count % 2 == 0

def split_even_number(number):
    mid = len(str(number)) // 2
    return int(str(number)[:mid]) , int(str(number)[mid:])

def blink(numbers, times = 1):
    if times == 0:
        return numbers
    else:
        new_numbers = []
        for number in numbers:
            if number == 0:
                new_numbers.append(1)
            elif is_even_digit_number(number):
                new_numbers.extend(split_even_number(number))
            else:
                new_numbers.append(2024 * number)
        return blink(new_numbers, times - 1)

with open("2024/11/input.txt", mode="r") as file:
    for line in file:
        numbers = [int(number) for number in line.split(' ')]

part1_start_time = time.time()

new_numbers = blink(numbers, 25)
print(len(new_numbers))


part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")