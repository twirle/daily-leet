# Given an integer array nums, return the length of the longest strictly increasing subsequence.


# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for i in range(len(nums)):
            # iterate through nums
            for j in range(0, i):
                # nested within to go through
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    def __init__(self) -> None:
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        result = self.lengthOfLIS(nums)
        print(result)
