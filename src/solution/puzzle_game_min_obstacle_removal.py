class Solution:

    def remove(self, matrix:list[list[str]]) -> int:
        # calculate the distance between the lowest point of the puzzle and the bottom
        # that will be the distance we need to move down each part of the puzzle
        lowest_distance = self._find_lowest_point_from_bottom(matrix)

        number_of_elements_to_remove = 0
        columns_count = len(matrix[0])
        rows_count = len(matrix)

        for column_index in range(columns_count):
            obstacles_to_remove = set()
            for row_index in range(rows_count - lowest_distance):
                symbol = matrix[row_index][column_index]
                if symbol == "." or symbol == "#":
                    continue

                for following_row_index in range(row_index + 1, row_index + 1 + lowest_distance):
                    if matrix[following_row_index][column_index] == "#":
                        obstacles_to_remove.add(following_row_index)

            number_of_elements_to_remove += len(obstacles_to_remove)

        return number_of_elements_to_remove

    @staticmethod
    def _find_lowest_point_from_bottom(matrix: list[list[str]]) -> int:
        lowest_distance = -1
        # assuming that all rows have equal number of columns
        columns_count = len(matrix[0])
        rows_count = len(matrix)

        for column_index in range(columns_count):
            column_lowest_distance = -1
            for row_index in range(rows_count):
                if matrix[row_index][column_index] == "*":
                    column_lowest_distance = rows_count - row_index - 1

            if column_lowest_distance != -1 and (column_lowest_distance < lowest_distance or lowest_distance == -1):
                lowest_distance = column_lowest_distance

        return lowest_distance
"""
. . * .
# * * #
. # * #
. # # #
"""
