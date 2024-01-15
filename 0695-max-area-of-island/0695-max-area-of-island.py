class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time: O(m*n), where m is len(grid) and n is len(grid[0]), as we are going over each element in the grid
        Space: O(m*n), as the worst case scenario will have all the elements in the grid as 1
        """
        max_area = 0

        def dfs(m, n):
            nonlocal area
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == 1:
                area += 1
                grid[m][n] = 0
                dfs(m + 1, n)
                dfs(m - 1, n)
                dfs(m, n + 1)
                dfs(m, n - 1)
                return 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    max_area = max(max_area, area)

        return max_area