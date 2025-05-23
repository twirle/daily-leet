# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.


# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            # if mid is target
            if nums[mid] == target:
                return True

            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
                continue

            # check left sorted portion
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # check right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False

    def __init__(self):
        nums = [1, 0, 1, 1, 1]
        target = 0
        result = self.search(nums, target)
        print(result)


solution = Solution()
