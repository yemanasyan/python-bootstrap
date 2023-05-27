from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_count = len(words)
        if words_count == 0:
            return []

        word_length = len(words[0])
        words_map = defaultdict(int)
        for word in words:
            words_map[word] += 1

        permutations_length = words_count * word_length
        indices = list()

        # we stop at len(s) - permutations_length + 1 because that can be max point
        # where a permutation can start
        for index in range(0, len(s) - permutations_length + 1):
            # we make a copy of the words map with an intent to decrease
            # occurrences of each word by once every time we meet starting from index index
            # when we move to the next iteration/index, we must start from the beginning
            words_map_copy = words_map.copy()
            for word_index in range(index, index + permutations_length, word_length):
                word = s[word_index: word_index + word_length]
                words_map_copy[word] -= 1

            # we check that all words have/left zero occurrence, this means that each word from the words
            # met exactly one time.
            # please note due to nature of defaultdict we can have negative values in it,
            # but we don't care, as we check that all of them are equal to zero
            if all(count == 0 for word, count in words_map_copy.items()):
                indices.append(index)

        return indices
