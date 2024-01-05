class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Recursive DFS:
        Time: O(m*n), where m is the rows and n is the cols
        Space: O(m*n), as in worst case scenario, we can have all 1's and the call stack will have m*n dfs() recursive calls
        
        Iterative DFS:
        Time: O(m*n)
        Space: O(m*n)
        For iterative approach, just remember to only enter DFS if grid[i][j] == "1" so that it's easier to count islands

        Iterative BFS:
        Time: O(m*n)
        Space: O(m*n)

        https://stackoverflow.com/questions/50901203/dfs-and-bfs-time-and-space-complexities-of-number-of-islands-on-leetcode
        """
        # # Recursive DFS
        # islands = 0
        # def dfs(m, n):
        #     if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == "1":
        #         grid[m][n] = "0"
        #         dfs(m+1, n)
        #         dfs(m-1, n)
        #         dfs(m, n+1)
        #         dfs(m, n-1)
        #         return True
        #     else:
        #         return False
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if dfs(i, j):
        #             islands += 1
        # return islands


        # # Iterative DFS
        # islands = 0
        # def dfs(i, j):
        #     nonlocal islands
        #     stack = [(i, j)]
        #     while stack:
        #         m, n = stack.pop()
        #         if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == "1":
        #             grid[m][n] = "0"
        #             stack.append((m+1, n))
        #             stack.append((m-1, n))
        #             stack.append((m, n+1))
        #             stack.append((m, n-1))
        #     islands += 1

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "1":
        #             dfs(i, j)
        # return islands

        # Iterative BFS
        islands = 0
        def bfs(i, j):
            nonlocal islands
            queue = deque([(i, j)])
            while queue:
                m, n = queue.popleft()
                if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == "1":
                    grid[m][n] = "0"
                    queue.append((m+1, n))
                    queue.append((m-1, n))
                    queue.append((m, n+1))
                    queue.append((m, n-1))
            islands += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
        return islands