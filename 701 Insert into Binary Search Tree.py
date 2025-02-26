# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


# Example 1:
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

# Example 3:
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            TreeNode(val)

        if val > root.val:
            self.insertIntoBST(root.right, val)

        elif val < root.val:
            self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST(self, root, val):
        # if root is empty, initialise treenode val
        if not root:
            return TreeNode(val)

        current = root

        while current:
            # go right
            if val > current.val:
                # if right is empty, insert node
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right

            # go left
            elif val < current.val:
                # if left is empty insert node
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left

        return root
