# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

import heapq


class Solution(object):
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        # [diff, row, col]
        minHeap = [[0, 0, 0]]
        visit = set()
        minDiff = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)
            if (row, col) in visit:
                continue

            visit.add((row, col))

            if (row, col) == (rows - 1, cols - 1):
                return diff

            for dRow, dCol in directions:
                newRow = row + dRow
                newCol = col + dCol

                if rows > newRow >= 0 and cols > newCol >= 0 and (newRow, newCol) not in visit:
                    minDiff = max(diff,
                                  abs(heights[row][col] - heights[newRow[newCol]]))
                    heapq.heappush(minHeap, [minDiff, newRow, newCol])

    def __init__(self):
        heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
            1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
        result = self.minimumEffortPath(heights)
        print(result)


solution = Solution()
