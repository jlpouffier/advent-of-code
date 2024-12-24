import time

class Grid:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
        else:
            raise ValueError("This grid is not coherent")
        self.start = self.get_start()
        self.end = self.get_end()
        self.visited = {}
        self.visited[self.start[0], self.start[1] , '>'] = 0
        self.to_explore = []
        self.to_explore.append((self.start[0], self.start[1] , '>'))

        self.best_seats = set()
        self.to_explore_for_seats = []
        
    def get_start(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.get(i,j) == 'S':
                    return (i, j)
        return None

    def get_end(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.get(i,j) == 'E':
                    return (i, j)
        return None
        
    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return None
        
    def explore(self):
        to_explore = []
        for start in self.to_explore:
            x = start[0]
            y = start[1]
            orientation = start[2]

            current_score = self.visited[x,y,orientation]
            # Going down v
            if self.get(x, y + 1) in ['.','E']:
                increment = 1 if orientation == 'v' else 1001
                new_score = current_score + increment
                if (x , y + 1 , 'v') not in self.visited or self.visited[x , y + 1 , 'v'] > new_score:
                    self.visited[x , y + 1 , 'v'] = new_score
                    if (x, y + 1) != self.end:
                        to_explore.append((x, y + 1, 'v'))
                
            # Going up ^
            if self.get(x, y - 1) in ['.','E']:
                increment = 1 if orientation == '^' else 1001
                new_score = current_score + increment
                if (x , y - 1 , '^') not in self.visited or self.visited[x , y - 1 , '^'] > new_score:
                    self.visited[x , y - 1 , '^'] = new_score
                    if (x, y - 1) != self.end:
                        to_explore.append((x, y - 1, '^'))

            # Going right >
            if self.get(x + 1, y) in ['.','E']:
                increment = 1 if orientation == '>' else 1001
                new_score = current_score + increment
                if (x + 1 , y , '>') not in self.visited or self.visited[x + 1 , y , '>'] > new_score:
                    self.visited[x + 1 , y , '>'] = new_score
                    if (x + 1 , y) != self.end:
                        to_explore.append((x + 1 , y, '>'))

            # Going left <
            if self.get(x - 1, y) in ['.','E']:
                increment = 1 if orientation == '<' else 1001
                new_score = current_score + increment
                if (x - 1 , y , '<') not in self.visited or self.visited[x - 1 , y , '<'] > new_score:
                    self.visited[x - 1 , y , '<'] = new_score
                    if (x + 1 , y) != self.end:
                        to_explore.append((x - 1 , y, '<'))
            
        self.to_explore = to_explore

    def solve(self):
        while True:
            self.explore()
            if len(self.to_explore) == 0:
                break
    
    def explore_for_seats(self):
        to_explore_for_seats = []
        for place in self.to_explore_for_seats:
            x = place[0]
            y = place[1]
            orientation = place[2]
            score = self.visited[ x , y , orientation ]
            
            if orientation == '^':
                for orientation , old_score in [('^',score - 1),('>',score - 1001),('v',score - 1001),('<',score - 1001)]:
                    if ( x , y + 1 , orientation ) in self.visited and self.visited[ x , y + 1 , orientation ] == old_score:
                        self.best_seats.add((x , y + 1))
                        #if (x , y + 1) != self.start:
                        to_explore_for_seats.append((x , y + 1 , orientation))
               
            elif orientation == '>':
                for orientation , old_score in [('>',score - 1),('^',score - 1001),('v',score - 1001),('<',score - 1001)]:
                    if ( x - 1 , y , orientation ) in self.visited and self.visited[ x - 1 , y , orientation ] == old_score:
                        self.best_seats.add((x - 1 , y))
                        #if (x - 1 , y) != self.start:
                        to_explore_for_seats.append((x - 1 , y , orientation))
            
            elif orientation == 'v':
                for orientation , old_score in [('v',score - 1),('>',score - 1001),('^',score - 1001),('<',score - 1001)]:
                    if ( x , y - 1 , orientation ) in self.visited and self.visited[ x , y - 1 , orientation ] == old_score:
                        self.best_seats.add((x , y - 1))
                        #if (x , y - 1) != self.start:
                        to_explore_for_seats.append((x , y - 1 , orientation))
            
            elif orientation == '<':
                for orientation , old_score in [('<',score - 1),('>',score - 1001),('v',score - 1001),('^',score - 1001)]:
                    if ( x + 1 , y , orientation ) in self.visited and self.visited[ x + 1 , y , orientation ] == old_score:
                        self.best_seats.add((x + 1 , y))
                        #if (x + 1 , y) != self.start:
                        to_explore_for_seats.append((x + 1 , y , orientation))
        self.to_explore_for_seats = to_explore_for_seats
            
    def solve_for_seat(self):
        while True:
            #print(self)
            #print('\n')
            #time.sleep(.01)
            self.explore_for_seats()
            if len(self.to_explore_for_seats) == 0:
                break
               
    def get_end_score(self):
        orientations = ['v','<','>','^']
        scores = []
        x = self.end[0]
        y = self.end[1]
        self.best_seats.add((x , y))
        for orientation in orientations:
            if (x , y , orientation) in self.visited:
                scores.append(self.visited[x , y , orientation])     
        for orientation in orientations:
            if (x , y , orientation) in self.visited and self.visited[x , y , orientation] == min(scores):
                self.to_explore_for_seats.append((x , y , orientation))
        return min(scores)

    def __repr__(self):
        rows = []
        for j in range(self.height):
            row = []
            for i in range(self.width):
                if (i,j) in self.best_seats:
                    row.append('O')
                else:
                    row.append(self.get(i,j))
            rows.append(row)
        return '\n'.join(' '.join(map(str, row)) for row in rows)


with open("2024/16/input.txt", mode="r") as file:
    grid_values = []
    width = 0
    height = 0
    for line in file:
        clean_line = line.strip()
        grid_values.extend(list(clean_line))
        height += 1
        width = max(width,len(clean_line))

part1_start_time = time.time()

grid = Grid(width, height, grid_values)
grid.solve()
print(grid.get_end_score())

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")

part2_start_time = time.time()

grid.solve_for_seat()
print(len(grid.best_seats))

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")