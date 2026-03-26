from base_sort import BaseSort
from decorators import measure_time

class ThreeWayMergeSort(BaseSort):
    time_complexity = "O(n log₃ n)"
    space_complexity = "O(n)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        self._three_way_merge_sort(nums, 0, len(nums) - 1)
        return nums

    def _three_way_merge_sort(self, nums, left, right):
        if left >= right:
            return

        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3

        self._three_way_merge_sort(nums, left, mid1)
        self._three_way_merge_sort(nums, mid1 + 1, mid2)
        self._three_way_merge_sort(nums, mid2 + 1, right)
        self._merge(nums, left, mid1, mid2, right)

    def _merge(self, nums, left, mid1, mid2, right):
        size1 = mid1 - left + 1
        size2 = mid2 - mid1
        size3 = right - mid2

        left_arr = nums[left:left + size1]
        mid_arr = nums[mid1 + 1:mid1 + 1 + size2]
        right_arr = nums[mid2 + 1:mid2 + 1 + size3]

        i = j = k = 0
        index = left

        while i < size1 or j < size2 or k < size3:
            min_value = float('inf')
            min_idx = -1

            if i < size1 and left_arr[i] < min_value:
                min_value = left_arr[i]
                min_idx = 0
            if j < size2 and mid_arr[j] < min_value:
                min_value = mid_arr[j]
                min_idx = 1
            if k < size3 and right_arr[k] < min_value:
                min_value = right_arr[k]
                min_idx = 2

            if min_idx == 0:
                nums[index] = left_arr[i]
                i += 1
            elif min_idx == 1:
                nums[index] = mid_arr[j]
                j += 1
            else:
                nums[index] = right_arr[k]
                k += 1

            index += 1

    def sort_gen(self):
        nums = self.numbers.copy()
        yield (nums.copy(), -1, -1, (0, 0))
        yield from self._three_way_merge_sort_gen(nums, 0, len(nums) - 1)
        yield (nums.copy(), -1, -1, (len(nums), 0))

    def _three_way_merge_sort_gen(self, nums, left, right):
        if left >= right:
            return

        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3

        yield from self._three_way_merge_sort_gen(nums, left, mid1)
        yield from self._three_way_merge_sort_gen(nums, mid1 + 1, mid2)
        yield from self._three_way_merge_sort_gen(nums, mid2 + 1, right)
        yield from self._merge_gen(nums, left, mid1, mid2, right)

    def _merge_gen(self, nums, left, mid1, mid2, right):
        size1 = mid1 - left + 1
        size2 = mid2 - mid1
        size3 = right - mid2

        left_arr = nums[left:left + size1]
        mid_arr = nums[mid1 + 1:mid1 + 1 + size2]
        right_arr = nums[mid2 + 1:mid2 + 1 + size3]

        i = j = k = 0
        index = left

        while i < size1 or j < size2 or k < size3:
            min_value = float('inf')
            min_idx = -1

            if i < size1 and left_arr[i] < min_value:
                min_value = left_arr[i]
                min_idx = 0
            if j < size2 and mid_arr[j] < min_value:
                min_value = mid_arr[j]
                min_idx = 1
            if k < size3 and right_arr[k] < min_value:
                min_value = right_arr[k]
                min_idx = 2

            if min_idx == 0:
                nums[index] = left_arr[i]
                i += 1
            elif min_idx == 1:
                nums[index] = mid_arr[j]
                j += 1
            else:
                nums[index] = right_arr[k]
                k += 1

            yield (nums.copy(), index, -1, (0, 0))
            index += 1
