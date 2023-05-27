class Solution:

    def __init__(self):
        self._numbers_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        digit = digits[0]
        if digit < "2" or digit > "9":
            raise Exception(f"Invalid symbol {digit}. Only symnols 2 to 9 are allowed")

        if len(digits) == 1:
            return self._numbers_to_letters[digit]

        letter_combinations = self.letterCombinations(digits[1:])
        new_letter_combinations = list()
        for letter in self._numbers_to_letters[digit]:
            for combination in letter_combinations:
                new_letter_combinations.append(letter + combination)

        return new_letter_combinations
