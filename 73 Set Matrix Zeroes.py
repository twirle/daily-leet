# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.


# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        rowzero = False

        #

        # find out which rows/cols can be flipped to zero
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    # flip the top row of the column to zero
                    matrix[0][col] = 0

                    if row == 0:
                        rowzero = True
                    else:
                        # flip the most left column of the row to zero
                        matrix[row][0] = 0

        # flip the insides if the outer row/col is zero
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # if corner is zero, flip the whole first column
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0

        if rowzero:
            for col in range(cols):
                matrix[0][col] = 0

        return matrix

    def __init__(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        result = self.setZeroes(matrix)
        print(result)

        # 1 1 1     1 0 1
        # 1 0 1     0 0 0
        # 1 1 1     1 0 1

        # 0 1 2 0   0 0 0 0
        # 3 4 5 2   0 4 5 0
        # 1 3 1 5   0 3 1 0

        # time complex: o(m * n)
        # space complex: o(1)


solution = Solution()
