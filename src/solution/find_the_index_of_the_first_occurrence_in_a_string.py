class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length, needle_length = len(haystack), len(needle)
        if haystack_length < needle_length:
            return -1

        pattern_hash_value = 0
        for s in needle:
            pattern_hash_value += hash(s)

        current_hash_value = 0
        for index in range(needle_length - 1):
            current_hash_value += hash(haystack[index])

        for index in range(needle_length - 1, haystack_length):
            current_hash_value += hash(haystack[index])
            starting_index = index - needle_length + 1
            if pattern_hash_value == current_hash_value:
                if haystack[starting_index:index + 1] == needle:
                    return starting_index

            current_hash_value -= hash(haystack[starting_index])

        return -1
