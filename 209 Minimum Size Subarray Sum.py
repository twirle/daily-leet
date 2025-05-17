# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        size = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            # if moving length is > total, cut from left
            while total >= target:
                size = min(right - left + 1, size)
                total -= nums[left]
                left += 1

        return 0 if size == float('inf') else size

    def __init__(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        result = self.minSubArrayLen(target, nums)
        print(result)

        # time complex: o(n) for going through nums
        # space complex: o(1) no extra storage


solution = Solution()
