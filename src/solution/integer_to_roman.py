class Solution:
    def intToRoman(self, num: int) -> str:
        quotient, remainder = divmod(num, 1000)
        roman_number = "".join("M" for _ in range(quotient))

        quotient, remainder = divmod(remainder, 900)
        roman_number = roman_number + "CM" if quotient == 1 else roman_number

        quotient, remainder = divmod(remainder, 500)
        roman_number += "".join("D" for _ in range(quotient))

        quotient, remainder = divmod(remainder, 400)
        roman_number = roman_number + "CD" if quotient == 1 else roman_number

        quotient, remainder = divmod(remainder, 100)
        roman_number += "".join("C" for _ in range(quotient))

        quotient, remainder = divmod(remainder, 90)
        roman_number = roman_number + "XC" if quotient == 1 else roman_number

        quotient, remainder = divmod(remainder, 50)
        roman_number += "".join("L" for _ in range(quotient))

        quotient, remainder = divmod(remainder, 40)
        roman_number = roman_number + "XL" if quotient == 1 else roman_number

        quotient, remainder = divmod(remainder, 10)
        roman_number += "".join("X" for _ in range(quotient))

        quotient, remainder = divmod(remainder, 9)
        roman_number = roman_number + "IX" if quotient == 1 else roman_number

        quotient, remainder = divmod(remainder, 5)
        roman_number += "".join("V" for _ in range(quotient))

        quotient, remainder = divmod(remainder, 4)
        roman_number = roman_number + "IV" if quotient == 1 else roman_number

        quotient, remainder = divmod(remainder, 1)
        roman_number += "".join("I" for _ in range(quotient))

        return roman_number


class Solution1:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[num % 1000 // 100] + X[num % 1000 % 100 // 10] + I[num % 1000 % 100 % 10]
