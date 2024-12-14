# Worst possible solution.
# I got sick of counting corners and all edge cases.
# I decided to "Explode" the grid twice.
# For exmaple:

# I transformed this
# A A A
# B B C
# B B C

# Into this
# A A A A A A A A A A A A
# A A A A A A A A A A A A
# A A A A A A A A A A A A
# A A A A A A A A A A A A
# B B B B B B B B C C C C
# B B B B B B B B C C C C
# B B B B B B B B C C C C
# B B B B B B B B C C C C
# B B B B B B B B C C C C
# B B B B B B B B C C C C
# B B B B B B B B C C C C
# B B B B B B B B C C C C

# This makes the counting of corners, and thus sides exptremely simple.
# But also extremely suboptimal
# I just needed to divide by 16 the area.


import time

class Grid:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
        else:
            raise ValueError("This grid is not coherent")
    
    def explode_grid(self):
        new_grid = Grid(2 * self.width, 2 * self.height, ['.'] * 4 * self.width * self.height)
        for j in range(self.height):
            for i in range(self.width):
                value = self.get(i,j)
                new_grid.set(2*i, 2*j, value)
                new_grid.set(2*i+1, 2*j, value)
                new_grid.set(2*i, 2*j+1, value)
                new_grid.set(2*i+1, 2*j+1, value)
        return new_grid
                
    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return -1
        
    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.values[x + y * self.width] = value
    
    def get_similar_neighbours(self, start_x, start_y):
        similar_neighbours = set()
        current_value = self.get(start_x, start_y)

        if self.get(start_x + 1, start_y) == current_value:
            similar_neighbours.add((start_x + 1, start_y))
        if self.get(start_x - 1, start_y) == current_value:
            similar_neighbours.add((start_x - 1, start_y))
        if self.get(start_x, start_y + 1) == current_value:
            similar_neighbours.add((start_x, start_y + 1))
        if self.get(start_x, start_y - 1) == current_value:
            similar_neighbours.add((start_x, start_y - 1))
        
        return similar_neighbours
    
    def get_different_neighbours(self, start_x, start_y):
        different_neighbours = set()
        current_value = self.get(start_x, start_y)

        if self.get(start_x + 1, start_y) != current_value:
            different_neighbours.add((start_x + 1, start_y))
        if self.get(start_x - 1, start_y) != current_value:
            different_neighbours.add((start_x - 1, start_y))
        if self.get(start_x, start_y + 1) != current_value:
            different_neighbours.add((start_x, start_y + 1))
        if self.get(start_x, start_y - 1) != current_value:
            different_neighbours.add((start_x, start_y - 1))
        
        return different_neighbours

    def get_different_corners(self, start_x, start_y):
        different_corners = set()
        current_value = self.get(start_x, start_y)

        if self.get(start_x + 1, start_y + 1) != current_value:
            different_corners.add((start_x + 1, start_y + 1))
        if self.get(start_x + 1, start_y - 1) != current_value:
            different_corners.add((start_x + 1, start_y - 1))
        if self.get(start_x - 1, start_y + 1) != current_value:
            different_corners.add((start_x - 1, start_y + 1))
        if self.get(start_x - 1, start_y - 1) != current_value:
            different_corners.add((start_x - 1, start_y - 1))
        
        return different_corners
    
    def get_different_corners_not_in_region(self, start_x, start_y, region):
        different_corners = set()
        current_value = self.get(start_x, start_y)

        if (start_x + 1, start_y + 1) not in region:
            different_corners.add((start_x + 1, start_y + 1))
        if (start_x + 1, start_y - 1) not in region:
            different_corners.add((start_x + 1, start_y - 1))
        if (start_x - 1, start_y + 1) not in region:
            different_corners.add((start_x - 1, start_y + 1))
        if (start_x - 1, start_y - 1) not in region:
            different_corners.add((start_x - 1, start_y - 1))
        
        return different_corners

    def get_region(self, start_x, start_y):
        region = set([(start_x, start_y)])
        neighbours = self.get_similar_neighbours(start_x, start_y)
        region.update(neighbours)
        while True:   
            points_to_be_added = set()
            for point in region:
                point_neighbours = self.get_similar_neighbours(point[0],point[1])
                for point_neighbour in point_neighbours:
                    if point_neighbour not in region:
                        points_to_be_added.add(point_neighbour)
            if points_to_be_added:
                region.update(points_to_be_added)
            else:
                break
        return region
    
    def get_region_area(self, region):
        return int(len(region) / 16)
    
    def get_region_full_border(self, region):
        different_neighbours = set()
        different_corners = set()
        full_border = set()

        for point in region:
            different_corners.update(self.get_different_corners_not_in_region(point[0],point[1], region))
            different_neighbours.update(self.get_different_neighbours(point[0],point[1]))
        
        full_border.update(different_neighbours)
        full_border.update(different_corners)

        return full_border

    def get_region_sides(self, region):   
        corners = 0
        full_border = self.get_region_full_border(region)

        for point in full_border:
            above = (point[0], point[1] + 1) in full_border
            below = (point[0], point[1] - 1) in full_border
            right = (point[0] + 1, point[1]) in full_border
            left = (point[0] - 1, point[1]) in full_border

            # Regular Corners
            if above and right and not (below or left):
                corners += 1
            elif above and left and not (below or right):
                corners += 1
            elif below and right and not (above or left):
                corners += 1
            elif below and left and not (above or right):
                corners += 1
        
        return corners
            
    
    def get_region_discounted_price(self, region):
        area = self.get_region_area(region)
        sides = self.get_region_sides(region)
        return area  * sides
    
    def compute_all_regions(self):
        already_part_of_regions = set()
        self.regions = []
        for j in range(self.height):
            for i in range (self.width):
                if (i,j) not in already_part_of_regions:
                    local_region = self.get_region(i,j)
                    self.regions.append(local_region)
                    already_part_of_regions.update(local_region)
    
    def compute_all_regions_price(self):
        self.total_price = 0
        for region in self.regions:
            self.total_price += self.get_region_price(region)

    def compute_all_regions_discounted_price(self):
        self.total_discounted_price = 0
        for region in self.regions:
            self.total_discounted_price += self.get_region_discounted_price(region)
        
    def __repr__(self):
        rows = [
            self.values[i * self.width:(i + 1) * self.width]
            for i in range(self.height)
        ]
        return '\n'.join(' '.join(map(str, row)) for row in rows)
        
with open("2024/12/input.txt", mode="r") as file:
    values = []
    width = 0
    height = 0
    for line in file:
        clean_line = line.strip()
        values.extend(list(clean_line))
        height += 1
        width = max(width,len(clean_line))

part2_start_time = time.time()

grid = Grid(width, height, values)
exploded_grid = grid.explode_grid().explode_grid()
exploded_grid.compute_all_regions()
exploded_grid.compute_all_regions_discounted_price()
print(exploded_grid.total_discounted_price)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")