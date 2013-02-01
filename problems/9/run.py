#!/usr/bin/env python3

from functools import reduce


def sum_of_squares(nums):
    return reduce(lambda x, y: x + y ** 2, nums)


def square_of_sums(nums):
    return sum(nums) ** 2


nums = range(1, 101)
result = square_of_sums(nums) - sum_of_squares(nums)
print(result)
