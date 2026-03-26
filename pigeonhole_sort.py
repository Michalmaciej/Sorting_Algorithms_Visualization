from base_sort import BaseSort
from decorators import measure_time

class PigeonholeSort(BaseSort):
    time_complexity = "O(n + range)"
    space_complexity = "O(range)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        my_min = min(nums)
        my_max = max(nums)
        size = my_max - my_min + 1
        holes = [0] * size

        for x in nums:
            holes[x - my_min] += 1

        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                nums[i] = count + my_min
                i += 1

        return nums

    def sort_gen(self):
        nums = self.numbers.copy()
        my_min = min(nums)
        my_max = max(nums)
        size = my_max - my_min + 1
        holes = [0] * size
        yield (nums.copy(), -1, -1, (0, 0))

        # counting phase
        for i, x in enumerate(nums):
            holes[x - my_min] += 1
            yield (nums.copy(), i, -1, (0, 0))

        # placing back
        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                nums[i] = count + my_min
                yield (nums.copy(), i, -1, (0, 0))
                i += 1

        yield (nums.copy(), -1, -1, (len(nums), 0))
