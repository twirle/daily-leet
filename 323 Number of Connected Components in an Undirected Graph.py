# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
# The nodes are numbered from 0 to n - 1.
# Return the total number of connected components in that graph.

# Example 1:
# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1

# Example 2:
# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output:
# 2

class Solution(object):
    def countComponents(self, n, edges):
        # parent tracks the parent of each node in the union-find tree structure, rank tracks size of tree
        parent = [i for i in range(n)]
        rank = [1] * n

        # find root parent of node by following parent pointer until reaching parent node
        def find(node1):
            result = node1

            while result != parent[result]:
                # flatten tree of the nodes by making node point directly to the root instead of traversing each node
                parent[result] = parent[parent[result]]
                result = parent[result]

            return result

        def union(node1, node2):
            # find the parents for node1 and node2
            parent1, parent2 = find(node1), find(node2)

            # if they have same parent, it means they are in the same component, and do not need to be merged
            if parent1 == parent2:
                return 0

            # compare the rank of the parents, if 
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]

            print(parent, rank)

            return 1
            # if they have different parents, union them
            # starting with [0, 1]
            # find(0) = 0, find(1) = 1
            # parent = [0, 0, 2, 3, 4, 5]
            # result = 6 - 1 = 5

            # for [1, 2]
            # find(1) = 0, find(2) = 2
            # parent = [0, 0, 0, 3, 4, 5]
            # result = 5 - 1 = 4

            # and so on

        # iterate through the input set of edges to union the 'unionable' edges, and count how many components are there
        # if there is a union, we reduce the counter, result, by 1 since we made an union
        result = n
        for node1, node2 in edges:
            result -= union(node1, node2)

        return result

    def __init__(self):
        n = 6
        edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
        result = self.countComponents(n, edges)
        print(result)

        # time complex: O(v + e), since we iterated through each edge and vertex
        # space complex: O(v + e), same as well since we need to store information of parent and rank array


solution = Solution()

# leetcode 547 is another union find question to try
