class Solution:
    def reverse(self, x: int) -> int:
        positive = True if x >=0 else False
        x = abs(x)
        result = 0
        min_value = 2**31
        max_value = 2**31 - 1

        while x != 0:
            result = result * 10 + x % 10
            x = x // 10
            if positive and result > max_value or not positive and result > min_value:
                return 0

        return result if positive else -result

class Solution1:
    def reverse(self, x: int) -> int:
        if x >= 0:
            y = int(str(x)[::-1])
            return y if y < 2147483648 else 0

        else:
            y = -int(str(x)[:0:-1])
            return y if y > -2147483648 else 0

