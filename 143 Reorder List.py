# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        # alternating merge thing between two lists

        # split list into two halves
        slow = fast = head

        # iterate to end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        prev = slow.next = None

        # reverse second half of linked list
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # merge halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        return head

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
        head = self.create_ll([1, 2, 3, 4])
        result = self.reorderList(head)
        print(self.read_ll(result))

        # current = 4, prev = 3, temp = 4
        # 1 2 3 4
        # 1 2 4 3
        # 1 4 2 3


solution = Solution()
