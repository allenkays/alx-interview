# 0x02. Minimum Operations


## 0. Minimum Operations

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, 

This method calculates the fewest number of operations needed to result in exactly n H characters in the file.

    - Returns an integer
    - If n is impossible to achieve, it returns 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
