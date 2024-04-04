class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time: O(rows*cols)
        Space: O(max(rows, cols))
        
        Algorithm:
        Very similar to Number of Islands or Flood Fill problems, we have to traverse cells which 
        are 1 using DFS and keep track of the area of the current traversal. We then compare it 
        with the max area and see which is bigger.
        """
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal area
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                area += 1
                grid[r][c] = 0
                dfs(r+1, c)
                dfs(r, c+1)
                dfs(r-1, c)
                dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                area = 0
                dfs(i, j)
                max_area = max(max_area, area)

        return max_area