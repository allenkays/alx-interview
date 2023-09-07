#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    current_h = 1  # Start with one 'H' in the file
    clipboard = 1  # Start with one 'H' in the clipboard

    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
        current_h += clipboard
        operations += 1

    return operations

# Test the function with the provided example
n = 9
print(minOperations(n))  # Output: 6
