from base_sort import BaseSort
from decorators import measure_time

MIN_RUN = 32

class TimSort(BaseSort):
    time_complexity = "Worst: O(n log n), Best: Ω(n)"
    space_complexity = "O(n)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        n = len(nums)
        min_run = self._calc_min_run(n)
        runs = []

        i = 0
        while i < n:
            run_end = self._find_run(nums, i, n)
            run_len = run_end - i
            if run_len < min_run:
                end = min(i + min_run, n)
                self._insertion_sort(nums, i, end - 1)
                run_end = end
            runs.append((i, run_end))
            i = run_end
            while len(runs) > 1:
                l1, r1 = runs[-2]
                l2, r2 = runs[-1]
                if r1 - l1 <= r2 - l2:
                    self._merge(nums, l1, r1 - 1, r2 - 1)
                    runs.pop()
                    runs[-1] = (l1, r2)
                else:
                    break

        while len(runs) > 1:
            l1, r1 = runs[-2]
            l2, r2 = runs[-1]
            self._merge(nums, l1, r1 - 1, r2 - 1)
            runs.pop()
            runs[-1] = (l1, r2)

        return nums

    def _calc_min_run(self, n):
        r = 0
        while n >= MIN_RUN:
            r |= n & 1
            n >>= 1
        return n + r

    def _find_run(self, nums, start, n):
        end = start + 1
        if end == n:
            return end
        if nums[end] < nums[start]:
            while end < n and nums[end] < nums[end - 1]:
                end += 1
            nums[start:end] = reversed(nums[start:end])
        else:
            while end < n and nums[end] >= nums[end - 1]:
                end += 1
        return end

    def _insertion_sort(self, nums, begin, end):
        for i in range(begin + 1, end + 1):
            key = nums[i]
            j = i - 1
            while j >= begin and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

    def _merge(self, nums, l, m, r):
        left = nums[l:m + 1]
        right = nums[m + 1:r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    def sort_gen(self):
        nums = self.numbers.copy()
        n = len(nums)
        min_run = self._calc_min_run(n)
        runs = []
        yield (nums.copy(), -1, -1, (0, 0))

        i = 0
        while i < n:
            run_end = self._find_run(nums, i, n)
            run_len = run_end - i
            if run_len < min_run:
                end = min(i + min_run, n)
                yield from self._insertion_sort_gen(nums, i, end - 1)
                run_end = end
            else:
                yield (nums.copy(), i, run_end - 1, (0, 0))

            runs.append((i, run_end))
            i = run_end

            while len(runs) > 1:
                l1, r1 = runs[-2]
                l2, r2 = runs[-1]
                if r1 - l1 <= r2 - l2:
                    yield from self._merge_gen(nums, l1, r1 - 1, r2 - 1)
                    runs.pop()
                    runs[-1] = (l1, r2)
                else:
                    break

        while len(runs) > 1:
            l1, r1 = runs[-2]
            l2, r2 = runs[-1]
            yield from self._merge_gen(nums, l1, r1 - 1, r2 - 1)
            runs.pop()
            runs[-1] = (l1, r2)

        yield (nums.copy(), -1, -1, (len(nums), 0))

    def _insertion_sort_gen(self, nums, begin, end):
        for i in range(begin + 1, end + 1):
            key = nums[i]
            j = i - 1
            yield (nums.copy(), i, j, (0, 0))
            while j >= begin and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
                yield (nums.copy(), j + 1, j, (0, 0))
            nums[j + 1] = key
            yield (nums.copy(), j + 1, -1, (0, 0))

    def _merge_gen(self, nums, l, m, r):
        left = nums[l:m + 1]
        right = nums[m + 1:r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                source = l + i
                nums[k] = left[i]
                i += 1
            else:
                source = m + 1 + j
                nums[k] = right[j]
                j += 1
            yield (nums.copy(), k, source, (0, 0))
            k += 1
        while i < len(left):
            nums[k] = left[i]
            yield (nums.copy(), k, l + i, (0, 0))
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            yield (nums.copy(), k, m + 1 + j, (0, 0))
            j += 1
            k += 1
