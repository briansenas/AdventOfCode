# Summary
Given the following number set
```
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
```
For each row of numbers we will measure the difference between neighbouring numbers.
After, we will go down-up extrapolating A and B as in the following example:
```
0   3   6   9  12  15   B
  3   3   3   3   3   A
    0   0   0   0   0
```
In this case A = 3 and B = 18.
