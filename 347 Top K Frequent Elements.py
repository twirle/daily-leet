# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        counter = Counter(nums)
        bucket = [[] for _ in range(n + 1)]
        result = []

        for num, freq in counter.items():
            bucket[freq].append(num)

        for i in range(n, -1, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result

        # time complex: o(n + k)
        # space complex: o(n + k)

    def topKFrequentHeap(self, nums, k):
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                # push in then pops the smallest out
                heapq.heappushpop(heap, (val, key))

        result = []
        for h in heap:
            result.append(h[1])

        return result

        # time complex: o(k log n)
        # space complex: o(n)

    def __init__(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = self.topKFrequent(nums, k)
        print(result)


solution = Solution()
