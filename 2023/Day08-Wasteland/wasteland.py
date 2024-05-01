from __future__ import annotations

import argparse
import re

import numpy as np


def read_file(input_file, part_two):
    hash_map = {}
    instructions = []
    start_nodes = []
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
            if key.endswith("A"):
                start_nodes += [key]
            hash_map[key] = [left, right]

    return instructions, hash_map, start_nodes


def transverse_map(instructions, hash_map):
    index = 0
    steps = 1
    location = hash_map["AAA"][instructions[index]]
    while location != "ZZZ":
        index += 1
        steps += 1
        location = hash_map[location][instructions[index % len(instructions)]]

    return steps


def transverse_all_maps(instructions, hash_map, start_nodes):
    def _transverse_map(start_node):
        _index = 0
        _steps = 1
        location = hash_map[start_node][instructions[_index]]
        while not location.endswith("Z"):
            _index += 1
            _steps += 1
            location = hash_map[location][instructions[_index % len(instructions)]]

        return _steps

    steps = 1
    steps_per_start = []
    for start in start_nodes:
        steps_per_start.append(_transverse_map(start))

    steps = np.lcm.reduce(np.asarray(steps_per_start))
    print(steps_per_start)
    return steps


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.txt")
    parser.add_argument("--part-two", action="store_true")
    input_args = parser.parse_args()
    instructions, hash_map, start_nodes = read_file(
        input_args.input,
        input_args.part_two,
    )
    if not input_args.part_two:
        steps = transverse_map(instructions, hash_map)
    else:
        steps = transverse_all_maps(instructions, hash_map, start_nodes)
    print(steps)
