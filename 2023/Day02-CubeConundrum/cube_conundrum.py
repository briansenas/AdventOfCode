"""
[SUMMARY]
I'm at Snow Island...long walk.. elf invites us to play a game...
Elf has a bag with small cubes... red, green or blue.
He will hide a secret amount of cubes in the bag.
He will show a handful of cubes couple times:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
Which games would have been possible if the bag contained
ONLY 12 red cubes, 13 green cubes, and 14 blue cubes?
"""
import argparse
from collections import defaultdict
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str,
                    default='input.txt')
parser.add_argument('--red', type=int, default=12)
parser.add_argument('--blue', type=int, default=14)
parser.add_argument('--green', type=int, default=13)
input_args = parser.parse_args()

MAX_RED = input_args.red
MAX_BLUE = input_args.blue
MAX_GREEN = input_args.green


def parse_handful(line: str):
    values = line.strip().split(',')
    handful = defaultdict(int)
    for value in values:
        amount, key = value.strip().split(' ')
        handful[key] = int(amount)
    return handful


def parse_line(line: str):
    gameid, handfuls = line.split(':')
    gameid = int(gameid.split(' ')[-1])
    handfuls = handfuls.split(';')
    handfuls = [parse_handful(handful) for handful in handfuls]
    return (gameid, handfuls)


def is_allowed(handfuls: list[dict]):
    return all([handful['red'] <= MAX_RED and
                handful['blue'] <= MAX_BLUE and
                handful['green'] <= MAX_GREEN
                for handful in handfuls])


with open(input_args.input, 'r') as file:
    lines = file.readlines()
lines = [parse_line(line) for line in lines]
total = sum([gameid for gameid, handfuls in lines if is_allowed(handfuls)])
print(total)
