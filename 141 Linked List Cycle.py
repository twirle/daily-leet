# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # if slow catches up to fast then the cycle is confirmed
            if slow == fast:
                return True

        return False

    def __init__(self):
        nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
        nodes[0].next = nodes[1]
        nodes[1].next = nodes[2]
        nodes[2].next = nodes[3]
        nodes[3].next = nodes[1]

        head = nodes[0]
        result = self.hasCycle(head)
        print(result)


solution = Solution()
