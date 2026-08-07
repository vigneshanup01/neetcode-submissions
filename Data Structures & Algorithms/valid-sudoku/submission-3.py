from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]    # 9 row sets
        cols = [set() for _ in range(9)]    # 9 column sets
        boxes = [set() for _ in range(9)]   # 9 box sets

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                # Box numbering:
                # 0 1 2
                # 3 4 5
                # 6 7 8
                box = (r // 3) * 3 + (c // 3)

                if (
                    num in rows[r]
                    or num in cols[c]
                    or num in boxes[box]
                ):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True