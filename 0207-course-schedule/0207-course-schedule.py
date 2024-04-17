class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time: O(E+V)
        Space: O(E+V)

        Algorithm:
        We have to first create an adjacency list from the prerequisites. We then have to go through
        each of the course one by one and do dfs on it. We have to check if there is a cycle in the
        current dfs on the course. Our aim is to reach the end of the prerequisite chain where there are
        no more prerequisites. 
        Note: We do visited.remove(course) since we have done dfs on the course and found no cycle on it. 
        As we try to do DFS on the next courses, we don't want the same node to be present in the visited 
        set or we will incorrectly say that there is a cycle. So basically, we remove all the nodes from
        visited which don't form a cycle and store the nodes which do form a cycle.
        """
        graph = defaultdict(list)
        visited = set()

        # Create adjacency list
        for crs, prereq in prerequisites:
            graph[crs].append(prereq) 
        
        def dfs(course):
            if course in visited:  # if there is a cycle
                return False
            if graph[course] == []:  # if course doesn't have any prerequisites, then we mark it with empty list
                return True
                
            visited.add(course)
            for crs in graph[course]:
                # if crs not in visited:  # we should not use this line as we are intentionally checking whether there is cycle or not
                if not dfs(crs): 
                    return False
            graph[course] = []  # this is to denote that this node isn't part of cycle and doesn't have any prerequisites
            visited.remove(course)  # removing the course from visited set since this is not part of a cycle
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
