import time
import numpy as np
import re

part2_start_time = time.time()

tokens = 0
with open("2024/13/input.txt", mode="r") as file:
    for line in file:
        clean_line = line.strip('\n')
        if clean_line.startswith('Button A: '):
            numbers = re.findall(r'\d+', clean_line)
            xa, ya = list(map(int, numbers))
            #print(f"Extracting info from {clean_line}")
            #print(f"  > xa = {xa} , ya = {ya}")
        elif clean_line.startswith('Button B: '):
            numbers = re.findall(r'\d+', clean_line)
            xb, yb = list(map(int, numbers))
            #print(f"Extracting info from {clean_line}")
            #print(f"  > xb = {xb} , yb = {yb}")
        elif clean_line.startswith('Prize: '):
            numbers = re.findall(r'\d+', clean_line)
            xp, yp = list(map(int, numbers))
            xp += 10000000000000
            yp += 10000000000000
            #print(f"Extracting info from {clean_line}")
            #print(f"  > xp = {xp} , yp = {yp}")
            M = np.array ([[ xa , xb ],
                           [ ya , yb ]])
            #print(f"Creating matrix {M}")
            p = np.array ([xp , yp])
            #print(f"Creating price vector {p}")
            ab = np.linalg.solve(M,p)
            #print(f"Solving ... {ab}")
            a,b = ab
            #print(a)
            #print(b)
            if all(abs(x - round(x)) < 1e-2 for x in [a, b]):
                #print('Solution in N!')
                a, b = round(a), round(b)
                tokens += int(a) * 3 + int(b) * 1
                #print(f"New token counts ... {tokens}")

tokens = int(tokens)
print(f"Final token counts: {tokens}")

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")