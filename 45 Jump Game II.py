# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#     0 <= j <= nums[i] and
#     i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            max_jump = nums[i]
            # 0 1 1 2 2
            # check every reachable index, starting from the 2nd element up to however much it can jump
            for j in range(i + 1, min(i + max_jump + 1, n)):
                # update dp with mininum jumps to reach based on element's value
                dp[j] = min(dp[j], dp[i] + 1)

        # return last element in dp array with minimum jumps
        return dp[n - 1]

    def jumpGreedy(self, nums):
        # initialise 2 pointers
        # end(the current element's max jump) and furtherst (the overall furthest we been so far)
        # smallest = smallest number of jumps we used so far to go the furthest we can
        smallest = 0
        end = furthest = 0

        for i in range(len(nums) - 1):
            # iterate from left to right until we reach the end
            # the furthest we reach so far will be current max, or current element spot + value of element
            furthest = max(furthest, i + nums[i])

            if i == end:
                # when we reach the end, increment jump count and push end to the furthest possible spot found from current iteration
                smallest += 1
                end = furthest

        # i = 0, furthest = 0, smallest = 1, end = 0
        # i = 1, furthest = 4, smallest = 2, end = 4

        return smallest

    def __init__(self) -> None:
        nums = [2, 3, 1, 1, 4]
        result = self.jumpGreedy(nums)
        print(result)


solution = Solution()
