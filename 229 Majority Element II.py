# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:
# Input: nums = [3, 2, 3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1, 2]
# Output: [1, 2]

# Constraints:

#     1 <= nums.length <= 5 * 104
#     -109 <= nums[i] <= 109

# Follow up: Could you solve the problem in linear time and in O(1) space?

import collections


class Solution(object):
    def majorityElementSorting(self, nums):
        nums.sort()
        # [2, 3, 3]

        result = []
        num = len(nums)

        i = 0
        while i < num:
            j = i + 1
            # quickly go through consecutive duplicates
            while j < num and nums[i] == nums[j]:
                j += 1

            # check len of that number if > nums // 3
            if (j - i) > nums // 3:
                result.append(nums[i])
            i = j

        return result

    def majorityElement(self, nums):
        count = collections.defaultdict(int)
        result = []

        # populate hashmap and increment value
        for num in nums:
            count[num] += 1

            # keep hashmap limited to 2 items
            if len(count) > 2:

                # when new 3rd item gets introduced, decrement existing two items by 1
                count2 = collections.defaultdict(int)
                for key, val in count.items():
                    if val > 1:
                        count2[key] = val - 1

                # replace with new decremented count
                count = count2

        for num in count:
            if nums.count(num) > len(nums) // 3:
                result.append(num)

        return result

    def __init__(self):
        nums = [3, 2, 3]
        result = self.majorityElement(nums)
        print(result)


solution = Solution()
