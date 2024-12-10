import time

class TopographicMap:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
        else:
            raise ValueError("This grid is not coherent")
        
    def find_tailheads(self):
        self.trailhead = set()
        for j in range(self.height):
            for i in range(self.width):
                if self.get(i,j) == 0:
                    self.trailhead.add((i,j))
    
    def get_reachable_neighbours(self, x, y):
        current_value = self.get(x,y)
        reachable_neighbours = set()
        if self.get(x+1,y) == current_value + 1:
            reachable_neighbours.add((x+1,y))
        if self.get(x-1,y) == current_value + 1:
            reachable_neighbours.add((x-1,y))
        if self.get(x,y+1) == current_value + 1:
            reachable_neighbours.add((x,y+1))
        if self.get(x,y-1) == current_value + 1:
            reachable_neighbours.add((x,y-1))
        return reachable_neighbours
        
    def find_trailhead_ends(self, trailhead):
        trail_ends = set()
        reachable_neighbours = self.get_reachable_neighbours(trailhead[0] , trailhead[1])
        for neighbour in reachable_neighbours:
            if self.get(neighbour[0],neighbour[1]) == 9:
                trail_ends.add(neighbour)
            else:
                trail_ends.update(self.find_trailhead_ends(neighbour))
        return trail_ends
    
    def compute_trailhead_rating(self, trailhead):
        rating = 0
        reachable_neighbours = self.get_reachable_neighbours(trailhead[0] , trailhead[1])
        for neighbour in reachable_neighbours:
            if self.get(neighbour[0],neighbour[1]) == 9:
                rating += 1
            else:
                rating += self.compute_trailhead_rating(neighbour)
        return rating
    
    def compute_trailhead_score(self, trailhead):
        return len(self.find_trailhead_ends(trailhead))

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return -1
        
    def __repr__(self):
        rows = [
            self.values[i * self.width:(i + 1) * self.width]
            for i in range(self.height)
        ]
        return '\n'.join(' '.join(map(str, row)) for row in rows)

with open("2024/10/input.txt", mode="r") as file:
    values = []
    width = 0
    height = 0
    for line in file:
        clean_line = line.strip('\n')
        values.extend(int(number) for number in list(clean_line))
        height += 1
        width = max(width,len(clean_line))
topographic_map = TopographicMap(width,height, values)


part1_start_time = time.time()
topographic_map.find_tailheads()
topographic_map_score = 0
for trailhead in topographic_map.trailhead:
    topographic_map_score += topographic_map.compute_trailhead_score(trailhead)
print(topographic_map_score)

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")

part2_start_time = time.time()
topographic_map_rating = 0
for trailhead in topographic_map.trailhead:
    topographic_map_rating += topographic_map.compute_trailhead_rating(trailhead)
print(topographic_map_rating)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")
