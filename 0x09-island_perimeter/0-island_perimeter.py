#!/usr/bin/python3
"""
Function to determine the perimeter of an Island defined by a grid
"""


def island_perimeter(grid):
    """
    This function determines the perimeter of an island

    Args:
        grid (list of lists): square grid of 0's and 1's

    Returns:
        perimeter (int): perimeter of the island represented by connected ones
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add all four sides of a square
                perimeter += 4

                # Check if left neighbour is water or land
                if col > 0 and grid[row][col - 1] == 1:
                    # subract two for shared sides (one from each)
                    perimeter -= 2

                # Check if top neighbor is water or  land
                if row > 0 and grid[row - 1][col] == 1:
                    # subtract 2 for shared sides (one from each)
                    perimeter -= 2

    return perimeter


if __name__ == "__main__":
    island_perimeter(grid)
