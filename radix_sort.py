from base_sort import BaseSort
from decorators import measure_time

class RadixSort(BaseSort):
    time_complexity = "O(d * (n + b))"
    space_complexity = "O(n + b)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        max1 = max(nums)
        exp = 1
        while max1 / exp >= 1:
            self._counting_sort(nums, exp)
            exp *= 10
        return nums

    def _counting_sort(self, nums, exp):
        n = len(nums)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = nums[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = nums[i] // exp
            output[count[index % 10] - 1] = nums[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            nums[i] = output[i]

    def sort_gen(self):
        nums = self.numbers.copy()
        max1 = max(nums)
        yield (nums.copy(), -1, -1, (0, 0))

        exp = 1
        while max1 / exp >= 1:
            yield from self._counting_sort_gen(nums, exp)
            exp *= 10

        yield (nums.copy(), -1, -1, (len(nums), 0))

    def _counting_sort_gen(self, nums, exp):
        n = len(nums)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = nums[i] // exp
            count[index % 10] += 1
            yield (nums.copy(), i, -1, (0, 0))

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = nums[i] // exp
            dest = count[index % 10] - 1
            output[dest] = nums[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            nums[i] = output[i]
            yield (nums.copy(), i, -1, (0, 0))
