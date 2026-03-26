from base_sort import BaseSort
from decorators import measure_time

class HeapSort(BaseSort):
    time_complexity = "O(n log n)"
    space_complexity = "O(log n)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._heapify(nums, i, 0)

        return nums

    def _heapify(self, nums, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and nums[l] > nums[largest]:
            largest = l

        if r < n and nums[r] > nums[largest]:
            largest = r

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self._heapify(nums, n, largest)

    def sort_gen(self):
        nums = self.numbers.copy()
        n = len(nums)
        sorted_set = set()
        yield (nums.copy(), -1, -1, frozenset(sorted_set))

        for i in range(n // 2 - 1, -1, -1):
            yield from self._heapify_gen(nums, n, i, sorted_set)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            sorted_set.add(i)
            yield (nums.copy(), 0, i, frozenset(sorted_set))
            yield from self._heapify_gen(nums, i, 0, sorted_set)

        sorted_set.add(0)
        yield (nums.copy(), -1, -1, frozenset(sorted_set))

    def _heapify_gen(self, nums, n, i, sorted_set):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and nums[l] > nums[largest]:
            largest = l

        if r < n and nums[r] > nums[largest]:
            largest = r

        yield (nums.copy(), i, largest, frozenset(sorted_set))

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            yield (nums.copy(), i, largest, frozenset(sorted_set))
            yield from self._heapify_gen(nums, n, largest, sorted_set)
