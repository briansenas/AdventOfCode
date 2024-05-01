from __future__ import annotations

import argparse
import re


def read_file(input_file, part_two):
    hash_map = {}
    instructions = []
    with open(input_file) as file:
        instructions_str = file.readline()
        instructions = [
            int(x)
            for x in list(
                instructions_str.replace("R", "1").replace("L", "0").strip("\n"),
            )
        ]
        file.readline()  # remove emptyline before map
        while line := file.readline():
            line = re.sub(r"(,|\(|\)|:|=)", "", line)
            line = re.sub(r"\s+", " ", line)
            values = line.strip().split(" ")
            key, left, right = values
            hash_map[key] = [left, right]

    return instructions, hash_map


def transverse_map(instructions, hash_map):
    index = 0
    steps = 1
    location = hash_map["AAA"][instructions[index]]
    while location != "ZZZ":
        index += 1
        steps += 1
        location = hash_map[location][instructions[index % len(instructions)]]

    return steps


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.txt")
    parser.add_argument("--part-two", action="store_true")
    input_args = parser.parse_args()
    instructions, hash_map = read_file(input_args.input, input_args.part_two)
    steps = transverse_map(instructions, hash_map)
    print(steps)
