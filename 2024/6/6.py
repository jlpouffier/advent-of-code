import copy
import time

available_spot = '.'
obstruction = '#'
outside = '0'
# Definting orientation as such so that we can rotate rigth 90 degrees by doing orientation = (orientation + 1) % 4
north = 0
east = 1
south = 2
west = 3

north_char = '^'
east_char = '>'
south_char = 'v'
west_chat = '<'

class Guard:
    def __init__(self, x, y, orientation, grid_width, grid_height):
        if x < grid_width and y < grid_height:
            self.x = x
            self.y = y
            self.orientation = orientation
            self.visited_places = [
                {
                    'x': self.x,
                    'y': self.y,
                    'orientation': self.orientation
                }
            ]
            self.is_in_a_loop = False
            self.is_outside = False
        else:
            raise ValueError("The guard cannot be created outside the grid boundaries")

    def rotate(self):
        self.orientation = (self.orientation + 1) % 4
        self.visited_places.append({
            'x': self.x,
            'y': self.y,
            'orientation': self.orientation
        })
    
    def fetch_next_bloc(self, grid):
        if self.orientation == north:
            return grid.get(self.x, self.y - 1)
        elif self.orientation == east:
            return grid.get(self.x + 1, self.y)
        elif self.orientation == south:
            return grid.get(self.x, self.y + 1)
        else:
            return grid.get(self.x - 1, self.y)
    
    def move(self):
        if self.orientation == north:
            self.y -= 1
        elif self.orientation == east:
            self.x += 1
        elif self.orientation == south:
            self.y += 1
        else:
            self.x -= 1
        if not self.has_visited_on_same_orientation(self.x, self.y, self.orientation):
            self.visited_places.append({
                'x': self.x,
                'y': self.y,
                'orientation': self.orientation
            })
        else:
            self.is_in_a_loop = True

    def compute_step(self,grid):
        next_bloc = self.fetch_next_bloc(grid)
        if next_bloc == obstruction:
            self.rotate()
        elif next_bloc == available_spot:
            self.move()
        elif next_bloc == outside:
            self.is_outside = True

    def has_visited(self, i,j):
        for place in self.visited_places:
            if place['x'] == i and place['y'] == j:
                return True
        return False

    def has_visited_on_same_orientation(self, i, j, orientation):
        for place in self.visited_places:
            if place['x'] == i and place['y'] == j and place['orientation'] == orientation:
                return True
        return False
    
    def get_uniquely_visited_location(self):
        unique_places = set()
        for place in self.visited_places:
            coordinates = (place['x'], place['y'])
            unique_places.add(coordinates)
        return unique_places
    
    def get_printable_orientation(self):
        if self.orientation == north:
            return north_char
        elif self.orientation == east:
            return east_char
        elif self.orientation == south:
            return south_char
        else:
            return west_chat

class Grid:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
        else:
            raise ValueError("This grid is not coherent")
    
    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return outside
    
    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.values[x + y * self.width] = value
        else:
            raise ValueError("Cannot change somerhing outside of the grid")

    def add_obstruction(self, i, j):
        new_grid = Grid(self.width, self.height, copy.deepcopy(self.values))
        if new_grid.get(i,j) != obstruction:
            new_grid.set(i,j,obstruction)
        return new_grid

def print_guard_on_grid(guard, grid):
 # Construct rows
    rows = []
    for j in range (grid.height):
        row = ""
        for i in range(grid.width):
            if i == guard.x and j == guard.y:
                row += guard.get_printable_orientation()
            elif guard.has_visited(i,j):
                row += 'X'
            else:
                row += grid.get(i,j)
        rows.append(row)
    print('\n'.join(' '.join(row) for row in rows))

with open("2024/6/input.txt", mode="r") as file:
    values = []
    width = 0
    height = 0
    guard_x = 0
    guard_y = 0
    for line in file:
        clean_line = line.strip('\n')
        # Check if guard is in the line
        if north_char in line:
            guard_y = height
            guard_x = clean_line.find(north_char)
            # Remove guard from grid
            clean_line = clean_line.replace(north_char, '.')
        values.extend(list(clean_line))
        height += 1
        width = max(width,len(clean_line))
    # Create guard
    guard = Guard(guard_x, guard_y, north, width, height)
    # create grip
    grid = Grid(width, height, values)

# Part 1
part1_start_time = time.time()
while True:
    #print_guard_on_grid(guard, grid)
    #print('\n')
    guard.compute_step(grid)
    if guard.is_outside:
        break
print(len(guard.get_uniquely_visited_location()))
part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")

# Part 2
part2_start_time = time.time()
visited_position = guard.get_uniquely_visited_location()
total_positions = len(visited_position)
options = 0
for id, position in enumerate(visited_position):
    progress = (id + 1) / total_positions * 100 
    grid = Grid(width, height, values)
    guard = Guard(guard_x, guard_y, north, width, height)
    if grid.get(position[0],position[1]) == available_spot and (guard.x != position[0] or guard.y != position[1]) :
        new_grid = grid.add_obstruction(position[0],position[1])
        while True:
            guard.compute_step(new_grid)
            if guard.is_outside:
                break
            if guard.is_in_a_loop:
                options += 1
                #print(f"Progress: {progress:.2f}%")
                #print(f"Loops found: {str(options)}")
                break
print(options)
part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")