from base_sort import BaseSort
from decorators import measure_time

class InsertionSort(BaseSort):
    time_complexity = "O(n²)"
    space_complexity = "O(1)"

    #insertion sort algorithm with time meausure
    @measure_time
    def sort(self):
        nums = self.numbers.copy()

        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        
        return nums

    #insertion sort algorithm generating data to animation
    def sort_gen(self):
        nums = self.numbers.copy()
        yield (nums.copy(), -1, -1, (0, 0))

        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            yield (nums.copy(), i, j, (0, 0))

            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
                yield (nums.copy(), j + 1, j, (0, 0))

            nums[j + 1] = key
            yield (nums.copy(), -1, -1, (0, 0))

        yield (nums.copy(), -1, -1, (len(nums), 0))