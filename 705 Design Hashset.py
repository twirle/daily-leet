# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

#     void add(key) Inserts the value key into the HashSet.
#     bool contains(key) Returns whether the value key exists in the HashSet or not.
#     void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet(object):

    def __init__(self):
        # initial dummy node
        self.set = [ListNode(0) for i in range(1000)]

    def add(self, key):
        current = self.set[key % len(self.set)]

        while current.next:
            # current key is already exists
            if current.next.key == key:
                return

            current = current.next

        # create new node next to the end
        current.next = ListNode(key)

    def remove(self, key):
        current = self.set[key % len(self.set)]

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return

            current = current.next

    def contains(self, key):
        current = self.set[key % len(self.set)]

        while current.next:
            if current.next.key == key:
                return True

            current = current.next
        return False
