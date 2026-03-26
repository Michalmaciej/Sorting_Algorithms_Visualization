from base_sort import BaseSort
from decorators import measure_time

class MergeSort(BaseSort):
    time_complexity = "O(n log n)"
    space_complexity = "O(n)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        self._merge_sort(nums, 0, len(nums) - 1)
        return nums

    def _merge_sort(self, nums, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(nums, left, mid)
            self._merge_sort(nums, mid + 1, right)
            self._merge(nums, left, mid, right)

    def _merge(self, nums, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = nums[left + i]
        for j in range(n2):
            R[j] = nums[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1

    def sort_gen(self):
        nums = self.numbers.copy()
        yield (nums.copy(), -1, -1, (0, 0))
        yield from self._merge_sort_gen(nums, 0, len(nums) - 1)
        yield (nums.copy(), -1, -1, (len(nums), 0))

    def _merge_sort_gen(self, nums, left, right):
        if left < right:
            mid = (left + right) // 2
            yield from self._merge_sort_gen(nums, left, mid)
            yield from self._merge_sort_gen(nums, mid + 1, right)
            yield from self._merge_gen(nums, left, mid, right)

    def _merge_gen(self, nums, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = nums[left + i]
        for j in range(n2):
            R[j] = nums[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
            yield (nums.copy(), k - 1, left + i if i < n1 else mid + 1 + j, (0, 0))

        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
            yield (nums.copy(), k - 1, -1, (0, 0))

        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1
            yield (nums.copy(), k - 1, -1, (0, 0))
