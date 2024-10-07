# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        # once sorted, it becomes like two sum II but with a 3rd input

        for i, n in enumerate(nums):
            print(i, n)
            if i > 0 and n == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = n + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    # if duplicates, move left pointer to right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result

    def __init__(self) -> None:
        nums = [-1, 0, 1, 2, -1, -4]
        result = self.threeSum(nums)
        print(result)


solution = Solution()
