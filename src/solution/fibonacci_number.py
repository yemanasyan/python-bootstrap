from time import time

# Memoization using a dictionary as a cache
cache = {
    0: 0,
    1: 1,
}


def fibonacci(num: int) -> int:
    if num in cache:
        return cache[num]

    # this way if we call fibonacci_number(3) we will populate all the values for 0, 1, 2, 3 indexes, store in
    # cache and later if we call fibonacci_number with a number lower than equal 3 we will get the
    # result in a constant time
    # this is called memoization
    value = fibonacci(num - 1) + fibonacci(num - 2)
    cache[num] = value
    return value


def fibonacci_with_safe_recursion_depth(num: int) -> int:
    start_num = min(num, 998)
    for number in range(start_num, num, 990):
        fibonacci(number)

    return fibonacci(num)


if __name__ == "__main__":
    start = time()
    print(f"fibonacci number for 20000: {fibonacci_with_safe_recursion_depth(20000)}. Duration: {time() - start}")
    start = time()
    print(f"fibonacci number for 10000: {fibonacci_with_safe_recursion_depth(1000)}. Duration: {time() - start}")
