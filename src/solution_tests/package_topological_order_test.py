import unittest

from package_topological_order import get_package_installation_order


class PackageTopologicalOrderTestCase(unittest.TestCase):
    def test_get_package_installation_order(self):
        test_data = [
            (
                [
                    (1, 2),
                    (1, 3),
                    (3, 4),
                    (4, 5),
                    (2, 5),
                    (1, 5),
                    (6, 7)
                ],
                [5, 2, 4, 3, 1, 7, 6]
            ),
            (
                [
                    (1, 2),
                    (1, 3),
                    (3, 4),
                    (4, 5),
                    (5, 1)
                ],
                None
            )
        ]

        for dependencies, expected_result in test_data:
            with self.subTest(dependencies=dependencies, expected_result=expected_result):
                result = get_package_installation_order(dependencies)
                self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
