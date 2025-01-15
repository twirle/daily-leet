# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # starting node
        node = ListNode()
        current = node

        # check the two heads of each list until both lists are done
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # after finishing one list, shove in the leftovers of the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

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
        list1 = self.create_ll([1, 2, 4])
        list2 = self.create_ll([1, 3, 4])
        result = self.mergeTwoLists(list1, list2)
        print(self.read_ll(result))


solution = Solution()
