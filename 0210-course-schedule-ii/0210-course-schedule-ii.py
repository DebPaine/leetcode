class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Time: O(E+V)
        Space: O(E+V)

        Algorithm:
        Same question as Course Schedule 1, do this problem first though as Neetcode's explanation
        for this is better than the first one.
        https://www.youtube.com/watch?v=Akt3glAwyfY
        """
        output = []
        graph = defaultdict(list)
        for crs, prereq in prerequisites:
            graph[crs].append(prereq)

        no_prereq = set()
        def dfs(crs):
            # The ordering of the below base conditions matter since if we write the visited one first,
            # then we will return False immediately for condition where we visit the same node again while looping
            if crs in no_prereq:    # if the current course has no prerequisites, then we don't need to go any further
                return True
            if crs in visited:  # if there is a cycle
                return False

            visited.add(crs)
            for nei in graph[crs]:  # the loop won't execute if course has no prerequisites
                if dfs(nei) == False:
                    return False
            output.append(crs)
            no_prereq.add(crs)
            # visited.remove(crs)
            return True

        for crs in range(numCourses):
            visited = set()
            if dfs(crs) == False:    # if there is a cycle, it means we cannot complete the course
                return []

        return output