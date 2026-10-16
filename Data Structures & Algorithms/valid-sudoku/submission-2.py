class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # One set per row, per column and per 3x3 box.
        # Each set holds the digits already seen in that group.
        digits_in_row = [set() for _ in range(9)]
        digits_in_column = [set() for _ in range(9)]
        digits_in_box = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                digit = board[row][column]

                if digit == '.':                 # empty cell, nothing to check
                    continue

                box = (row // 3) * 3 + column // 3   # which 3x3 box, numbered 0 to 8

                if (digit in digits_in_row[row]
                        or digit in digits_in_column[column]
                        or digit in digits_in_box[box]):
                    return False                 # repeated digit in a row, column or box

                digits_in_row[row].add(digit)
                digits_in_column[column].add(digit)
                digits_in_box[box].add(digit)

        return True