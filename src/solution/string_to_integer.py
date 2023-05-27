class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        negative = False
        first_digit_met = False
        max_negative = 2 ** 31
        max_positive = max_negative - 1

        for index, char in enumerate(s):
            if char >= "0" and char <= "9":
                result = result * 10 + int(char)

                if negative and result > max_negative:
                    return -max_negative

                if not negative and result > max_positive:
                    return max_positive

                first_digit_met = True
            elif char == "-" and not first_digit_met:
                negative = True
                first_digit_met = True
            elif char == "+" and not first_digit_met:
                negative = False
                first_digit_met = True
            elif char != " " or first_digit_met:
                break

        return -result if negative else result
