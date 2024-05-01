from __future__ import annotations

import argparse
import re
from functools import reduce


def read_file(input_file, part_two: bool = False):
    with open(input_file) as file:
        time = file.readline()
        distance = file.readline()
    time = time.replace("Time:", "")
    distance = distance.replace("Distance:", "")
    time = re.sub(r"\s+", " ", time)
    distance = re.sub(r"\s+", " ", distance)
    if part_two:
        time = re.sub(r"\s+", "", time)
        distance = re.sub(r"\s+", "", distance)
    times = [int(x) for x in time.strip().split(" ")]
    distances = [int(x) for x in distance.strip().split(" ")]
    return times, distances


def get_total_wins_bruteforce(times, distances):
    total_wins = [0 for _ in range(0, len(times))]
    for i, pairs in enumerate(zip(times, distances)):
        time, distance = pairs
        total_speed = 1
        for t in range(1, time):
            remaining = time - t
            if remaining * total_speed > distance:
                total_wins[i] += 1
            total_speed += 1
    return reduce(lambda x, y: x * y, total_wins)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.txt")
    parser.add_argument("--part-two", action="store_true")
    input_args = parser.parse_args()
    time, distance = read_file(input_args.input, input_args.part_two)
    print(time, distance)
    total_wins = get_total_wins_bruteforce(time, distance)
    print(total_wins)
