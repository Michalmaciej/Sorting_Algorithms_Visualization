import random
import time

#decorator to measure time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} takes {end_time - start_time:.6f}s")
        return result
    return wrapper

#selection sort algorithm with time meausure
@measure_time
def selection_sort(numbers):
    for i in range(len(numbers)-1):
        smallest = 0
        index = 0
        for j in range(i+1, len(numbers)):
            if numbers[j] < smallest or smallest == 0: 
                smallest = numbers[j]
                index = j
        if numbers[i] > smallest:
            numbers[i], numbers[index] = smallest, numbers[i]
    return numbers

#creating unsorted list with the numbers
numbers = random.sample(range(1, 20001), 20000)
print(selection_sort(numbers)[0:100])
