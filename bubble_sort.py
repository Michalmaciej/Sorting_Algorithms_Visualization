from base_sort import BaseSort
from decorators import measure_time

class BubbleSort(BaseSort):
    time_complexity = "O(n²)"
    space_complexity = "O(1)"

    #bubble sort algorithm with time meausure
    @measure_time
    def sort(self):
        nums = self.numbers.copy()

        for i in range(len(nums)):
            swap = False
            for j in range(len(nums)-i-1):
                if nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if not swap: break
        return nums

    #bubble sort algorithm generating data to animation
    def sort_gen(self):
        nums = self.numbers.copy()
        yield (nums.copy(), -1, -1, (0, 0))
        for i in range(len(nums)):
            swap = False
            for j in range(len(nums)-i-1):
                if nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
                yield (nums.copy(), j+1, j, (0, i))
            if not swap:
                break
            yield (nums.copy(), -1, -1, (0, i + 1))
        yield (nums.copy(), -1, -1, (0, len(nums)))