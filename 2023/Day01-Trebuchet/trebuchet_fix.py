# -*- coding: utf-8 -*-
"""
Summary of the problem:
Given a map with the possible places with problems.
I need to check all 50 stars.

The calibration document has ben amended...
Each line of text contains a specific calibration value.
The value is found by:
    - Combining the **first_digit** and the **last_digit**
        to form a two-digit number.

Example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

becomes: 12, 38, 15, 77 and therefore 142
[FIX]: Some digits are actually spelled out ... one..two..three
"""
# It will be easier to match using a regular expresion
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str,
                    default='input.txt')
input_args = parser.parse_args()
words_numbers = [
    "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
]
regex_expr = re.compile(r'[1-9]')
# Simple: We must first read the input.txt file.
total = 0
with open(input_args.input, 'r') as file:
    # The file ain't too big so:
    lines = file.read().strip()
    for i in range(1, 10):
        value = words_numbers[i-1]
        lines = lines.replace(value, f'{value}{i}{value}')
    lines = lines.split('\n')
    matches = [re.findall(regex_expr, line) for line in lines]
    total = sum(int(match[0] + match[-1]) for match in matches)
print(total)
