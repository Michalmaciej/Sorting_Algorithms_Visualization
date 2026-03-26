# Sorting Algorithms Visualization

An interactive visualization of 14 sorting algorithms built in Python using Matplotlib animations. Each algorithm is implemented as a class inheriting from a common base, with real-time bar chart animations showing comparisons, swaps, and sorted regions.

---

## Algorithms

| Algorithm | Time Complexity | Space Complexity | Link |
|---|---|---|---|
| Selection Sort | O(n²) | O(1) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/) |
| Bubble Sort | O(n²) | O(1) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/) |
| Insertion Sort | O(n²) | O(1) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/) |
| Merge Sort | O(n log n) | O(n) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/merge-sort/) |
| Quick Sort | O(n log n) | O(log n) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/) |
| Heap Sort | O(n log n) | O(1) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/heap-sort/) |
| Counting Sort | O(n + k) | O(k) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/counting-sort/) |
| Radix Sort | O(n * k) | O(n + k) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/radix-sort/) |
| Bucket Sort | O(n + k) | O(n + k) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/bucket-sort-2/) |
| Cycle Sort | O(n²) | O(1) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/cycle-sort/) |
| Pigeonhole Sort | O(n + range) | O(range) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/pigeonhole-sort/) |
| Tim Sort | O(n log n) | O(n) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/timsort/) |
| Intro Sort | O(n log n) | O(log n) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/introsort-cs-sorting-weapon/) |
| 3-Way Merge Sort | O(n log₃ n) | O(n) | [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/3-way-merge-sort/) |

---

## Project Structure

```
sorting/
├── main.py                   # entry point — runs all algorithms
├── base_sort.py              # abstract base class for all algorithms
├── decorators.py             # @measure_time decorator
├── visualizer.py             # matplotlib animation function
├── selection_sort.py
├── bubble_sort.py
├── insertion_sort.py
├── merge_sort.py
├── quick_sort.py
├── heap_sort.py
├── counting_sort.py
├── radix_sort.py
├── bucket_sort.py
├── cycle_sort.py
├── pigeonhole_sort.py
├── tim_sort.py
├── intro_sort.py
├── three_way_merge_sort.py
└── records/                  # screen recordings of each algorithm
```

---

## Color Legend

| Color | Meaning |
|---|---|
| 🔵 Blue | Active element (key, pivot, or current position) |
| 🔴 Red | Element being compared against |
| 🟢 Green | Element in its final sorted position |
| ⬜ Grey | Unsorted element |

---

## Interesting Implementation Details

**Generator-based streaming** — each algorithm implements `sort_gen()` as a Python generator that `yield`s snapshots of the array at each step. Matplotlib's `FuncAnimation` consumes these frames directly without storing them all in memory.

**`yield from` with return value** — recursive algorithms like QuickSort use `pi = yield from self._partition_gen(...)`. In Python 3, a generator can `return` a value that gets propagated via `yield from`, allowing recursion to work naturally with generators.

**Two sorted-region formats** — simple algorithms (Selection, Bubble, Insertion) use a `(sorted_left, sorted_right)` tuple to mark sorted ranges. Algorithms with non-contiguous sorted positions (QuickSort, HeapSort, CycleSort) use a `frozenset` of finalized indices instead. The visualizer handles both.

**Abstract base class** — `BaseSort` uses Python's `abc.ABC` with `@abstractmethod`, so any new algorithm that forgets to implement `sort()` or `sort_gen()` raises a `TypeError` at instantiation, not at call time.

**`@measure_time` decorator** — writes elapsed time directly to `self.elapsed` via `self` in the wrapper, so the result is attached to the object and accessible after sorting without returning it alongside the sorted array.

---

## How to Run

**Requirements:**
```bash
pip install matplotlib
```

**Run all algorithms:**
```bash
python main.py
```

Each algorithm opens its own window. Close it to proceed to the next one.

**Run a single algorithm** — edit `algorithms` list in `main.py`:
```python
algorithms = [QuickSort]
```

**Change array size or range** — edit in `main.py`:
```python
numbers = random.sample(range(1, 101), 100)
```

---

## Recordings

### Selection Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/selection%20sort.mp4

### Bubble Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/bubble%20sort.mp4

### Insertion Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/insertion%20sort.mp4

### Merge Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/merge%20sort.mp4

### Quick Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/quick%20sort.mp4

### Heap Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/heap%20sort.mp4

### Counting Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/counting%20sort.mp4

### Radix Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/radix%20sort.mp4

### Bucket Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/bucket%20sort.mp4

### Cycle Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/cycle%20sort.mp4

### Pigeonhole Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/pigeonhole%20sort.mp4

### Tim Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/tim%20sort.mp4

### Intro Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/intro%20sort.mp4

### 3-Way Merge Sort
https://github.com/Michalmaciej/Sorting_Algorithms_Visualization/blob/pigeon/records/threeway%20merge%20sort.mp4
