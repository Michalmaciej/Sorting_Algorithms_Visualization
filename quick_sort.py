from base_sort import BaseSort
from decorators import measure_time

class QuickSort(BaseSort):
    time_complexity = "O(n log n)"
    space_complexity = "O(n)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort(self, nums, low, high):
        if low < high:
            pi = self._partition(nums, low, high)
            self._quick_sort(nums, low, pi - 1)
            self._quick_sort(nums, pi + 1, high)

    def _partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def sort_gen(self):
        nums = self.numbers.copy()
        sorted_set = set()
        yield (nums.copy(), -1, -1, frozenset(sorted_set))
        yield from self._quick_sort_gen(nums, 0, len(nums) - 1, sorted_set)
        yield (nums.copy(), -1, -1, frozenset(range(len(nums))))

    def _quick_sort_gen(self, nums, low, high, sorted_set):
        if low == high:
            sorted_set.add(low)
            yield (nums.copy(), -1, -1, frozenset(sorted_set))
        elif low < high:
            pi = yield from self._partition_gen(nums, low, high, sorted_set)
            sorted_set.add(pi)
            yield (nums.copy(), -1, -1, frozenset(sorted_set))
            yield from self._quick_sort_gen(nums, low, pi - 1, sorted_set)
            yield from self._quick_sort_gen(nums, pi + 1, high, sorted_set)

    def _partition_gen(self, nums, low, high, sorted_set):
        pivot_idx = high
        i = low - 1
        for j in range(low, high):
            yield (nums.copy(), pivot_idx, j, frozenset(sorted_set))
            if nums[j] < nums[pivot_idx]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                yield (nums.copy(), pivot_idx, i, frozenset(sorted_set))
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        yield (nums.copy(), i + 1, -1, frozenset(sorted_set))
        return i + 1
