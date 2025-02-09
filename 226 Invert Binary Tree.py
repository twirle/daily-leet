# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4, 2, 7, 1, 3, 6, 9]
# Output: [4, 7, 2, 9, 6, 3, 1]

# Example 2:
# Input: root = [2, 1, 3]
# Output: [2, 3, 1]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTreeIterative(self, root):
        if not root:
            return None

        stack = [root]
        while stack:
            current = stack.pop()
            current.left, current.right = current.right, current.left
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return root

    # time complex: o(n)
    # space complex: o(n)
