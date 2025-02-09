# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.result = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # combine total from left and right of root
            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.result

    # time complex: o(n), n = no of nodes
    # time complex: o(h), h = height of tree

    def diameterOfBinaryTreeIterative(self, root):
        stack = [root]
        visited = {}

        while stack:
            node = stack[-1]

            # postorder of left > right > root
            if node.left and node.right not in visited:
                stack.append(node.left)
            elif node.right and node.right not in visited:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = visited[node.left]
                rightHeight, rightDiameter = visited[node.right]

                # diameter: max(left + right height, left / right diameter)
                visited[node] = (1 + max(leftHeight, rightDiameter), max(
                    leftHeight + rightHeight, leftDiameter, rightDiameter))

        return visited[root][1]
