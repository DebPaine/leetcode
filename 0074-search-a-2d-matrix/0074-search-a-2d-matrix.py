class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(log(m)+log(n)) = O(log(m*n))
        Space: O(1)

        Algorithms:
        Both the approaches have the same time complexity. In the second approach, we just need
        to use only one binary search instead of two in the first one. In first approach, we first
        find the correct row, then we try to find the target in the row. In second approach, we treat
        the entire matrix as a row of size m*n and apply binary search on it.
        """
        # # Approach 1: Using two binary searches, one to find the correct row, and the second one to find the element within the row
        # top, bottom = 0, len(matrix)-1
        # row = 0
        # # Binary search to find the correct row
        # while top <= bottom:
        #     m = bottom - (bottom - top)//2
        #     if matrix[m][0] <= target <= matrix[m][-1]:
        #         row = m
        #         break
        #     if target > matrix[m][-1]:
        #         top = m + 1
        #     elif target < matrix[m][0]:
        #         bottom = m - 1

        # # Binary search to find the target in the above row that we found 
        # l, r = 0, len(matrix[row])-1
        # while l <= r:
        #     m = r - (r - l)//2
        #     if target == matrix[row][m]:
        #         return True
        #     if target < matrix[row][m]:
        #         r = m - 1
        #     else:
        #         l = m + 1
        # return False
        

        # Approach 2: We can treat the 2D matrix as 1D sorted array of size m*n as all the rows are sorted
        # To find row: array size // no. of cols
        # To find the col: array size % no. of cols
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows*cols) - 1
        while l <= r:
            m = r - (r - l)//2
            row = m // cols
            col = m % cols
            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                r = m - 1
            else:
                l = m + 1
        
        return False
