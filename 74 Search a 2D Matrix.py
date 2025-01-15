# You are given an m x n integer matrix matrix with the following two properties:
#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # vertical binary search to find the correct row
        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2
            # check if target is within the current row range
            if matrix[row][0] <= target <= matrix[row][-1]:
                break

            elif matrix[row][0] > target:
                bot = row - 1

            else:
                top = row + 1

        # if none of the rows have the target
        if not (top <= bot):
            return False

        # normal binary search to find the target
        left = 0
        right = cols - 1
        row = (top + bot) // 2

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True

        return False

    def __init__(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        result = self.searchMatrix(matrix, target)
        print(result)

        # 1 3 5 7
        # 10 11 16 20
        # 23 30 34 60

        # time complex: o(log (m * n))
        # space complex: o(1)


solution = Solution()
