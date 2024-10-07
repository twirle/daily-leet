# There is a robot on an m x n grid. The robot is initially located at the top-left corner(i.e., grid[0][0]). The robot tries to move to the bottom-right corner(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

#   n n n n n n n n n
# m 28 21 15 10 6 3 1
# m 7  6  5  4  3 2 1
# m 1  1  1  1  1 1 1

class Solution(object):
    def uniquePaths(self, m, n):
        # m = row, n = column
        row = [1] * n

        for i in range(m - 1):
            # generate 'm' rows of 'n' columns
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                # going from the right
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

    def __init__(self) -> None:
        m = 3
        n = 7
        result = self.uniquePaths(m, n)
        print(result)

solution = Solution()
