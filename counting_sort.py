from base_sort import BaseSort
from decorators import measure_time

class CountingSort(BaseSort):
    time_complexity = "O(N + M)"
    space_complexity = "O(N + M)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        if not nums:
            return []

        maxval = max(nums)
        cnt = [0] * (maxval + 1)

        for v in nums:
            cnt[v] += 1

        for i in range(1, maxval + 1):
            cnt[i] += cnt[i - 1]

        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            v = nums[i]
            ans[cnt[v] - 1] = v
            cnt[v] -= 1

        return ans

    def sort_gen(self):
        nums = self.numbers.copy()
        if not nums:
            return

        n = len(nums)
        maxval = max(nums)
        yield (nums.copy(), -1, -1, (0, 0))

        # counting phase
        cnt = [0] * (maxval + 1)
        for i, v in enumerate(nums):
            cnt[v] += 1
            yield (nums.copy(), i, -1, (0, 0))

        # prefix sums - internal, no visual change to array
        for i in range(1, maxval + 1):
            cnt[i] += cnt[i - 1]

        # building output array
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            v = nums[i]
            dest = cnt[v] - 1
            ans[dest] = v
            cnt[v] -= 1
            yield (ans.copy(), dest, i, (0, 0))

        yield (ans.copy(), -1, -1, (len(ans), 0))
