class Solution:
    """
    This is the sliding window solution, which means if the letter accrued before instead of returning to the last
    starting point + 1 position and continuing checking and finding substrings we can just pass through each char
    only once and consider the start of a substring the last occasion of the string + 1. Please note the last occasion
    can be before the current start, because after changing the start we don't clean up chars before it.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_dict = dict()
        start = 0
        max_length = 0

        for index, char in enumerate(s):
            if char in chars_dict:
                # because we don't erase chars before the current start
                start = max(chars_dict[char] + 1, start)

            chars_dict[char] = index
            max_length = max(max_length, index - start + 1)

        return max_length


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        current_substring_length = 0
        last_starting_char_index = 0
        current_index = 0
        unique_chars_set = set()

        while current_index < len(s):
            current_char = s[current_index]
            char_exist = current_char in unique_chars_set
            if not char_exist:
                unique_chars_set.add(current_char)
                current_substring_length = current_substring_length + 1
                longest_substring_length = max(longest_substring_length, current_substring_length)
                current_index = current_index + 1

            if char_exist or current_index == len(s):
                unique_chars_set = set()
                last_starting_char_index = last_starting_char_index + 1
                current_index = last_starting_char_index
                current_substring_length = 0

        return longest_substring_length
