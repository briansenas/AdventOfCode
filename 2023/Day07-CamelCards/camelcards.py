from __future__ import annotations

import argparse
import re


RANKS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.points = self.rank()

    def rank(self):
        points = ""
        for card in set(self.hand):
            points += str(len(re.findall(card, self.hand)) - 1)
        points = points.replace("0", "")
        if points == "12":
            points = "21"
        return points

    def __lt__(self, other):
        return not self > other

    def __gt__(self, other):
        if self.points != other.points:
            return self.points > other.points
        else:
            index = 0
            myrank = RANKS.index(self.hand[index])
            otherrank = RANKS.index(other.hand[index])
            while myrank == otherrank and index < len(self.hand):
                index += 1
                myrank = RANKS.index(self.hand[index])
                otherrank = RANKS.index(other.hand[index])
            return myrank < otherrank

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.hand} {self.points} {self.bid}"


def read_file(input_file):
    hands = []
    with open(input_file) as file:
        while line := file.readline():
            hand, bid = line.strip("\n").split(" ")
            hands.append(Hand(hand, int(bid)))
    hands = sorted(hands)
    return hands


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.txt")
    input_args = parser.parse_args()
    hands = read_file(input_args.input)
    ranks = []
    for i, hand in enumerate(hands):
        ranks.append(hand.bid * (i + 1))
    print(sum(ranks))
