"""
[SUMMARY]
I need to help a elf know if he won some scratchcards for him
to lend me his boat.
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
Everytime there is a match the points double.
Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
Card 4 has one winning number (84), so it is worth 1 point.
Card 5 has no winning numbers, so it is worth no points.
OUTPUT=13.
"""
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
