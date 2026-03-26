import random
from selection_sort import SelectionSort
from bubble_sort import BubbleSort
from visualizer import visualize

#list of algorithms to use
algorithms = [BubbleSort, SelectionSort]

#creating unsorted list with the numbers
numbers = random.sample(range(1, 101), 100)

#loop to run all of the algorithms and visualize them
for AlgClass in algorithms:
    alg = AlgClass(numbers)
    alg.sort()
    ani = visualize(
        alg.sort_gen(),
        len(alg.numbers),
        max(alg.numbers),
        alg.elapsed,
        alg.name,
        alg.time_complexity,
        alg.space_complexity
    )
