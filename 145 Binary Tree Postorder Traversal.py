# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Explanation:

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]
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
    def postorderTraversal(self, root):
        # postorder: left > right > root
        result = []

        def postOrder(root):
            if not root:
                return

            postOrder(root.left)
            postOrder(root.right)
            result.append(root.val)

        postOrder(root)
        return result

    def postorderTraversalIterative(self, root):
        result = []
        stack = []
        current = root

        # root > right > left thrn reverse maybe

        while current or stack:
            if current:
                # add root
                result.append(current.val)

                # store left
                stack.append(current.left)

                # point right
                current = current.right

            else:
                # pop left and because we're left with lefts, need to point to left
                current = stack.pop()
                current = current.left

        result.reverse()
        return result.reverse()
