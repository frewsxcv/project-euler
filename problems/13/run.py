#!/usr/bin/env python3

with open("input.txt") as infile:
   nums = [int(line.strip()) for line in infile]

total_sum = sum(nums)
print(str(total_sum)[:10])
