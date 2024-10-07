# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

class Solution(object):
    def rob(self, nums):
        rob1 = 0
        rob2 = 0

        for num in nums:
            # 2 7 9 3 1
            # 2 7 11 11 12
            temp = max(num + rob1, rob2)
            # temp = 2 
            # rob1 = 0 
            # rob2 = 2 
            rob1 = rob2
            rob2 = temp

        return rob2

    def __init__(self) -> None:
        nums = [2, 7, 9, 3, 1]
        result = self.rob(nums)
        print(result)


solution = Solution()
