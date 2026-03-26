from base_sort import BaseSort
from decorators import measure_time

class BucketSort(BaseSort):
    time_complexity = "Worst: O(n²), Best: O(n + k)"
    space_complexity = "O(n + k)"

    @measure_time
    def sort(self):
        nums = self.numbers.copy()
        n = len(nums)
        minval, maxval = min(nums), max(nums)
        buckets = [[] for _ in range(n)]

        for num in nums:
            bi = min(int((num - minval) / (maxval - minval + 1) * n), n - 1)
            buckets[bi].append(num)

        for bucket in buckets:
            self._insertion_sort(bucket)

        index = 0
        for bucket in buckets:
            for num in bucket:
                nums[index] = num
                index += 1

        return nums

    def _insertion_sort(self, bucket):
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key

    def sort_gen(self):
        nums = self.numbers.copy()
        n = len(nums)
        minval, maxval = min(nums), max(nums)
        yield (nums.copy(), -1, -1, (0, 0))

        # distribute into buckets
        buckets = [[] for _ in range(n)]
        for i, num in enumerate(nums):
            bi = min(int((num - minval) / (maxval - minval + 1) * n), n - 1)
            buckets[bi].append(num)
            yield (nums.copy(), i, -1, (0, 0))

        # sort individual buckets
        for bucket in buckets:
            self._insertion_sort(bucket)

        # concatenate back into nums
        index = 0
        for bucket in buckets:
            for num in bucket:
                nums[index] = num
                yield (nums.copy(), index, -1, (0, 0))
                index += 1

        yield (nums.copy(), -1, -1, (len(nums), 0))
