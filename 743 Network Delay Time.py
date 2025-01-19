# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))

        visit = set()
        minHeap = [(0, k)]
        time = 0

        while minHeap:
            nodeTravelTime, node = heapq.heappop(minHeap)
            if node in visit:
                continue

            visit.add(node)
            time = max(time, nodeTravelTime)

            for neighbour, neighWeight in graph[node]:
                newWeight = nodeTravelTime + neighWeight
                if neighbour not in visit:
                    heapq.heappush(minHeap, (newWeight, neighbour))

        if len(visit) == n:
            return time
        else:
            return -1

    def __init__(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2


solution = Solution()
