import time

class Rule:
    def __init__(self, data):
        self.numbers = [int(number) for number in data.split('|')]

class Update:
    def __init__(self, data):
        self.numbers = [int(number) for number in data.split(',')]

    def is_valid_against_rule(self, rule):
        for i in range (len(self.numbers)):
            # The number is part of a rule, it's supposed the be the first one
            if self.numbers[i] == rule.numbers[0]:
                # Because numbers[i] is supposed to be the first one, we loop on everything BEFORE it
                # If i is the first index, the rule is valid automagically
                if i == 0:
                    return True
                else:
                    for j in range(i-1):
                        # if we find the second part of the rule here, the rule is not valid
                        if self.numbers[j] == rule.numbers[1]:
                            return False
                    # Number not found, rule valid
                    return True
            # The number is part of a rule, it's supposed the be the second one
            elif self.numbers[i] == rule.numbers[1]:
                # Because numbers[i] is supposed to be the second one, we loop on everything AFTER it
                # If i is the last index, the rule is valid automagically
                if i == len(self.numbers):
                    return True
                else:
                    for j in range(len(self.numbers) - i):
                        # if we find the first part of the rule here, the rule is not valid
                        if self.numbers[i+j] == rule.numbers[0]:
                            return False
                    # Number not found, rule valid
                    return True
        # Loop ended, then the rule is not applicable, it's then valid
        return True
    
    def is_valid_against_rules(self, rules):
        # Check all rules sequentialy, return False as soon as one fails
        for rule in rules:
            if not self.is_valid_against_rule(rule):
                return False
        # No rule failed. Return true
        return True
    
    def get_middle_number(self):
        # Check if length is odd. I do not really like taking the "MIDDLE" of an even list.
        if len(self.numbers) % 2 == 1:
            return self.numbers[len(self.numbers) // 2]
        else:
            raise ValueError("The update length is even. Middle is not much sense here.")

    def reorder_update_against_rules(self, rules):
        while True:
            numbers_touched = False
            for rule in rules:
                # If a rule does not match
                if not self.is_valid_against_rule(rule):
                    # Find elements
                    first_number_index = self.numbers.index(rule.numbers[0])
                    second_number_index = self.numbers.index(rule.numbers[1])
                    # swap element
                    self.numbers[first_number_index], self.numbers[second_number_index] = self.numbers[second_number_index], self.numbers[first_number_index]
                    # Flasg the numbers as touched to check all rules at least once
                    numbers_touched = True
            if not numbers_touched:
                break
            
# Data Extraction
rules = []
updates = []
with open("2024/5/input.txt", mode="r") as file:
    rule_extraction_over = False
    for line in file:
        if line == '\n':
            rule_extraction_over = True
        elif not rule_extraction_over:
            rules.append(Rule(line.strip('\n')))
        elif rule_extraction_over:
            updates.append(Update(line.strip('\n')))

# Part 1
part1_start_time = time.time()
result1 = 0
for update in updates:
    if update.is_valid_against_rules(rules):
        result1 += update.get_middle_number()
print(result1)

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")

# Part 2
part2_start_time = time.time()
result2 = 0
for update in updates:
    if not update.is_valid_against_rules(rules):
        update.reorder_update_against_rules(rules)
        result2 += update.get_middle_number()
print(result2)

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")
