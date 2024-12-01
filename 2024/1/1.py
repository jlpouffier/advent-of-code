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
print("Extracted Lists:")
print (extracted_list1)
print (extracted_list2)

sorted_list1 = sorted(extracted_list1)
sorted_list2 = sorted(extracted_list2)
print("Sorted Lists:")
print (sorted_list1)
print (sorted_list2)

distance_list = [abs(int(a)-int(b)) for a,b in zip(sorted_list1,sorted_list2)]
print("Distance List:")
print (distance_list)

summed_distance = sum(distance_list)
print("Summed distance:")
print (summed_distance)

# Part 2
similarity_list1 = []
for number1 in extracted_list1:
    similarity = 0
    for number2 in extracted_list2:
        if number2 == number1:
            similarity += 1
    similarity_list1.append(int(number1) * similarity)
print("Similarity list:")
print(similarity_list1)

summed_similarities = sum(similarity_list1)
print("Summed similarities:")
print(summed_similarities)