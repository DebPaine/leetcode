class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(log(m)+log(n)) or O(log(m*n)), where m is no. of rows and n is no. of cols
        Space: O(1)
        """
        # Instead of doing two binary searches, we can treat the entire matrix as a single sorted array
        # rows, cols = len(matrix), len(matrix[0])
        # l, r = 0, rows*cols-1

        # while l <= r:
        #     mid = r - (r  - l)//2
        #     # Find which row and col the mid index belongs to
        #     row, col = mid // cols, mid % cols
        #     if target < matrix[row][col]:
        #         r = mid - 1
        #     elif target > matrix[row][col]:
        #         l = mid + 1
        #     else:
        #         return True

        # return False

        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = top - (top - bot)//2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
            
        # # There can be a situation where top > bot and we didn't break out from the above loop
        # if top > bot:
        #     return False

        # We got the required row from above
        l, r = 0, cols - 1
        while l <= r:
            mid = r - (r - l)//2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True

        return False