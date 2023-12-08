"""
[SUMMARY]
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

The power of a set of cubes is equal to the numbers of
red, green, and blue cubes multiplied together.
The power of the minimum set of cubes in game 1 is 48.
In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.
"""
import argparse
from cube_conundrum import parse_line, read_file
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str,
                    default='input.txt')
input_args = parser.parse_args()


def power_set(handfuls: list[dict]):
    min_red = min_blue = min_green = 0
    for handful in handfuls:
        min_red = max(handful['red'], min_red)
        min_blue = max(handful['blue'], min_blue)
        min_green = max(handful['green'], min_green)
    return min_red * min_blue * min_green


if __name__ == '__main__':
    lines = read_file(input_args.input)
    lines = [parse_line(line) for line in lines]
    total = sum([power_set(handfuls) for gameid, handfuls in lines])
    print(total)
