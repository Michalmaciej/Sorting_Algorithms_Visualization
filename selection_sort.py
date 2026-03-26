import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#creating unsorted list with the numbers
numbers = random.sample(range(1, 101), 100)

#decorator to measure time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        return result, elapsed
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

#selection sort algorithm generating data to animation
def selection_sort_gen(numbers):
    yield (numbers.copy(), -1, -1, -1)
    for i in range(len(numbers)-1):
        smallest = 0
        index = 0
        for j in range(i+1, len(numbers)):
            if numbers[j] < smallest or smallest == 0:
                smallest = numbers[j]
                index = j
            yield (numbers.copy(), i, j, i - 1)
        if numbers[i] > smallest:
            numbers[i], numbers[index] = smallest, numbers[i]
        yield (numbers.copy(), -1, -1, i)
    yield (numbers.copy(), -1, -1, len(numbers) - 1)

#function to visualize sorting proces
def visualize(gen, size, max_val, elapsed):
    fig, ax = plt.subplots(facecolor="#2b2b2b")
    ax.set_facecolor("#2b2b2b")
    bars = ax.bar(range(size), [0] * size, color="#c0c0c0", edgecolor="#1a1a1a", linewidth=0.5)
    ax.set_ylim(0, max_val * 1.05)
    ax.set_title("Selection Sort", color="white")
    ax.tick_params(colors="white")

    for spine in ax.spines.values():
        spine.set_edgecolor("#444")

    info = f"Czas: {elapsed:.10f}s  |  Złożoność czasowa: O(n²)  |  Złożoność miejsca: O(1)"
    fig.text(0.5, 0.01, info, ha="center", color="white", fontsize=9)

    def update(frame):
        arr, i, j, sorted_up_to = frame
        for idx, (bar, val) in enumerate(zip(bars, arr)):
            bar.set_height(val)
            if idx <= sorted_up_to:
                bar.set_facecolor("#50c878")
            elif idx == i:
                bar.set_facecolor("#87ceeb")
            elif idx == j:
                bar.set_facecolor("#ff6b6b")
            else:
                bar.set_facecolor("#c0c0c0")
            bar.set_edgecolor("#1a1a1a")

    ani = animation.FuncAnimation(
        fig, update,
        frames=gen,
        interval=10,
        repeat=False,
        cache_frame_data=False
    )
    plt.show(block=True)
    return ani

#sorting and measuring time
sorted_numbers, elapsed = selection_sort(numbers.copy())

#vizualization
ani = visualize(selection_sort_gen(numbers.copy()), len(numbers), max(numbers), elapsed)
