# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.


# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

import heapq
from collections import Counter, deque


class Solution(object):
    def leastInterval(self, tasks, n):
        # count the number of tasks for each letter
        taskCount = Counter(tasks)
        maxHeap = [-task for task in taskCount.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                # pop from maxHeap and decrease counter by 1
                freq = -heapq.heappop(maxHeap)
                freq -= 1

                # if not erased, append remaining counter to cooldown, with a cooldown timer
                # cooldownTime | counter left
                if freq > 0:
                    cooldown.append((time + n, freq))

            # if cooldown timer is up, pop from deque and push back into heap
            if cooldown and cooldown[0][0] == time:
                readyTime, freq = cooldown.popleft()
                heapq.heappush(maxHeap, -freq)

        return time

    def __init__(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 3
        result = self.leastInterval(tasks, n)
        print(result)

        # time complex: o(k log k), o(k) for each letter to heapify, heap operations o(log k), deque operation o(1)


solution = Solution()
