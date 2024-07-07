from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 유효한지 확인하기
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            # Check if num is not in the current row and column
            for i in range(9):
                if board[row][i] == num:
                    return False  # 숫자가 현재 행에 이미 있음
                if board[i][col] == num:
                    return False  # 숫자가 현재 열에 이미 있음

            # Check 3x3 sub-box
            start_row = 3 * (row // 3)
            start_col = 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False  # 숫자가 3x3 서브그리드에 이미 있음

            return True

        def backtrack(board: List[List[str]]) -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num  # Place the num
                                if backtrack(board):  # Continue to solve rest of the board
                                    return True
                                board[row][col] = '.'  # Undo the move
                        return False
            return True

        backtrack(board)