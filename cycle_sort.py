from base_sort import BaseSort
from decorators import measure_time

class CycleSort(BaseSort):
    time_complexity = "O(n²)"
    space_complexity = "O(1)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        n = len(nums)

        for cycleStart in range(n - 1):
            item = nums[cycleStart]

            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if nums[i] < item:
                    pos += 1

            if pos == cycleStart:
                continue

            while item == nums[pos]:
                pos += 1
            nums[pos], item = item, nums[pos]

            while pos != cycleStart:
                pos = cycleStart
                for i in range(cycleStart + 1, n):
                    if nums[i] < item:
                        pos += 1

                while item == nums[pos]:
                    pos += 1
                nums[pos], item = item, nums[pos]

        return nums

    def sort_gen(self):
        nums = self.numbers.copy()
        n = len(nums)
        sorted_set = set()
        yield (nums.copy(), -1, -1, frozenset(sorted_set))

        for cycleStart in range(n - 1):
            item = nums[cycleStart]

            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if nums[i] < item:
                    pos += 1
                yield (nums.copy(), cycleStart, i, frozenset(sorted_set))

            if pos == cycleStart:
                sorted_set.add(cycleStart)
                yield (nums.copy(), -1, -1, frozenset(sorted_set))
                continue

            while item == nums[pos]:
                pos += 1
            nums[pos], item = item, nums[pos]
            yield (nums.copy(), cycleStart, pos, frozenset(sorted_set))

            while pos != cycleStart:
                pos = cycleStart
                for i in range(cycleStart + 1, n):
                    if nums[i] < item:
                        pos += 1
                    yield (nums.copy(), cycleStart, i, frozenset(sorted_set))

                while item == nums[pos]:
                    pos += 1
                nums[pos], item = item, nums[pos]
                yield (nums.copy(), cycleStart, pos, frozenset(sorted_set))

            sorted_set.add(cycleStart)
            yield (nums.copy(), -1, -1, frozenset(sorted_set))

        sorted_set.add(n - 1)
        yield (nums.copy(), -1, -1, frozenset(sorted_set))
