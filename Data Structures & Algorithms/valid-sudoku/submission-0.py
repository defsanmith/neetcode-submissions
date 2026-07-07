class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_unit(unit):
            unit = [num for num in unit if num != '.']
            return len(unit) == len(set(unit))

        for row in board:
            if not is_valid_unit(row):
                return False

        for col in zip(*board):
            if not is_valid_unit(col):
                return False

        for base_row in range(0, 9, 3):
            for base_col in range(0, 9, 3):
                box = [
                    board[r][c]
                    for r in range(base_row, base_row + 3)
                    for c in range(base_col, base_col + 3)
                ]
                if not is_valid_unit(box):
                    return False

        return True
        