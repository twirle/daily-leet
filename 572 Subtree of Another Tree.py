# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        # check if subtree is bigger than main tree
        if not root:
            return False
        if not subRoot:
            return True

        # go through tree until we find the subroot in the main root
        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left), subRoot or self.isSubtree(root.right, subRoot)

    # function to check if identical tree
    def sameTree(self, root, subRoot):
        # both trees are out of nodes
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            # check left and right of both
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

        #
        return False
