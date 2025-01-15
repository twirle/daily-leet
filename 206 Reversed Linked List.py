# Reverse Linked List

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

# Example 2:
# Input: head = []
# Output: []


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head: ListNode):
        curr = head
        prev = None
        print(curr)

        while curr:
            # set next for current to be previous
            temp = curr.next
            curr.next = prev

            # continue to traverse to next node
            prev = curr
            curr = temp

        # at the end, set next = null

        return prev

    def __init__(self):
        head = [0, 1, 2, 3]
        result = self.reverseList(head)
        print(result)

        # 0, 1, 2, 3
        # temp = curr.next
        # curr.next = prev

        # continue to 
        # prev = curr
        # curr = next

        # prev  curr    next
        # 2     3       1


solution = Solution()
