class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Time: O(q*(E+V)), where q is no. or queries, E is no. of edges, and V is no. of vertices in the graph
        Space: O(E+V), since we are using adjacency list to store the vertices (hash key) and edges (hash value)

        Algorithm:
        This doesn't seem like a graph problem initially but after drawing it out, we get an intuition
        for graph. We first create an adjacency list to represent the graph. We then go over the list
        of queries and do dfs on it. We keep going in the dfs till our source and target nodes become the same.
        """
        graph = defaultdict(list)
        output = []

        for (x, y), value in zip(equations, values):    # create the adjacency list to represent the graph
            graph[x].append((y, value))
            graph[y].append((x, 1/value))
        
        def dfs(source, target, weight):
            if source not in graph or target not in graph:
                return -1
            if source == target:
                return weight

            for node, val in graph[source]:
                if node not in visited:
                    visited.add(node)   # we need to add the current node to visited before doing dfs or we have stack overflow
                    result = dfs(node, target, weight*val)
                    if result != -1.0:
                        return result
            return -1.0

        for x, y in queries:
            visited = set() # we need a new set for every query
            output.append(dfs(x, y, 1))

        return output
