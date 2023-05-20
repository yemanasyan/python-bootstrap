def permutation(value1: str, value2: str) -> bool:
    """
    The permutation of string is the set of all the strings, that contains the same characters as the original string,
    but the order of the arrangement of the characters can be different.
    :param value1:
    :param value2:
    :return: True if the provided two string are permutations, otherwise False
    """
    value1_sorted = sorted(value1)
    value2_sorted = sorted(value2)

    return value1_sorted == value2_sorted