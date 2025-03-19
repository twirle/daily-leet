# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Example 1:
# Input: root = [1, 2, 3, null, 5, null, 4]
# Output: [1, 3, 4]

# Example 2:
# Input: root = [1, 2, 3, 4, null, null, null, 5]
# Output: [1, 3, 4, 5]

# Example 3:
# Input: root = [1, null, 3]
# Output: [1, 3]

# Example 4:
# Input: root = []
# Output: []


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution(object):
    def rightSideView(self, root):
        queue = collections.deque([root])
        result = []

        while queue:
            # the most right-side node to add to the result
            right = None

            # iterate through each level
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    # overwrite right until it is the most right
                    right = node

                    # go left first so we reach the right-most node last
                    queue.append(node.left)
                    queue.append(node.right)

            if right:
                result.append(right.val)

        return result
