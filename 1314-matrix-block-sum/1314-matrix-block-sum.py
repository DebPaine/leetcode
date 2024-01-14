class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        Steps:
        1. Create a prefix sum matrix
        2. Add padding of k zeroes all around the prefix matrix of size len(mat)xlen(mat[0])
        3. Fill the prefix matrix but exclude the k padding on each side of the matrix

        We don't have to add padding of k on either side of the prefix sum matrix, we can just add a single padding.
        This will simply calculating the block sum in answer matrix and we can use the following trick:
        r1, c1 = max(0, i-k), max(0, j-k)
        r2, c2 = min(rows-1, i+k), min(cols-1, j+k)
        Here, 
        (r1, c1) is for the top left corner of the block (i-k, j-k)
        (r2, c2) is for the bottom right corner of the block (i+k, j+k)
        
        Visit this problem again as it's confusing!
        Prerequisites:
        https://leetcode.com/problems/range-sum-query-immutable/
        https://leetcode.com/problems/range-sum-query-2d-immutable/
        """
        rows, cols = len(mat), len(mat[0])
        p = [[0]*(cols+1) for _ in range(rows+1)]  # +1 since we need a padding of 0
        answer = [[0]*cols for _ in range(rows)]
        
        # Fill the prefix sum array
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                p[i][j] = mat[i-1][j-1] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]

        # Compute the block sum for every (i,j) in answer matrix
        for i in range(rows):
            for j in range(cols):
                # To handle out of bounds scenarios
                r1, c1 = max(0, i-k), max(0, j-k)  # top left corner of block indices, if index becomes less than 0
                r2, c2 = min(rows-1, i+k), min(cols-1, j+k)  # bottom right corner of block indices, if index becomes greater than rows or cols
                answer[i][j] = p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1]

        return answer

        
                
        
