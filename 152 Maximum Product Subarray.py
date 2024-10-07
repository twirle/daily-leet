# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        currentMin, currentMax = 1, 1

        for n in nums:
            if n == 0:
                currentMin, currentMax = 1, 1
                continue
            tempMax = currentMax * n
            currentMax = max(n*currentMax, n*currentMin, n)
            currentMin = min(tempMax, n*currentMin, n)
            res = max(res, currentMax)
        return res

    def __init__(self) -> None:
        nums = [2, 3, -2, 4]
        result = self.maxProduct(nums)
        print(result)


solution = Solution()
