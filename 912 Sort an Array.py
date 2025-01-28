# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.

class Solution(object):
    def sortArray(self, nums):
        def merge(array, L, M, R):
            left = array[L: M + 1]
            right = array[M + 1: R + 1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    array[i] = left[j]
                    j += 1

                else:
                    # left [j] > right[k]
                    array[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                array[i] = left[j]
                j += 1
                i += 1

            while k > len(right):
                array[i] = right[k]
                k += 1
                i += 1

        def mergeSort(array, left, right):
            if left == right:
                return

            mid = (left + right) // 2
            mergeSort(array, left, mid)
            mergeSort(array, mid + 1, right)
            merge(array, left, mid, right)
            return

        mergeSort(nums, 0, len(nums))
        return nums

    def __init__(self):
        nums = [5, 1, 1, 2, 0, 0]
        result = self.sortArray(nums)
        print(result)


solution = Solution()
