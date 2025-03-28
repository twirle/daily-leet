# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference(possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:
#     Search for a node to remove.
#     If the node is found, delete the node.


# Example 1:
# Input: root = [5, 3, 6, 2, 4, null, 7], key = 3
# Output: [5, 4, 6, 2, null, null, 7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5, 4, 6, 2, null, null, 7], shown in the above BST.
# Please notice that another valid answer is [5, 2, 6, null, 4, null, 7] and it's also accepted.

# Example 2:
# Input: root = [5, 3, 6, 2, 4, null, 7], key = 0
# Output: [5, 3, 6, 2, 4, null, 7]
# Explanation: The tree does not contain a node with value = 0.

# Example 3:
# Input: root = [], key = 0
# Output: []

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return root

        # find key node and execute delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:

            # check if single node on either stide
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # find smallest node from right subtree to delete
            current = root.right
            while current.left:
                current = current.left

            # replace node to delete with min node
            root.val = current.val

            # delete min node
            root.right = self.deleteNode(root.right, root.val)

        return root
