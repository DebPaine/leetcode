class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Time: O(m*n) creating the prefix matrix, calculating prefix sum is O(1)
        Space: O(m*n) storing the prefix matrix

        https://www.youtube.com/watch?v=WibxoqMSMCw
        """
        self.prefix_matrix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.prefix_matrix[i][j] = self.prefix_matrix[i-1][j] + self.prefix_matrix[i][j-1] - self.prefix_matrix[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix_sum = self.prefix_matrix[row2+1][col2+1] - self.prefix_matrix[row2+1][col1] - self.prefix_matrix[row1][col2+1] + self.prefix_matrix[row1][col1]
        return prefix_sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)