# 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# input: nums = [ 2, 7, 11, 15], target = 9
# output: [ 0, 1 ]
# nums[0], nums[1] == 9, we return [0, 1]

# input: nums = [ 3, 2, 4 ], target = 6
# output: [ 1, 2 ]

# input: nums = [ 3, 3 ], target = 6
# output: [ 0, 1 ]

# looping bruteforce (so it will be n^2)
# check [0,1] [0,2] [0,3] if they are target
# have an x and y, and loop them

# hashmap
# since each input in the array is unique, if target - ind

class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
