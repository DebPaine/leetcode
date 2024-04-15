class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Time: O(n) or O(E+V)
        Space: O(E+V)

        Algorithm:
        This is the same problem as 1319. Number of Operations to Make Network Connected, except we are
        given an adjacency matrix instead of adjacency list. We just have to traverse the graph by going
        node by node and dfs on it's neighbours.
        """
        visited = set()
        provinces = 0

        def dfs(node):
            for nei in range(len(isConnected[node])):   # go through the neighbours of node
                if isConnected[node][nei] == 1 and nei not in visited:  # == 1 means node and nei are connected
                    visited.add(nei)
                    dfs(nei)

        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1

        return provinces
