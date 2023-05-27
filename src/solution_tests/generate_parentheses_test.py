import unittest


class GenerateParenthesesTestCase(unittest.TestCase):
    def test_generate_parentheses(self):
        test_data = [
            (
                ["()(())()", "()()()()", "((()))()", "(()())()", "(())()()", "(()()())", "()(()())", "()()(())",
                 "((())())", "(()(()))", "((()()))", "()((()))", "(((())))"],
                ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())",
                 "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
            )
        ]

        for result, expected_result in test_data:
            for expected_item in expected_result:
                if expected_item not in result:
                    print(f"Missing item: {expected_item}")


if __name__ == '__main__':
    unittest.main()
