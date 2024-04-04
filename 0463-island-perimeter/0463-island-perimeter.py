class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Algorithm 1: Using recursive DFS, we don't really need DFS since we are guaranteed to 
        have only one island and there's no need to traverse.
        Time: O(rows*cols)
        Space: O(rows*cols)

        Algorithm 2: Without using recursive DFS, we can just traverse the grid using nested loops
        Time: O(rows*cols)
        Space: O(1), since we don't need a call stack for recursion as compared to above algorithm
        """
        # Using recursive DFS (overkill)
        # perimeter = 0
        # rows, cols = len(grid), len(grid[0])
        # visited = set()

        # def dfs(r, c):
        #     nonlocal perimeter
        #     if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited:
        #         visited.add((r, c))
        #         if r == 0 or grid[r-1][c] == 0:  # cell above is water or we are at top row
        #             perimeter += 1
        #         if r == rows-1 or grid[r+1][c] == 0:
        #             perimeter += 1
        #         if c == 0 or grid[r][c-1] == 0:
        #             perimeter += 1
        #         if c == cols-1 or grid[r][c+1] == 0:
        #             perimeter += 1 
        #         dfs(r+1, c)
        #         dfs(r-1, c)
        #         dfs(r, c+1)
        #         dfs(r, c-1)

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1:
        #             dfs(i, j)

        # return perimeter

        # Without using recursion and saving space
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0 or grid[r-1][c] == 0:
                        perimeter += 1
                    if r == rows-1 or grid[r+1][c] == 0:
                        perimeter += 1
                    if c == 0 or grid[r][c-1] == 0:
                        perimeter += 1
                    if c == cols-1 or grid[r][c+1] == 0:
                        perimeter += 1

        return perimeter