import time

class Grid:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
        else:
            raise ValueError("This grid is not coherent")
    
    def get(self, x, y):
        if x < self.width and y < self.height:
            return self.values[x + y * self.width]
        else:
            raise ValueError("This is outside the grid")
    
    # Extract Subgrid
    def extract_sub_grid(self, start_x, start_y, sub_width, sub_height):
        if start_x >= self.width:
            raise ValueError("The begining of the subgrid is outside the grid")
        elif start_y >= self.height:
            raise ValueError("The begining of the subgrid is outside the grid")
        elif start_x + sub_width - 1 >= self.width:
            raise ValueError("The end of the subgrid is outside the grid")
        elif start_y + sub_height - 1 >= self.height:
            raise ValueError("The end of the subgrid is outside the grid")
        else:
            values = []
            for j in range(sub_height):
                for i in range(sub_width):
                    values.append(self.get(start_x + i, start_y + j))
            return Grid(sub_width, sub_height, values)
    
    # Check if subgrid is mathching a certain mask
    def is_sub_grid_matching_mask(self, start_x, start_y, mask):
        sub_grid = self.extract_sub_grid(start_x, start_y, mask.width, mask.height)
        for j in range(sub_grid.height):
            for i in range(sub_grid.width):
                if mask.get(i,j) != ' ':
                    if mask.get(i,j) != sub_grid.get(i,j):
                        return False
        return True
    
    # Count all subgrid mathcing a mask
    def count_subgrid_matching_mask(self, mask):
        count = 0
        for j in range(self.height - mask.height + 1):
            for i in range(self.width - mask.width + 1):
                if self.is_sub_grid_matching_mask(i, j, mask):
                    count += 1
        return count

part2_start_time = time.time()
# Extract Grid
grid_values = []
grid_width = 0
grid_height = 0
with open("2024/4/input.txt", mode="r") as file:
    for line in file:
        clean_line = line.strip()
        grid_values.extend(list(clean_line))
        grid_height += 1
        grid_width = max(grid_width,len(clean_line))
grid = Grid(grid_width, grid_height, grid_values)

# Create Masks
# M.S
# .A.
# M.S
mask1 = Grid(3,3,['M', ' ', 'S', ' ', 'A', ' ', 'M', ' ', 'S'])
# M.M
# .A.
# S.S
mask2 = Grid(3,3,['M', ' ', 'M', ' ', 'A', ' ', 'S', ' ', 'S'])
# S.M
# .A.
# S.M
mask3 = Grid(3,3,['S', ' ', 'M', ' ', 'A', ' ', 'S', ' ', 'M'])
# S.S
# .A.
# M.M
mask4 = Grid(3,3,['S', ' ', 'S', ' ', 'A', ' ', 'M', ' ', 'M'])

matches = 0
matches += grid.count_subgrid_matching_mask(mask1)
matches += grid.count_subgrid_matching_mask(mask2)
matches += grid.count_subgrid_matching_mask(mask3)
matches += grid.count_subgrid_matching_mask(mask4)

print(matches)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")