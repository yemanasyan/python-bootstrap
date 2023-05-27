class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = list()
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in operations:
                second_number = stack.pop()
                first_number = stack.pop()
                result = operations[token](first_number, second_number)
                stack.append(result)
            else:
                number = int(token)
                stack.append(number)

        return stack.pop()
