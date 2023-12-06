class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time = O(n**2), or O(9**2) since we already know the size of the board as 9x9
        Space = O(n**2), or O(9**2) since we are storing values multiple times

        Instead of going through board[r][c] and board[c][r], we don't need to do this since 
        we just have to store which row and which column the current value belongs to and we 
        store it in a hashmap set. This significantly makes the solution easier.
        We are also create boxes of size 3,3 so that we can divide the entire board and see if
        there are repeated values in the boxes or not.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                
                if(board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in boxes[(r//3, c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        
        return True