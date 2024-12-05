import time

class Report:
    def __init__(self, levels):
        self.levels = [int(level) for level in levels]
    
    # A report is increasing of all levels are in increasing order
    def is_increasing(self):
        for i in range(len(self.levels) - 1):
            if self.levels[i] >= self.levels[i+1]:
                return False
        return True

    # A report is decreasing of all levels are in increasing order
    def is_decreasing(self):
        for i in range(len(self.levels) - 1):
            if self.levels[i] <= self.levels[i+1]:
                return False
        return True
    
    # A report is adjacent close if any two adjacent levels differ by at least one and at most three
    def is_adjacent_close(self):
        for i in range(len(self.levels) - 1):
            difference = abs(self.levels[i] - self.levels[i+1]) 
            if difference < 1 or difference > 3:
                return False
        return True
    
    # A report is valid if it is (increasing or decreasing) and adjacent close
    def is_valid(self):
        return (self.is_increasing() or self.is_decreasing()) and self.is_adjacent_close()
    
    # The problem dampener allow a single bad level
    def is_valid_with_problem_dampener(self):
        if self.is_valid():
            return True
        else:
            for i in range(len(self.levels)):
                temporary_report = Report(self.levels[:i] + self.levels[i+1:])
                if temporary_report.is_valid():
                    return True
            return False


reports = []
with open('2024/2/input.txt', mode='r') as file:
    for line in file:
        row = line.strip().split(' ')
        reports.append(Report(row))

# Part1
part1_start_time = time.time()
number_of_valid_reports = 0
for report in reports:
    if report.is_valid():
        number_of_valid_reports += 1
print(number_of_valid_reports)

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")

# Part2
part2_start_time = time.time()
number_of_valid_reports_with_problem_dampener = 0
for report in reports:
    if report.is_valid_with_problem_dampener():
        number_of_valid_reports_with_problem_dampener += 1
print(number_of_valid_reports_with_problem_dampener)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")