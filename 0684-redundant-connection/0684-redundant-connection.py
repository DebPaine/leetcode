class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Time: O(n**2)
        Space: O(n)

        Algorithm:
        We have to go through the edges and construct the graph using one edge at a time. We first 
        check whether the current edge is redundant or not by seeing if we can reach node from a to b
        without adding the current edge in the graph. We also check if we are going in a loop or not.
        """
        # Note: Constraint given n == edges.length, which means that there will always be a cycle
        graph = defaultdict(list)
        output = []
        
        visited = set()
        def dfs(u, v):
            if u in visited:    # we are checking if there is a cycle in the graph
                return False
            if u == v:      # we are checking if we can reach u to v, eg: [2, 3]
                return True

            visited.add(u)
            for nei in graph[u]:
                if dfs(nei, v):
                    return True
            visited.remove(u)
            return False

        # Every iteration, we check whether we can reach node a to b within the graph. If yes, then we don't need to add edge [a, b].
        # We are checking whether we need to add the current edge to the existing graph or not as it might be redundant.
        for a, b in edges:
            # visited = set()
            if dfs(a, b):
                output = [a, b]
            # Add both nodes in each other's neighbours list as it's an undirected graph
            graph[a].append(b)
            graph[b].append(a)
        
        return output