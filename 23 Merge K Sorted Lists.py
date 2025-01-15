# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: The linked-lists are:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# merging them into one sorted list:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        # divide and conquer merge sorted lists

        # base case break if there's no lists left
        if not lists or len(lists) == 0:
            return None

        # keep merging until there's only 1 list left
        while len(lists) > 1:
            mergedLists = []

            # merge lists in pairs
            # if there are an odd number of lists, then the last list will merge with None, which returns the first list
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedLists.append(self.mergeList(list1, list2))

            # update initial lists to changes made in mergedlists
            # then go around loop using this set of merged lists
            lists = mergedLists
        return lists[0]

    def mergeList(self, list1, list2):
        node = ListNode()
        current = node

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # leftovers
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
        # lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        list1 = self.create_ll([1, 4, 5])
        list2 = self.create_ll([1, 3, 4])
        list3 = self.create_ll([2, 6])
        lists = [list1, list2, list3]
        result = self.mergeKLists(lists)
        print(self.read_ll(result))

        # time complex: merging two lists is o(n + m), where n and m are size of lists
        # each iteration halves the number of lists, total complex is o(n log k), where n is number of nodes, k is the number of lists
        # space complex: o(1)


solution = Solution()
