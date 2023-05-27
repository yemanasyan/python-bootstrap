class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_dict = dict()
        for char in t:
            if char not in chars_dict:
                chars_dict[char] = 0
            chars_dict[char] += 1

        minimum_window = ""
        start_index, end_index, string_length = 0, 0, len(s)

        while end_index <= string_length:
            # this means that the minimum substring is found
            if all(count <= 0 for count in chars_dict.values()):
                current_window = s[start_index:end_index]
                minimum_window = current_window \
                    if minimum_window == "" or len(current_window) < len(minimum_window) \
                    else minimum_window

                if s[start_index] in chars_dict:
                    chars_dict[s[start_index]] += 1

                start_index += 1
            else:
                if end_index != string_length and s[end_index] in chars_dict:
                    chars_dict[s[end_index]] -= 1

                end_index += 1

        return minimum_window
