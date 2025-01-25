# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []  # [index, temp]
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # while stack and current day temp is higher than day before
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex

            # push current temp and index to stack
            stack.append((temp, index))

        return result

    def __init__(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        result = self.dailyTemperatures(temperatures)
        print(result)

        # 75 71 69 72
        # 1 1 ? ? 1


solution = Solution()
