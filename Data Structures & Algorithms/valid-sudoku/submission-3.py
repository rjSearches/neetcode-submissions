class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # 1. Check the rest of the row
                for col_idx in range(9):
                    if col_idx != c and board[r][col_idx] == val:
                        return False

                # 2. Check the rest of the column
                for row_idx in range(9):
                    if row_idx != r and board[row_idx][c] == val:
                        return False

                # 3. Check the rest of the 3x3 box
                start_row, start_col = 3 * (r // 3), 3 * (c // 3)
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if (i != r or j != c) and board[i][j] == val:
                            return False

        return True