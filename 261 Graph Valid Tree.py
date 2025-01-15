# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# No duplicate edges will appear in edges, and all edges are undirected. [0, 1] and [1, 0] will not appear together in edges.

# Example 1:
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: True


#    0
#  / | \
# 1  2  3
# |
# 4

# Tree could be invalid due to:
# - loop
# - node that is not connected to main tree


class Solution(object):
    def validTree(self, n, edges):

        # initialise a graph with n nodes, then connect the edges.
        graph = {i: [] for i in range(n)}
        # {0: [], 1: [], 2: [], 3: [], 4: []}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}
        visited = set()

        def dfs(i, prev):
            # if already added to visited, it means that we hit a loop so it's not valid
            # this 'prev' will prevent false detection of loop when we check 4: 1 again,  after coming from 1: 0, 4
            print('i =', i)
            if i in visited:
                return False

            # add to visited, so that if we see it again we will return false due to looping
            visited.add(i)
            print('visted', visited)

            for j in graph[i]:
                print('graph i', graph[i])
                print('j prev', j, prev, j == prev)

                # iterate through the edges for each node in the hash, then check if the following
                # 0: 1, 2, 3
                # 1: 0, 4
                # 2: 0
                # 3: 0
                # 4: 1

                # dfs(0, -1)
                # dfs(1, 0)
                # dfs(4, 1)
                # dfs(2, 0)
                # dfs(3, 0)

                # if it is the previous node that we came from, we skip and go next because we will loop back to what we checked before, but is not a loop.
                if j == prev:
                    print('same node')
                    continue

                print(i, j)

                # if it's not the previous node that we came from, then we dfs on that
                # if returned false, then we return false
                # if true then we continue
                if not dfs(j, i):
                    return False
            return True

        # run dfs to check for loops, but starting from (0, -1)
        # if every node is visitable from 0, then all nodes/vertices are connected
        return dfs(0, -1) and n == len(visited)

    def __init__(self):
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        n = 5
        result = self.validTree(n, edges)
        print(result)

        # (0, 1)
        # (1, 4)
        # (0, 2)
        # (0, 3)

        # time complex: O(v + e)
        # space complex: O(v + e)


solution = Solution()
