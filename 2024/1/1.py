import csv
import os

print(os.getcwd())

# Part 1
extracted_list1 = []
extracted_list2 = []
with open('2024/1/input.txt', mode='r') as file:
    for line in file:
        row = line.strip().split('   ')
        extracted_list1.append(row[0])
        extracted_list2.append(row[1])

sorted_list1 = sorted(extracted_list1)
sorted_list2 = sorted(extracted_list2)

distance_list = [abs(int(a)-int(b)) for a,b in zip(sorted_list1,sorted_list2)]

summed_distance = sum(distance_list)
print (summed_distance)

# Part 2
similarity_list1 = []
for number1 in extracted_list1:
    similarity = 0
    for number2 in extracted_list2:
        if number2 == number1:
            similarity += 1
    similarity_list1.append(int(number1) * similarity)

summed_similarities = sum(similarity_list1)
print(summed_similarities)