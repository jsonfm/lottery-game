import numpy as np


def consecutiveTripletsEliminator(numbers: list, *args, **kwargs):
    ...


def combinationsRangeEliminator(numbers: list, *args, **kwargs):
    ...


def sumEliminator(numbers: list, sums: list, *args, **kwargs):
    """Checks if the sum of `numbers` is contained by `sums`."""
    return sum(numbers) in sums


def evenOddPatternEliminator(numbers: list, patterns: list, *args, **kwargs):
    """Checks of the even/odd Pattern is completed at least by one term of `numbers`."""
    result = ['O' if x % 2 else 'E' for x in numbers] # ['O', 'E', 'O', 'E', 'O', ...]
    return any(result == pattern for pattern in patterns)


def startsWithEliminator(numbers: list, sums: list, *args, **kwargs):
    """Checks if the first item of `numbers` is contained by `sums`"""
    return numbers[0] in sums


def digitsEliminator(numbers: list, digit: int, *args, **kwargs):
    """Checks if any item of `numbers` is contained by `digit`"""
    return any(number in str(digit) for number in numbers)
