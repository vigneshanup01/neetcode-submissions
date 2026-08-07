class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        squares={}

        for r in range(9):
            for c in range(9):

                if board[r][c]=='.':
                    continue

                square_key=f"{r//3},{c//3}"

                rows.setdefault(r,set())

                cols.setdefault(c,set())

                squares.setdefault(square_key,set())

                if(
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[square_key]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[square_key].add(board[r][c])

        return True
                