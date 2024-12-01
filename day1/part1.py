import numpy as np
def solve_part1(lines):
    # Parse numbers from the line
    numbers = [tuple(map(int, line.strip().split())) for line in lines]
    # transpose the list of tuples
    numbers = np.array(numbers).T
    # order the numbers in each tuple
    numbers = [sorted(t) for t in numbers]
    # extract the differences between the two lists
    diffs = np.array(numbers[1]) - np.array(numbers[0])
    # get the absolute value of the differences
    diffs = np.abs(diffs)
    # print the sum of the differences
    print(np.sum(diffs))

