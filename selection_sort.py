import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#creating unsorted list with the numbers
numbers = random.sample(range(1, 20001), 20000)

#creating list of lists to animate sorting
sel_sort_frames = []

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
    sel_sort_frames.append(numbers.copy())
    for i in range(len(numbers)-1):
        smallest = 0
        index = 0
        for j in range(i+1, len(numbers)):
            if numbers[j] < smallest or smallest == 0: 
                smallest = numbers[j]
                index = j
        if numbers[i] > smallest:
            numbers[i], numbers[index] = smallest, numbers[i]
            sel_sort_frames.append(numbers.copy())
    return numbers

#creating unsorted list with the numbers
numbers = random.sample(range(1, 101), 100)
sorted_numbers, elapsed = selection_sort(numbers)
print(sorted_numbers[0:100])
print(f"Czas: {elapsed:.6f}s")

def visualize(frames):
    fig, ax = plt.subplots(facecolor="#2b2b2b")
    ax.set_facecolor("#2b2b2b")
    bars = ax.bar(range(len(frames[0])), frames[0], color="#c0c0c0")
    ax.set_title("Selection Sort", color="white")
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_edgecolor("#444")

    def update(frame_idx):
        for bar, val in zip(bars, frames[frame_idx]):
            bar.set_height(val)
        ax.set_xlabel(f"Krok {frame_idx + 1}/{len(frames)}", color="white")

    ani = animation.FuncAnimation(
        fig, update,
        frames=len(frames),
        interval=200,
        repeat=False
    )
    plt.show()
    return ani

ani = visualize(sel_sort_frames)
