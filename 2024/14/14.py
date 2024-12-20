import time
import re

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robots = []
                
    def add_robot(self, robot):
        self.robots.append(robot)

    def get(self, x, y):
        count = 0
        for robot in self.robots:
            if robot.x == x and robot.y == y:
                count += 1
        return count
    
    def move_robots(self, iteration = 1):
        if iteration > 0:
            for robot in self.robots:
                robot.x = (robot.x + robot.vx) % self.width
                robot.y = (robot.y + robot.vy) % self.height
            #print(self)
            #print("\n")
            self.move_robots(iteration - 1)
    
    def get_satefy_score(self):
        nb_robot_quadrant1 = 0
        nb_robot_quadrant2 = 0
        nb_robot_quadrant3 = 0
        nb_robot_quadrant4 = 0
        for j in range(self.height):
            for i in range(self.width):
                if i < self.width // 2 and j < self.height // 2:
                    #print(f'{i}, {j} is in quadrant 1')
                    nb_robot_quadrant1 += self.get(i,j)
                    #print(f'Safety score of quadaran 1 is {nb_robot_quadrant1}')
                elif i > self.width // 2 and j < self.height // 2:
                    #print(f'{i}, {j} is in quadrant 2')
                    nb_robot_quadrant2 += self.get(i,j)
                    #print(f'Safety score of quadaran 2 is {nb_robot_quadrant2}')
                elif i < self.width // 2 and j > self.height // 2:
                    #print(f'{i}, {j} is in quadrant 3')
                    nb_robot_quadrant3 += self.get(i,j)
                    #print(f'Safety score of quadaran 3 is {nb_robot_quadrant3}')
                elif i > self.width // 2 and j > self.height // 2:
                    #print(f'{i}, {j} is in quadrant 4')
                    nb_robot_quadrant4 += self.get(i,j)
                    #print(f'Safety score of quadaran 4 is {nb_robot_quadrant4}')
        #print(f'Safety score of quadaran 1 is {nb_robot_quadrant1}')
        #print(f'Safety score of quadaran 2 is {nb_robot_quadrant2}')
        #print(f'Safety score of quadaran 3 is {nb_robot_quadrant3}')
        #print(f'Safety score of quadaran 4 is {nb_robot_quadrant4}')
        return  nb_robot_quadrant1 * nb_robot_quadrant2 * nb_robot_quadrant3 * nb_robot_quadrant4
    
    def is_symetrical(self):
        for j in range(self.height):
            for i in range(self.width // 2):
                #print(f' For {i}, {j}. grid(i,j) = {self.get(i,j)} amd its mirror in {self.width - i},{j} is {self.get(self.width - i , j)}')
                if self.get(i,j) != self.get(self.width - 1 - i , j):
                    return False
        return True
        
    def get_symetry_score(self):
        score = 0
        for j in range(self.height):
            for i in range(self.width // 2):
                #print(f' For {i}, {j}. grid(i,j) = {self.get(i,j)} amd its mirror in {self.width - i},{j} is {self.get(self.width - i , j)}')
                if self.get(i,j) != 0 and self.get(i,j) == self.get(self.width - 1 - i , j):
                    score += self.get(i,j) * 2
        return score / len(self.robots)

    def __repr__(self):
        rows = []
        for j in range(self.height):
            row = []
            for i in range(self.width):
                number_of_robot = self.get(i,j)
                if number_of_robot == 0:
                    char = '.'
                else:
                    char = str(number_of_robot)
                row.append(char)
            rows.append(row)
        return '\n'.join(' '.join(map(str, row)) for row in rows)


class Robot:
    def __init__(self, data):
        self.x, self.y, self.vx, self.vy = re.findall(r'[-]?\d+', data)
        self.x = int(self.x)
        self.y = int(self.y)
        self.vx = int(self.vx)
        self.vy = int(self.vy)
        #print(f"Robot created in {self.x},{self.y} with velocity {self.vx},{self.vy} ")

# PART 1
part1_start_time = time.time()
robots = []
grid = Grid(101,103)
with open("2024/14/input.txt", mode="r") as file:
    for line in file:
        grid.add_robot(Robot(line))

grid.move_robots(100)
print(grid.get_satefy_score())

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")



# PART 2
part2_start_time = time.time()
robots = []
grid = Grid(101,103)
#grid = Grid(11,7)
with open("2024/14/input.txt", mode="r") as file:
    for line in file:
        grid.add_robot(Robot(line))

print("Searching for the first symetrical solution")
# elapsed = 0
# while True:
#     grid.move_robots()
#     elapsed += 1
#     if grid.is_symetrical():
#         break
# print(grid)
# print(elapsed)

# elapsed = 0
# while True:
#     grid.move_robots()
#     elapsed += 1
#     if grid.get_symetry_score() > 0.1: 
#         print(grid)
#         print(elapsed)
#         print('\n')

# elapsed = 0
# while True:
#     grid.move_robots()
#     elapsed += 1
#     print(grid)
#     print(elapsed)
#     print('\n')


elapsed = 72
grid.move_robots(72)
print(grid)
while True:
    increment = 101
    grid.move_robots(increment)
    elapsed += increment
    print(grid)
    print (elapsed)
    print('\n')

# I do not have a "real" program that provide an answer and stops.
# I found the answer by trial and error

# I jumped to an assumption that a XMAS tree would be symetrical.
# I first created a true is_symetrical() method and simply printed grid to see if I was getting somewhere but after some time I gave up.

# The exercice was mentionning "most of the robots"
# I tried to compute some sort of "Symetry score"
# But it simply went nowhere 

# I ended up simply watching the stream of grids pass by in the terminal and noticed some clear pattern at 72, 173, 274
# I decided to try and print these 101 increments.
# And voila. XMAS tress spotted in the terminal



part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")


