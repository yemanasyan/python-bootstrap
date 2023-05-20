class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome_start_index = 0
        longest_palindrome_end_index = 0
        for index in range(len(s) - 1):
            # to detect palindrome indexes from babad bab, here you can see the center is letter a
            start_index, end_index = self._get_palindrome_start_and_end(s, index, index)
            if end_index - start_index > longest_palindrome_end_index - longest_palindrome_start_index:
                longest_palindrome_start_index = start_index
                longest_palindrome_end_index = end_index

            # to detect palindrome indexes from baabad baab, here you can see the center are letter a and a
            start_index, end_index = self._get_palindrome_start_and_end(s, index, index + 1)
            if end_index - start_index > longest_palindrome_end_index - longest_palindrome_start_index:
                longest_palindrome_start_index = start_index
                longest_palindrome_end_index = end_index

        return s[longest_palindrome_start_index:longest_palindrome_end_index + 1]

    @staticmethod
    def _get_palindrome_start_and_end(s: str, left_index: int, right_index: int) -> (int, int):
        # this is to cover the following case:
        # imgin the input string is: babad and as left_index we have 1 and right_indedx 2
        # in this case we have no palindrome, that's why we will return two left_index to consider as our
        # palindrome "a"
        if s[left_index] != s[right_index]:
            return left_index, left_index

        while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
            left_index -= 1
            right_index += 1

        return left_index + 1, right_index - 1
