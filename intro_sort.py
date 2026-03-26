import math
from base_sort import BaseSort
from decorators import measure_time

class IntroSort(BaseSort):
    time_complexity = "O(n log n)"
    space_complexity = "O(log n)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        depth_limit = 2 * math.floor(math.log2(len(nums)))
        self._introsort(nums, 0, len(nums) - 1, depth_limit)
        return nums

    def _introsort(self, nums, begin, end, depth_limit):
        size = end - begin
        if size < 16:
            self._insertion_sort(nums, begin, end)
            return
        if depth_limit == 0:
            self._heapsort(nums, begin, end)
            return
        pivot = self._median_of_three(nums, begin, begin + size // 2, end)
        nums[pivot], nums[end] = nums[end], nums[pivot]
        partition_point = self._partition(nums, begin, end)
        self._introsort(nums, begin, partition_point - 1, depth_limit - 1)
        self._introsort(nums, partition_point + 1, end, depth_limit - 1)

    def _insertion_sort(self, nums, begin, end):
        for i in range(begin + 1, end + 1):
            key = nums[i]
            j = i - 1
            while j >= begin and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

    def _heapsort(self, nums, begin, end):
        n = end - begin + 1
        for i in range(begin + n // 2 - 1, begin - 1, -1):
            self._heapify(nums, begin, end, i)
        for i in range(end, begin, -1):
            nums[begin], nums[i] = nums[i], nums[begin]
            self._heapify(nums, begin, i - 1, begin)

    def _heapify(self, nums, begin, end, i):
        largest = i
        l = begin + 2 * (i - begin) + 1
        r = begin + 2 * (i - begin) + 2
        if l <= end and nums[l] > nums[largest]:
            largest = l
        if r <= end and nums[r] > nums[largest]:
            largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self._heapify(nums, begin, end, largest)

    def _partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def _median_of_three(self, nums, a, b, d):
        A, B, C = nums[a], nums[b], nums[d]
        if A <= B <= C or C <= B <= A:
            return b
        if B <= A <= C or C <= A <= B:
            return a
        return d

    def sort_gen(self):
        nums = self.numbers.copy()
        depth_limit = 2 * math.floor(math.log2(len(nums)))
        yield (nums.copy(), -1, -1, (0, 0))
        yield from self._introsort_gen(nums, 0, len(nums) - 1, depth_limit)
        yield (nums.copy(), -1, -1, (len(nums), 0))

    def _introsort_gen(self, nums, begin, end, depth_limit):
        size = end - begin
        if size < 16:
            yield from self._insertion_sort_gen(nums, begin, end)
            return
        if depth_limit == 0:
            yield from self._heapsort_gen(nums, begin, end)
            return
        pivot = self._median_of_three(nums, begin, begin + size // 2, end)
        nums[pivot], nums[end] = nums[end], nums[pivot]
        yield (nums.copy(), pivot, end, (0, 0))
        pi = yield from self._partition_gen(nums, begin, end)
        yield from self._introsort_gen(nums, begin, pi - 1, depth_limit - 1)
        yield from self._introsort_gen(nums, pi + 1, end, depth_limit - 1)

    def _insertion_sort_gen(self, nums, begin, end):
        for i in range(begin + 1, end + 1):
            key = nums[i]
            j = i - 1
            yield (nums.copy(), i, j, (0, 0))
            while j >= begin and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
                yield (nums.copy(), j + 1, j, (0, 0))
            nums[j + 1] = key
            yield (nums.copy(), j + 1, -1, (0, 0))

    def _heapsort_gen(self, nums, begin, end):
        n = end - begin + 1
        for i in range(begin + n // 2 - 1, begin - 1, -1):
            yield from self._heapify_gen(nums, begin, end, i)
        for i in range(end, begin, -1):
            nums[begin], nums[i] = nums[i], nums[begin]
            yield (nums.copy(), begin, i, (0, 0))
            yield from self._heapify_gen(nums, begin, i - 1, begin)

    def _heapify_gen(self, nums, begin, end, i):
        largest = i
        l = begin + 2 * (i - begin) + 1
        r = begin + 2 * (i - begin) + 2
        if l <= end and nums[l] > nums[largest]:
            largest = l
        if r <= end and nums[r] > nums[largest]:
            largest = r
        yield (nums.copy(), i, largest, (0, 0))
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            yield (nums.copy(), i, largest, (0, 0))
            yield from self._heapify_gen(nums, begin, end, largest)

    def _partition_gen(self, nums, low, high):
        pivot_idx = high
        i = low - 1
        for j in range(low, high):
            yield (nums.copy(), pivot_idx, j, (0, 0))
            if nums[j] <= nums[pivot_idx]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                yield (nums.copy(), pivot_idx, i, (0, 0))
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        yield (nums.copy(), i + 1, -1, (0, 0))
        return i + 1
