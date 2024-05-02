from __future__ import annotations

import argparse


def extrapolate_history(numbers_list):
    predictions = []
    for numbers in numbers_list:
        differences_list = []
        differences = [y - x for x, y in zip(numbers, numbers[1:])]
        differences_list.append(differences)
        while not all([d == 0 for d in differences]):
            differences = [y - x for x, y in zip(differences, differences[1:])]
            differences_list.append(differences)
        prediction = 0
        for layer in differences_list[::-1]:
            prediction = prediction + layer[-1]
        prediction += numbers[-1]

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
    input_args = parser.parse_args()
    numbers = read_file(input_args.input)
    predictions = extrapolate_history(numbers)
    print(sum(predictions))
