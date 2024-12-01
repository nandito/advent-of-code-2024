import numpy as np


def solve_part2(lines):
    # Parse numbers from the line
    numbers = [tuple(map(int, line.strip().split())) for line in lines]
    # transpose the list of tuples
    numbers = np.array(numbers).T
    # count the array's first items' occurrence in the array's second items and multiply by the first item
    similiraty_score = np.array([np.count_nonzero(numbers[0] == n) * n for n in numbers[1]])
    print(np.sum(similiraty_score))

