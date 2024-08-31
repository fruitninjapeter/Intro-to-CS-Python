def is_even(n):
    return (n % 2) == 0


def in_an_interval(n):
    # The intervals are [2,9), (47,92), (12, 19], and [101,103]
    return (2 <= n < 9) or (47 < n < 92) or (12 < n <= 19) or (101 <= n <= 103)