import random

#creating unsorted list with the numbers
numbers = random.sample(range(1, 1001), 500)

for i in range(len(numbers)-1):
    smallest = 1001
    index = 0
    for j in range(i+1, len(numbers)):
        if numbers[j] < smallest:
            smallest = numbers[j]
            index = j
    if numbers[i] > smallest:
        numbers[i], numbers[index] = smallest, numbers[i]

#print(numbers[400:500])