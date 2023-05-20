def all_unique_chars_solution_1(symbols: str) -> bool:
    """
    This method returns True if all provided chars are unique. Otherwise, False.
    It expects only ANSI chars. It uses a list of bool that shows whether a char with corresponding ANSI code
    detected before, if so the method will immediately return False when it detects the first not unique char.

    :param symbols: the string that must be checked
    :return: the result
    """
    if len(symbols) > 128:
        return False

    # All ANSI chars have their int code from 0 to 128, we will use it. For example a has a value 97
    chars_by_code = [False] * 128
    for single_char in symbols:
        char_code = ord(single_char)
        if chars_by_code[char_code]:
            return False

        chars_by_code[char_code] = True

    return True

def all_unique_chars_solution_2(symbols: str) -> bool:
    """
    This method returns True if all provided chars are unique. Otherwise, False.
    It expects only ANSI chars. It uses a list of bool that shows whether a char with corresponding ANSI code
    detected before, if so the method will immediately return False when it detects the first not unique char.

    :param symbols: the string that must be checked
    :return: the result
    """

    if len(symbols) > 128:
        return False

    int_size = 32
    number_of_buckets = 128 // int_size
    chars_by_code = [0] * number_of_buckets

    for single_char in symbols:
        char_code = ord(single_char) - ord("a")
        bucket = char_code // int_size
        position = char_code % int_size
        char_bucket_code = 1 << position
        chars_by_code[bucket] = chars_by_code[bucket] ^ char_bucket_code

        if chars_by_code[bucket] >> position & 1 != 1:
            return False

    return True