import time

wall = '#'
box = 'O'
robot = '@'
outside = 'X'
available = '.'

class Grid:
    def __init__(self, width, height, values, moves):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
        else:
            raise ValueError("This grid is not coherent")
        self.moves = moves
        for j in range(height):
            for i in range(width):
                #print(f'checking {i},{j}')
                if self.get(i,j) == robot:
                    self.robot_x = i
                    self.robot_y = j

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return None
        
    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.values[x + y * self.width] = value
    
    def move(self):
        for move in moves:
            if move == 'v':
                x_direction = 0
                y_direction = 1
            elif move == '>':
                x_direction = 1
                y_direction = 0
            elif move == '<':
                x_direction = -1
                y_direction = 0
            elif move == '^':
                x_direction = 0
                y_direction = -1
            #print(f'Moving ... {move}')
            self.move_bloc(self.robot_x, self.robot_y, x_direction, y_direction)
            #print(self)
            #time.sleep(.01)

    def move_bloc(self, x, y, x_direction, y_direction, parent = True):
        new_blocs = []
        index = 0
        available_case_reached = False
        wall_reached = False
        while True:
            current_x = x + index * x_direction
            curent_y = y + index * y_direction
            next_x = x + (index + 1) * x_direction
            next_y = y + (index + 1) * y_direction

            if self.get(next_x , next_y) == available:
                new_blocs.append({
                    'x' : next_x,
                    'y' : next_y,
                    'value' : self.get(current_x, curent_y)
                })
                available_case_reached = True

            elif self.get(next_x , next_y) == wall:
                wall_reached = True
            
            else:
                new_blocs.append({
                    'x' : next_x,
                    'y' : next_y,
                    'value' : self.get(current_x, curent_y)
                })
            
            if available_case_reached or wall_reached:
                break

            else:
                index += 1

        if available_case_reached:
            new_blocs.append({
                'x' : x,
                'y' : y,
                'value' : available
            })
            self.robot_x = self.robot_x + x_direction
            self.robot_y = self.robot_y + y_direction
                
            for bloc in new_blocs:
                self.set(bloc['x'],bloc['y'],bloc['value'])
    
    def get_gps_score(self):
        score = 0
        for j in range(height):
            for i in range(width):
                #print(f'checking {i},{j}')
                if self.get(i,j) == box:
                    score += i + 100 * j
        return score

    def __repr__(self):
        rows = [
            self.values[i * self.width:(i + 1) * self.width]
            for i in range(self.height)
        ]
        return '\n'.join(' '.join(map(str, row)) for row in rows)

with open("2024/15/input.txt", mode="r") as file:
    grid_values = []
    width = 0
    height = 0
    moves = []
    grid_data = True
    for line in file:
        if line == '\n':
            grid_data = False
        if grid_data:
            clean_line = line.strip()
            grid_values.extend(list(clean_line))
            height += 1
            width = max(width,len(clean_line))
        else:
            clean_line = line.strip()
            moves.extend(list(clean_line))
        
part1_start_time = time.time()

grid = Grid(width, height, grid_values, moves)
#print(grid)
grid.move()
print(grid.get_gps_score())

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")