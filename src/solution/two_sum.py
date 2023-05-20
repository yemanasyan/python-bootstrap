class Solution:

    def twoSum(self, numbers: list[int], summary: int) -> list[list[int]]:
        """
        The method returns all unique pairs of ints which summary is equal to the provided value
        :param numbers: list of int
        :param summary: the summary that must be checked
        :return: list of pairs
        """
        sorted_numbers = sorted(numbers)
        result = list()
        sorted_numbers_length = len(sorted_numbers)
        for i in range(sorted_numbers_length - 1):
            # To keep the uniqueness
            if i > 0 and sorted_numbers[i - 1] == sorted_numbers[i]:
                continue

            j = sorted_numbers_length - 1

            while i != j:
                numbers_sum = sorted_numbers[i] + sorted_numbers[j]
                if numbers_sum == summary:
                    result.append([sorted_numbers[i], sorted_numbers[j]])
                    break
                elif numbers_sum > summary:
                    j = j - 1
                else:
                    break

        return result