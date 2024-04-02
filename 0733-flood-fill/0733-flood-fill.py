class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Time: O(n), where n is the no. of elements in the grid
        Space: O(max(rows, cols)), as we will only store the rows or cols as we do recursion, we won't store all the elements
        Algorithm:
        We can do either DFS or BFS and traverse the image then change the color of the pixels one by one where the condition is satisfied
        """
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]  # we are saving start color as the color will change at image[sr][sc] so we can't use it directly

        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and image[row][col] == start_color:
                image[row][col] = color
                dfs(row+1, col)
                dfs(row, col+1)
                dfs(row-1, col)
                dfs(row, col-1)

        if start_color != color:  # in a case where every pixel is the same in an image, we would have infinite recursion
            dfs(sr, sc)
        return image
