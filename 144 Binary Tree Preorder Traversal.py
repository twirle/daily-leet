# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [1, 2, 3]
# Explanation:

# Example 2:
# Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
# Output: [1, 2, 4, 5, 6, 7, 3, 8, 9]
# Explanation:

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        # preorder: root > left > right
        result = []

        def preOrder(root):
            if not root:
                return
            result.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return result

    def preorderTraversalIterative(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            if current:
                # add root
                result.append(current.val)

                # store right
                stack.append(current.right)

                # point to left
                current = current.left
            else:
                # at bottom left NULL, pop the empty from stack and start on right
                current = stack.pop()

        return result
