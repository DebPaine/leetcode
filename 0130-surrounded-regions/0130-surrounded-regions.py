class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Algorithm 1: Brute force DFS
        We can go through all the cells in the board and find the surrounded regions and mark it to O.
        This is very inefficient and messy to find the surrounded regions in the first place.

        Algorithm 2: "Reverse Thinking" 
        Instead of searching for surrounded regions, we find the unsurrounded regions. This is easier to 
        find since we can just search the borders of the board and see which cells are marked as "O". These
        cells will be guaranteed to be unsurrounded regions, since atleast one of the region will be out of
        the board. We then mark these border cells as "T" (temporary) and we go through the entire board
        to mark all the remaining "O"s to "X" as these "O"s will be the surrounded regions. We then go 
        through the board again and convert the "T"s to "X"s.
        """
        rows, cols = len(board), len(board[0]) 

        def dfs(r, c):
            if (0 <= r < rows) and (0 <= c < cols) and board[r][c] == "O":
                board[r][c] = "T"   # mark it to "T" temporarily
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        # Step 1: Mark all unsurrounded regions (or border cells) which are "O" to "T"
        for r in range(rows):
            dfs(r, 0)   # traverse left border
            dfs(r, cols-1)  # traverse right border 

        for c in range(cols):
            dfs(0, c)   # traverse top border
            dfs(rows-1, c)  # traverse bottom border
        
        # Step 2: Go through the entire board and mark all the remaining "O"s (surrounded region) to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Step 3: Mark all the "T"s back to "O"s as these are the unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
            