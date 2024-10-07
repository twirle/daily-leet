# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

class Solution(object):
    # greedy solution
    # O(n)
    def canJump(self, nums):
        target = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0

    # dp solution
    def canJumpDP(self, nums):
        # initialise dp array to store results
        dp = {len(nums) - 1: True}

        def reach(i):
            if i in dp:
                return dp[i]

            for jump in range(i, nums[i] + 1):
                if reach(i+jump):
                    dp[i] = True
                    return True

            dp[i] = False
            return False

        return reach(0)

    def __init__(self) -> None:
        nums = [3, 2, 1, 0, 4]
        result = self.canJump(nums)
        print(result)


solution = Solution()
