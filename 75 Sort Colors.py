# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.


# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

class Solution(object):
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        i = 0

        # swap items in the swap between the left and right pointers
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= right:
            print(i, left, right, nums)
            if nums[i] == 0:
                swap(left, i)
                left += 1

            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1

        return nums

    def __init__(self):
        nums = [2, 0, 2, 1, 1, 0]
        result = self.sortColors(nums)
        print(result)

        # I could do one pass to check the number of 0s, 1s, 2s, then do another pass through the nums and update them

        # 2 0 2 1 1 0
        # 2 1 1


solution = Solution()
