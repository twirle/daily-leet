# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [1, 3, 2]
# Explanation:

# Example 2:
# Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
# Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]
# Explanation:

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        # inorder: left > root > right
        result = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return result

    def inorderTraversalIterative(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                # traverse to bottom left
                stack.append(current)
                current = current.left
            # at bottom left, pop and point to right
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

        # time complex: o(n)
        # space complex: o(h), height of tree


solution = Solution()
