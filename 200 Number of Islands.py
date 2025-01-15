# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
                return
            else:
                # overwrite and turn surrounding 'land' tiles of same island to 0, then once island is submerged, continue along to scan the grid for next island

                # submerge found land
                grid[row][col] = '0'

                # check WASD and submerge them
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        # go through whole grid to find '1's
        for row in range(rows):
            for col in range(cols):
                # if we find land
                if grid[row][col] == "1":
                    # bfs to look through surrounding tiles if they are part of
                    dfs(row, col)
                    islands += 1

        return islands

    def __init__(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        result = self.numIslands(grid)
        print(result)

        # time complex: O(m*n)
        # space complex: O(m*n)


solution = Solution()


# alternative BFS queue solution
class Solution(object):
    def numIslandsv2(self, grid):
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(row, col):
            queue = collections.deque()
            visit.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for directionRow, directionCol in directions:
                    # row, col = row + directionRow, col + directionCol
                    if ((row + directionRow) in range(rows) and
                        (col + directionCol) in range(cols) and
                        grid[row + directionRow][col + directionCol] == "1" and
                            (row + directionRow, col + directionCol) not in visit):

                        queue.append((row + directionRow, col + directionCol))
                        visit.add((row + directionRow, col + directionCol))

        # go through whole grid to find '1's
        for row in range(rows):
            for col in range(cols):
                # if we find land
                if grid[row][col] == "1" and (row, col) not in visit:
                    # bfs to look through surrounding tiles if they are part of
                    bfs(row, col)
                    islands += 1
        return islands
