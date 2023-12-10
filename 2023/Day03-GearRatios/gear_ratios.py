"""
[SUMMARY]
You need to use a gondola lift... it's broken.
You offer to help. There seems to be a part missing.
If you can add up all the part numbers in the engine schematic,
it should be easy to work out which part is missing.
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
Apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum (4361)
[PART TWO]

"""
import re
import math as m
import argparse
from utils import check_around, check_left, check_right, check_vertical, \
    get_adyacent_values


def sum_symbols(lines: list[str]):
    symbol_expr = re.compile('[^0-9.]')
    first_line_matches = re.finditer(symbol_expr, lines[0])
    value = 0
    # Edge case 1: The first line only checks horizontaly and below.
    for match in first_line_matches:
        left, lines[0] = check_left(match.start(), lines[0])
        right, lines[0] = check_right(match.start(), lines[0])
        below, lines[1] = check_vertical(match.start(), lines[1])
        value += left + right + below
    # All the other methods check_around them
    for i in range(1, len(lines)-1):
        line = lines[i]
        matches = re.finditer(symbol_expr, line)
        for match in matches:
            around, lines[i-1:i+2] = check_around(match.start(),
                                                  lines[i-1:i+2])
            value += around
    # Edge case 2: The last line only checks horizontaly and above.
    last_line_matches = re.finditer(symbol_expr, lines[-1])
    for match in last_line_matches:
        left, lines[-1] = check_left(match.start(), lines[-1])
        right, lines[-1] = check_right(match.start(), lines[-1])
        above, lines[-2] = check_vertical(match.start(), lines[-2])
        value += left + right + above
    return value


def mul_symbols(lines: list[str]):
    symbol_expr = re.compile('[^0-9.]')
    first_line_matches = re.finditer(symbol_expr, lines[0])
    value = 0
    # Edge case 1: The first line only checks horizontaly and below.
    for match in first_line_matches:
        left, lines[0] = check_left(match.start(), lines[0])
        right, lines[0] = check_right(match.start(), lines[0])
        below, lines[1] = check_vertical(match.start(), lines[1])
        values = list(filter(lambda x: x != 0, [left, right, below]))
        if len(values) >= 2:
            value += m.prod(values)
    # All the other methods check_around them
    for i in range(1, len(lines)-1):
        line = lines[i]
        matches = re.finditer(symbol_expr, line)
        for match in matches:
            around, lines[i-1:i+2] = get_adyacent_values(match.start(),
                                                         lines[i-1:i+2])
            around = list(filter(lambda x: x != 0, around))
            if len(around) >= 2:
                value += m.prod(around)
    # Edge case 2: The last line only checks horizontaly and above.
    last_line_matches = re.finditer(symbol_expr, lines[-1])
    for match in last_line_matches:
        left, lines[-1] = check_left(match.start(), lines[-1])
        right, lines[-1] = check_right(match.start(), lines[-1])
        above, lines[-2] = check_vertical(match.start(), lines[-2])
        values = list(filter(lambda x: x != 0, [left, right, above]))
        if len(values) >= 2:
            value += m.prod(values)
    return value


def read_file(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [x.strip('\n') for x in lines]
    return lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                        default='input.txt')
    input_args = parser.parse_args()
    lines = read_file(input_args.input)
    print(sum_symbols(lines.copy()))
    print(mul_symbols(lines.copy()))
