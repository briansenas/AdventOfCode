# -*- coding: utf-8 -*-
import re
import argparse
from collections import defaultdict


def parse_cards(lines: list[str]):
    points = 0
    for line in lines:
        winning_numbers, my_numbers = line.split(' | ')
        regex_expr = winning_numbers.replace('  ', ' ').replace(' ', '|')
        matches = re.findall(f"\\b({regex_expr})\\b", my_numbers)
        points += 1 << len(matches) - 1 if matches else 0
    return points

def recursive_parse_cards(lines: list[str]):
    num_copies = defaultdict(int)
    for i in range(0, len(lines)):
        num_copies[i] = 1
    def _parse_cards(line: str, index: int = 0):
        if index >= len(lines):
            return 1
        line = lines[index]
        winning_numbers, my_numbers = line.split(' | ')
        regex_expr = winning_numbers.replace('  ', ' ').replace(' ', '|')
        matches = re.findall(f"\\b({regex_expr})\\b", my_numbers)
        for i, _ in enumerate(matches):
            num_copies[index+i+1] += 1*num_copies[index]
        _parse_cards(lines, index+1)
    _parse_cards(lines, 0)
    return sum(num_copies.values())



def read_file(filename: str):
    with open(input_args.input, 'r') as file:
        lines = file.readlines()
    lines = [x.split(':')[-1].strip('\n').strip() for x in lines]
    return lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                        default='input.txt')
    input_args = parser.parse_args()
    lines = read_file(input_args.input)
    print(parse_cards(lines))
    print(recursive_parse_cards(lines))
