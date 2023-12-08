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
"""
# It will be easier to match using a regular expresion
import re
regex_expr = re.compile(r'[^0-9]')
# Simple: We must first read the input.txt file.
with open('input.txt', 'r') as file:
    # Use generador to reduce memory usage?
    total = 0
    for line in file:
        line_ = re.sub(regex_expr, '', line)
        total += int(line_[0] + line_[-1])
print(total)
