class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time: O(rows*cols)
        Space: O(max(rows, cols))
        Algorithm:
        We have to traverse the grid using either BFS or DFS and only traverse when cell is "1". As we 
        traverse, we have to keep marking the cells to something other than 1, 0 in this case, so that 
        we don't traverse it again. After we traversed the entire group of "1" cells, we can consider the
        entire thing as an island and increase the counter by 1.
        Note: We have to use a nested for loop to go through the grid cell by cell as there might be some
        cells which we can't reach directly using DFS as we are only going on 4-directions.
        """
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                grid[r][c] = 0
                dfs(r+1, c)
                dfs(r, c+1)
                dfs(r-1, c)
                dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands