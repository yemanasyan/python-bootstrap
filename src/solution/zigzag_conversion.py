class Solution:
    def convert(self, s: str, numRows: int) -> str:
        going_down = True
        row_number = 0
        matrix = list()
        column = [None] * numRows
        matrix.append(column)
        for char in s:
            if going_down:
                column[row_number] = char
                row_number += 1
            else:
                column = [None] * numRows
                column[row_number] = char
                matrix.append(column)
                row_number -= 1

            if row_number == numRows:
                going_down = False
                row_number = row_number - 2 if numRows > 1 else 0

            if row_number == 0:
                going_down = True
                column = [None] * numRows
                matrix.append(column)

        result = ""
        for row_number in range(numRows):
            for column in matrix:
                if column[row_number] is not None:
                    result += column[row_number]

        return result
