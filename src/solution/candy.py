from typing import List


class Solution:

    def candy(self, ratings: List[int]) -> int:
        children_count = len(ratings)
        left_to_right = [1] * children_count
        right_to_left = [1] * children_count

        for index in range(children_count - 1):
            if ratings[index + 1] > ratings[index]:
                left_to_right[index + 1] = left_to_right[index] + 1

        for index in range(children_count - 1, 0, -1):
            if ratings[index - 1] > ratings[index]:
                right_to_left[index - 1] = right_to_left[index] + 1

        candies = 0
        for index in range(children_count):
            candies += max(left_to_right[index], right_to_left[index])

        return candies

    def candy1(self, ratings: List[int]) -> int:
        children = len(ratings)
        candies = [1] * children
        result = children

        has_change = True
        while has_change:
            has_change = False
            for index in range(children - 1):
                if ratings[index] > ratings[index + 1] and candies[index] <= candies[index + 1]:
                    candies[index] = candies[index + 1] + 1
                    result += 1
                    has_change = True

            for index in range(children - 1, 0, -1):
                if ratings[index] > ratings[index - 1] and candies[index] <= candies[index - 1]:
                    candies[index] = candies[index - 1] + 1
                    result += 1
                    has_change = True

        return result
