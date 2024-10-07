# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# if 4
# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2

# is actually fibonacci sequence
#  0 1 2 3 4 5 6
# 13 8 5 3 2 1 1

class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1

        for i in range(n - 1):
            one = one + two
            two = one - two
        return one

    def __init__(self) -> None:
        n = 3
        result = self.climbStairs(n)
        print(result)


solution = Solution()
