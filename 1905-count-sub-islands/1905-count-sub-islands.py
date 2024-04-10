class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        Optimized approach:
        Time: O(rows*cols)
        Space: O(max(rows, cols))

        Algorithm:
        We use "Reverse Thinking" to solve this in an optimized way. We first remove all the non-subislands from grid2.
        This will leave us with only the valid subislands.
        """
        # Brute force, test cases passed but TLE when submitting
        # subislands = 0
        # islands1 = set()
        # islands2 = set()
        # rows, cols = len(grid1), len(grid1[0])   # size of grid1 and grid2 are same as mentioned in the constraints
        
        # def dfs(r, c, grid):
        #     if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
        #         island.add((r, c))
        #         grid[r][c] = 0
        #         dfs(r+1, c, grid)
        #         dfs(r-1, c, grid)
        #         dfs(r, c+1, grid)
        #         dfs(r, c-1, grid)

        # # Traversing grid1
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid1[r][c] == 1:
        #             island = set()
        #             dfs(r, c, grid1)
        #             islands1.add(frozenset(island))
        
        # # Traversing grid2
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid2[r][c] == 1:
        #             island = set()
        #             dfs(r, c, grid2)
        #             islands2.add(frozenset(island))
        
        # for i1 in islands1:
        #     for i2 in islands2:
        #         if i2.issubset(i1):
        #             subislands += 1
        # return subislands

        # Optimized solution
        sub_islands = 0
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid2[r][c] == 1:
                grid2[r][c] = 0
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        # Step 1: Go through grid2 and remove all the guaranteed non-subislands
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and grid1[r][c] == 0:   # if grid2 cell is land and grid1 cell is water
                    dfs(r, c)
                
        # Step 2: After removing all the non-subislands from grid2, we will check where grid2 and grid1 cells are both 1
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and grid1[r][c] == 1:   # if grid2 cell is land and grid1 cell is water
                    dfs(r, c)
                    sub_islands += 1
        return sub_islands

