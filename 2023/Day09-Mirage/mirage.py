from __future__ import annotations

import argparse


def extrapolate_history(numbers_list, part_two: bool = False):
    predictions = []
    for numbers in numbers_list:
        differences_list = []
        differences = [y - x for x, y in zip(numbers, numbers[1:])]
        differences_list.append(differences)
        while not all([d == 0 for d in differences]):
            differences = [y - x for x, y in zip(differences, differences[1:])]
            differences_list.append(differences)
        prediction = 0
        if not part_two:
            for layer in differences_list[::-1]:
                prediction = prediction + layer[-1]
            prediction += numbers[-1]
        else:
            for layer in differences_list[::-1]:
                prediction = layer[0] - prediction
            prediction = numbers[0] - prediction

        predictions.append(prediction)
    return predictions


def read_file(input_file):
    numbers = []
    with open(input_file) as file:
        while line := file.readline():
            numbers.append([int(x) for x in line.strip("\n").split(" ")])

    return numbers


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.txt")
    parser.add_argument("--part-two", action="store_true")
    input_args = parser.parse_args()
    numbers = read_file(input_args.input)
    predictions = extrapolate_history(numbers, input_args.part_two)
    print(sum(predictions))
