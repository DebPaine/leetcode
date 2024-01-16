class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time: O(m*n), where m is len(grid) and n is len(grid[0])
        Space: O(m*n)

        Steps:
        We have to use multipoint BFS to solve this.
        1. Since there can be multiple rotten oranges in the grid, they can start making other fresh oranges rotten 
        at the same time.
        2. Count the no. of fresh oranges in the grid initially and also add the rotten orange coordinates in a queue.
        3. Start BFS and go through the rotten orange coordinates. The rotten oranges will make other fresh oranges rotten
        in all 4 directions around it. So basically, just traverse using level order BFS traversal.
        4. At the end, check if any fresh oranges remain or not.

        Note: While going through the queue, we also have to check if fresh_oranges > 0 or not, as we can continue going
        through the queue if there are more rotten oranges but no fresh oranges left in the grid.
        """
        minutes = 0
        fresh_oranges = 0
        queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                m, n = queue.popleft()
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

                for row, col in directions:
                    if 0 <= m+row < len(grid) and 0 <= n+col < len(grid[0]) and grid[(m+row)][(n+col)] == 1:
                        grid[(m+row)][(n+col)] = 2
                        fresh_oranges -= 1
                        queue.append((m+row, n+col))
            minutes += 1

        return minutes if fresh_oranges == 0 else -1 
            


        