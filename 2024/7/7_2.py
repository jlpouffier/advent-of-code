import time

part2_start_time = time.time()
with open("2024/7/input.txt", mode="r") as file:
    part2 = 0
    for line in file:
        # Extract result and numbers, and correctly cast them
        result, numbers = line.strip('\n').split(': ')
        result = int(result)
        numbers = [int(number) for number in numbers.split(' ')]

        # Initialize a list of possibilities with the number list
        possibilities = [numbers]

        # Initialize a results list empty.
        results = []

        keep_going = True
        while keep_going:
            keep_going = False
            new_possibilities = []

            # Loop on each possibility
            for possibility in possibilities:
                
                # If the possibility has more than 2 numbers. 
                # Append the sum and product and concatenation (Only if smaller than the result)
                # To a new possibilities list
                if len(possibility) > 2:
                    keep_going = True
                    if possibility[0] + possibility[1] <= result:
                        new_possibilities.append([possibility[0] + possibility[1]] +  possibility[2:])
                    if possibility[0] * possibility[1] <= result:
                        new_possibilities.append([possibility[0] * possibility[1]] +  possibility[2:])
                    if int(str(possibility[0]) + str(possibility[1])) <= result:
                        new_possibilities.append([int(str(possibility[0]) + str(possibility[1]))] +  possibility[2:])
    
                # If the possibility is exactly 2 numbers. 
                # Append the sum and product and concatenation  (ONly if smaller than the result)
                # To the results list
                elif len(possibility) == 2:
                    if possibility[0] + possibility[1] <= result:
                        results.append(possibility[0] + possibility[1])
                    if possibility[0] * possibility[1] <= result:    
                        results.append(possibility[0] * possibility[1])
                    if int(str(possibility[0]) + str(possibility[1])) <= result:
                        results.append(int(str(possibility[0]) + str(possibility[1])))

            # Flush the possibilities with the new ones.
            possibilities = new_possibilities
        
        # If result in results, add result to part2 solution
        if result in results:
            part2 += result

print(part2)
part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")