# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        node = ListNode(0, head)
        left = node
        right = head

        # set right to be n nodes from head
        for i in range(n):
            right = right.next

        # move both pointers right all the way until right turns to null
        while right:
            left = left.next
            right = right.next

        # replace target node with next next
        left.next = left.next.next

        return node.next

    def create_ll(self, list):
        node = ListNode()
        current = node
        for item in list:
            current.next = ListNode(item)
            current = current.next
        return node.next
    
    def read_ll(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def __init__(self):
        head = self.create_ll([1, 2, 3, 4, 5])
        n = 2
        result = self.removeNthFromEnd(head, n)
        print(self.read_ll(result))


solution = Solution()
