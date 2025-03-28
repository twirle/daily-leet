# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

# Example 3:
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true

class Solution:
    def containsDuplicate(self, nums):
        hash = {}

        for i, n in enumerate(nums):
            if n in hash:
                return True
            hash[n] = i
        return False

    def __init__(self):
        nums = [1, 2, 3, 1]
        result = self.containsDuplicate(nums)
        print(result)

# solution = Solution()


class Solution:
    def containsDuplicate(self, nums):
        hash = set()
        for n in nums:
            if n in hash:
                return True
            hash.add(n)
        return False


# set uniques to compare length
class Solution:
    def containsDuplicate(self, nums):
        # sets are unordered unique so if there's a dupe the length would not be the same
        return len(set(nums)) == len(nums)
