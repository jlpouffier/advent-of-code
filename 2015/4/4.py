import time
import hashlib

with open("2015/4/input.txt", mode="r") as file:
    input = ""
    for line in file:
        input += line

part1_start_time = time.time()

number = 0
while True:
    tested_input = input + str(number)
    md5_hash = hashlib.md5()
    md5_hash.update(tested_input.encode('utf-8'))
    hash_result = md5_hash.hexdigest()
    if hash_result.startswith("00000"):
        break
    else:
        number += 1
print(number)

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")

part2_start_time = time.time()

number = 0
while True:
    tested_input = input + str(number)
    md5_hash = hashlib.md5()
    md5_hash.update(tested_input.encode('utf-8'))
    hash_result = md5_hash.hexdigest()
    if hash_result.startswith("000000"):
        break
    else:
        number += 1
print(number)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")