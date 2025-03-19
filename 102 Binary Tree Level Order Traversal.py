# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[3], [9, 20], [15, 7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        queue = collections.deque([root])
        # result to store lists of each level
        result = []

        while queue:
            # initialise inner list to store per level
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    # add to level list to queue list
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)
        return result

    def levelOrderDFS(self, root):
        result = []

        def dfs(node, depth):
            if not node:
                return None

            if len(result) == depth:
                result.append([])

            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result
