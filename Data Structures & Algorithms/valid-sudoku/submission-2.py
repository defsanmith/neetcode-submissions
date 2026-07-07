from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                item = board[i][j]

                if item == '.':
                    continue

                square_idx = (i // 3) * 3 + j // 3

                if item in row_set[i] or item in col_set[j] or item in square_set[square_idx]:
                    return False
                
                row_set[i].add(item)
                col_set[j].add(item)
                square_set[square_idx].add(item)


        return True