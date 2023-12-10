# -*- coding: utf-8 -*-
import re
import argparse


def parse_cards(lines: list[str]):
    points = 0
    for line in lines:
        winning_numbers, my_numbers = line.split(' | ')
        regex_expr = winning_numbers.replace('  ', ' ').replace(' ', '|')
        matches = re.findall(f"\\b({regex_expr})\\b", my_numbers)
        points += 1 << len(matches) - 1 if matches else 0
    return points


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
