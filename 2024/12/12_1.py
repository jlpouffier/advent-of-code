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
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return -1
    
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
        return len(region)
    
    def get_region_perimeter(self, region):
        perimeter = 0
        for point in region:
            perimeter += len(self.get_different_neighbours(point[0],point[1]))
        return perimeter
            
    def get_region_price(self, region):
        area = self.get_region_area(region)
        perimeter = self.get_region_perimeter(region)
        return area * perimeter
    
    
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
    
part1_start_time = time.time()

grid = Grid(width, height, values)
grid.compute_all_regions()
grid.compute_all_regions_price()
print(grid.total_price)

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")