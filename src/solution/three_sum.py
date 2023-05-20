class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        """
        This method returns all unique three numbers list which summary is equal to 0
        :param nums: the list of numbers
        :return: list that contains list of values
        """

        result = set()
        sorted_numbers = sorted(nums)
        numbers_length = len(sorted_numbers)

        for i in range(numbers_length - 2):
            j = i + 1
            z = numbers_length - 1

            while j < z:
                numbers_sum = sorted_numbers[i] + sorted_numbers[j] + sorted_numbers[z]
                if numbers_sum == 0:
                    result.add((sorted_numbers[i], sorted_numbers[j], sorted_numbers[z]))
                    j = j + 1
                    z = z - 1
                elif numbers_sum > 0:
                    z = z - 1
                else:
                    j = j + 1

        return [list(values) for values in result]

    def threeSum2(self, numbers: [int]) -> [[int]]:
        """
        This method returns all unique three numbers list which summary is equal to 0
        :param numbers: the list of numbers
        :return: list that contains list of values
        """

        result = list()
        sorted_numbers = sorted(numbers)
        numbers_length = len(sorted_numbers)

        for i in range(numbers_length - 2):
            # two filter out duplicates
            if i != 0 and sorted_numbers[i - 1] == sorted_numbers[i]:
                continue

            j = i + 1
            z = numbers_length - 1

            while j != z:
                if j != i + 1 and sorted_numbers[j] == sorted_numbers[j - 1]:
                    j = j + 1
                    continue

                if z != numbers_length - 1 and sorted_numbers[z] == sorted_numbers[z + 1]:
                    z = z - 1
                    continue

                numbers_sum = sorted_numbers[i] + sorted_numbers[j] + sorted_numbers[z]
                if numbers_sum == 0:
                    result.append([sorted_numbers[i], sorted_numbers[j], sorted_numbers[z]])
                    z = z - 1
                elif numbers_sum > 0:
                    z = z - 1
                else:
                    j = j + 1

        return result