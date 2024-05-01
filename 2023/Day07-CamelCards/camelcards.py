from __future__ import annotations

import argparse
import re


RANKS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
PART_TWO_RANKS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


class Hand:
    def __init__(self, hand: str, bid: int, part_two: bool = False):
        self.hand = hand
        self.bid = bid
        self.points = self.rank(part_two)

    def rank(self, part_two: bool = False):
        points = ""
        hand_set = set(self.hand)
        deck = self.hand
        if part_two and "J" in hand_set:
            j_is = ""
            max_ = 0
            for card in hand_set:
                matches = len(re.findall(card, self.hand.replace("J", card)))
                if matches > max_:
                    j_is = card
                    max_ = matches
            deck = self.hand.replace("J", j_is)
            print(self.hand, deck, j_is)
        for card in set(deck):
            points += str(len(re.findall(card, deck)) - 1)
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


def read_file(input_file, part_two: bool = False):
    hands = []
    with open(input_file) as file:
        while line := file.readline():
            hand, bid = line.strip("\n").split(" ")
            hands.append(Hand(hand, int(bid), part_two))
    hands = sorted(hands)
    return hands


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.txt")
    parser.add_argument("--part-two", action="store_true")
    input_args = parser.parse_args()
    if input_args.part_two:
        RANKS = PART_TWO_RANKS
    hands = read_file(input_args.input, input_args.part_two)
    ranks = []
    for i, hand in enumerate(hands):
        ranks.append(hand.bid * (i + 1))
    print(sum(ranks))
