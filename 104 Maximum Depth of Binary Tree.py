# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 3

# Example 2:
# Input: root = [1, null, 2]
# Output: 2


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # time complex: o(n)
    # space complex: o(h)

    def maxDepthIterative(self, root):
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append(node.left, depth + 1)
                stack.append(node.right, depth + 1)

        return result

    def maxDepthBFS(self, root):
        queue = deque()
        if root:
            queue.append(root)

        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
