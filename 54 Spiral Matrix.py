# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        output = []
        row = len(matrix)
        column = len(matrix[0])

        i = 0
        j = 0

        UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4

        up = 0
        left = -1
        down = row
        right = column
        direction = RIGHT

        while len(output) != (row * column):
            if direction == RIGHT:
                # move to right wall
                while j < right:
                    output.append(matrix[i][j])
                    j += 1

                # hit top right and transition to move down
                i += 1
                j -= 1
                right -= 1
                direction = DOWN

            elif direction == DOWN:
                while i < down:
                    output.append(matrix[i][j])
                    i += 1

                # hit bot right and transition to move down
                i -= 1
                j -= 1
                down -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > left:
                    output.append(matrix[i][j])
                    j -= 1
                i -= 1
                j += 1
                left += 1
                direction = UP

            else:
                while i > up:
                    output.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                up += 1
                direction = RIGHT

        return output

    def __init__(self):
        # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        result = self.spiralOrder(matrix)
        print(result)

        # time complex: O(m * n), row x column
        # space complex: O(m * n), row x column


solution = Solution()
