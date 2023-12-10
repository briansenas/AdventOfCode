# SUMMARY
I need to help a elf know if he won some scratchcards for him
to lend me his boat.
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```
Everytime there is a match the points double.\
Card 2 has two winning numbers (32 and 61), so it is worth 2 points.\
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.\
Card 4 has one winning number (84), so it is worth 1 point.\
Card 5 has no winning numbers, so it is worth no points.\
`Expected output: 13`.
# PART 2
There's no such thing as "points". Instead, scratchcards only cause you to
win more scratchcards equal to the number of winning numbers you have.
E.g: 
if card 10 were to have 5 matching numbers, you would win one copy 
each of cards 11, 12, 13, 14, and 15.
Basically, print(len(scratchcards)) after creating the copies.
`Expected output: 30`
"""
