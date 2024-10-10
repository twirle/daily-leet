# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # initialise hashmap for spaces for each course
        preReqMap = {i: [] for i in range(numCourses)}

        # populate the hashmap with courses and their prereqs
        for course, req in prerequisites:
            preReqMap[course].append(req)

        # initialise set to store visited courses that have prereqs that we haven't 'cleared'
        # if we meet a course in this set while searching using dfs, it means we hit a loop
        visited = set()

        # dfs to search for courses that are in prereqs
        def dfs(course):
            # if already stored in visited, means we already seen this course before and we're looping and can't finish/break
            if course in visited:
                return False

            # check the preReqMap to know if there's any prereqs for that course
            # if its empty then there's no prereqs and can finish the courses that need this prereq
            if preReqMap[course] == []:
                return True

            # else if there's some prereqs, we will add that to the visited set and check through the prereqs for other prereqs
            visited.add(course)
            for pre in preReqMap[course]:
                # if we get a false return from any prereq, we can just break and return false again
                if not dfs(pre):
                    return False

            # once we visited the course and checked it clear, we remove course and its reqs
            visited.remove(course)
            preReqMap[course] = []
            return True

        # check through all the courses in numCourses, incase there's disconnected (non-linked/broken graph)
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        # time complex o(v + e),

    def __init__(self):
        numCourses = 20
        prerequisites = [[0, 10], [3, 18], [5, 5], [
            6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
        result = self.canFinish(numCourses, prerequisites)
        print(result)


solution = Solution()
