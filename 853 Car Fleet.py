# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.


# Example 1:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
#     The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
#     The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
#     The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

# Example 2:
# Input: target = 10, position = [3], speed = [3]
# Output: 1
# Explanation:
# There is only one car, hence there is only one fleet.

# Example 3:
# Input: target = 100, position = [0,2,4], speed = [4,2,1]
# Output: 1

# Explanation:
#     The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
#     Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.


class Solution(object):
    def carFleet(self, target, position, speed):
        pair = []  # [position, speed]
        stack = []

        for car in range(len(position)):
            pair.append((position[car], speed[car]))

        # sort the pair array inversely
        pair.sort(reverse=True)
        print(pair)

        # scan through pair array and append timeTaken to stack
        for position, speed in pair:
            timeTaken = (float(target - position)) / speed
            stack.append(timeTaken)

            # if the prev car in the stack has lower timeTaken than the new car, they will meet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

    def __init__(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]

        # target = 10
        # position = [6, 8]
        # speed = [3, 2]
        result = self.carFleet(target, position, speed)
        print(result)

        # 10 8 0 5 3
        # 12 12 1 6 6
        # 12 12 2 7 7

        # (10, 2), (8, 4), (5, 1), (3, 3), (0, 1)

        # 12 - 2 / 2 = 1
        # 12 - 8 / 4 = 1
        # 12 - 5 / 1 = 7
        # 12 - 3 / 3 = 3
        # 12 / 1 = 12


solution = Solution()
