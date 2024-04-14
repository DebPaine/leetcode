class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Time: O(n) or O(E+V)
        Space: O(E+V)

        Algorithm:
        This is not a very difficult problem. We have to only remember that we need a minimum of (n-1) 
        edges to connect n nodes in the graph. We then find all the clusters using DFS.
        """
        if n-1 > len(connections):
            return -1

        # Step 1: Create adjacency list for the connections
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: Find the no. of nodes in the connected cluster
        def dfs(x):
            for nei in graph[x]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        # Count the total no. of clusters
        clusters = 0
        visited = set()
        # We have to go through all the nodes as there might be disconnected clusters which we cannot traverse using single DFS
        for i in range(n):
            if i not in visited:
                visited.add(i) 
                dfs(i)  # each dfs will add all the connected nodes to the visited set
                clusters += 1

        return clusters - 1 # since each cluster can be thought of as a node, we need n-1 edges to connect them    

