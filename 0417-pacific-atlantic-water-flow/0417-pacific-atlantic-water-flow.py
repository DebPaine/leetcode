class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Algorithm 1: Naive and brute force DFS
        Here, we are going through every cell and doing DFS traversal and trying to reach the 
        pacific and atlantic oceans. 
        Time: O(rows*cols)**2
        Space: O(max(rows, cols))

        Algorithm 2: Optimized DFS
        Here, we start from left and top (for pacific ocean) and right and bottom (for atlantic ocean). Since
        we already know that the edges already touch the oceans, we traverse inwards. We check whether the next 
        inward cell's height is greater or equal to current cell's height, and we also check if the current cell
        is already in visited or not. This will help us to not traverse the same cells again and again, as the 
        cell can reach the respective ocean since it's already in the set.
        Note: Have a look at the for loops used to traverse the grid, the conditions might be a bit confusing initially
        but it's pretty intuitive once you think about it.
        """
        # Naive brute force DFS solution
        # rows, cols = len(heights), len(heights[0])
        # output = []

        # def dfs_atlantic(r, c):
        #     nonlocal atlantic
        #     if not (0 <= r < rows) or not (0 <= c < cols):
        #         return
        #     # Check if the current cell reached atlantic or not
        #     if r == rows-1 or c == cols-1:
        #         atlantic = True
        #         return

        #     if r > 0 and heights[r-1][c] <= heights[r][c]:
        #         dfs_atlantic(r-1, c)
        #     if r < rows-1 and heights[r+1][c] <= heights[r][c]:
        #         dfs_atlantic(r+1, c)
        #     if c > 0 and heights[r][c-1] <= heights[r][c]:
        #         dfs_atlantic(r, c-1) 
        #     if c < cols-1 and heights[r][c+1] <= heights[r][c]:
        #         dfs_atlantic(r, c+1)

        # def dfs_pacific(r, c):
        #     nonlocal pacific
        #     if not (0 <= r < rows) or not (0 <= c < cols):
        #         return
        #     # Check if the current cell reached pacific or not
        #     if r == 0 or c == 0:
        #         pacific = True

        #     if r > 0 and heights[r-1][c] <= heights[r][c]:
        #         dfs_pacific(r-1, c)
        #     if r < rows-1 and heights[r+1][c] <= heights[r][c]:
        #         dfs_pacific(r+1, c)
        #     if c > 0 and heights[r][c-1] <= heights[r][c]:
        #         dfs_pacific(r, c-1) 
        #     if c < cols-1 and heights[r][c+1] <= heights[r][c]:
        #         dfs_pacific(r, c+1)

        # for r in range(rows):
        #     for c in range(cols):
        #         atlantic, pacific = False, False
        #         dfs_atlantic(r, c)
        #         dfs_pacific(r, c)
        #         if atlantic and pacific:
        #             output.append([r, c])
        # return output

        # Optimized solution
        rows, cols = len(heights), len(heights[0])
        pacific_set, atlantic_set = set(), set()

        def dfs(r, c, prev_height, visited):  # visited will either be pacific_set or atlantic_set
            if (0 <= r < rows) and (0 <= c < cols) and ((r, c) not in visited) and (heights[r][c] >= prev_height):
                visited.add((r, c))
                dfs(r+1, c, heights[r][c], visited)
                dfs(r-1, c, heights[r][c], visited)
                dfs(r, c+1, heights[r][c], visited)
                dfs(r, c-1, heights[r][c], visited)

        # Start from Pacific ocean
        for c in range(cols):   # go top to bottom, starting at the top edge
            dfs(0, c, heights[0][c], pacific_set)
        for r in range(rows):   # go left to right, starting at the left edge
            dfs(r, 0, heights[r][0], pacific_set) 
        
        # Start from Atlantic ocean
        for c in range(cols-1, -1, -1):  # go from bottom to top, starting at the bottom edge
            dfs(rows-1, c, heights[rows-1][c], atlantic_set)  
        for r in range(rows-1, -1, -1):  # go from right to left, starting at the right edge
            dfs(r, cols-1, heights[r][cols-1], atlantic_set)

        return list(pacific_set & atlantic_set)
