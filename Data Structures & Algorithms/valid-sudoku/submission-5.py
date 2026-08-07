class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]

        boxes=[set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                piece=board[row][col]

                if(piece=='.'):
                    continue
                
                box=(row//3)*3+col//3

                if(piece in rows[row] or piece in cols[col] or piece in boxes[box]):
                    return False

                rows[row].add(piece)
                cols[col].add(piece)
                boxes[box].add(piece)

        return True