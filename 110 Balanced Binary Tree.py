# Given a binary tree, determine if it is height-balanced

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Postorder traverse
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [0, True]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[1] and right[1] and abs(left[0]-right[0]) <= 1
            return (1 + max(left[0], right[0]), balanced)

        return dfs(root)[1]

    def isBalancedStack(self, root):
        stack = []
        current = root
        depth = {}
        last = None

        while current or stack:
            if current:
                # store root into stack
                stack.append(current)
                current = current.left
            else:
                # check root stored in stack
                current = stack[-1]

                if not current.right or last == current.right:
                    stack.pop()
                    left = depth.get(current.left, 0)
                    right = depth.get(current.right, 0)

                    # check if balanced
                    if abs(left - right) > 1:
                        return False

                    # increase depth at current node +1
                    depth[current] = 1 + max(left, right)
                    last = current
                    current = None

                else:
                    current = current.right

        return True
    
    # time complex: o(n)
    # space complex: o(n)