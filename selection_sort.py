from base_sort import BaseSort
from decorators import measure_time

class SelectionSort(BaseSort):
    time_complexity = "O(n²)"
    space_complexity = "O(1)"

    #selection sort algorithm with time meausure
    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        for i in range(len(nums)-1):
            smallest = 0
            index = 0
            for j in range(i+1, len(nums)):
                if nums[j] < smallest or smallest == 0: 
                    smallest = nums[j]
                    index = j
            if nums[i] > smallest:
                nums[i], nums[index] = smallest, nums[i]
        return nums

    #selection sort algorithm generating data to animation
    def sort_gen(self):
        nums = self.numbers.copy()
        yield (nums.copy(), -1, -1, -1)
        for i in range(len(nums)-1):
            smallest = 0
            index = 0
            for j in range(i+1, len(nums)):
                if nums[j] < smallest or smallest == 0:
                    smallest = nums[j]
                    index = j
                yield (nums.copy(), i, j, i - 1)
            if nums[i] > smallest:
                nums[i], nums[index] = smallest, nums[i]
            yield (nums.copy(), -1, -1, i)
        yield (nums.copy(), -1, -1, len(nums) - 1)

