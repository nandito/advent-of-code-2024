import numpy as np
def solve_part1(lines):
    # Parse numbers from the line
    numbers = np.array([np.fromstring(line.strip(), dtype=int, sep=" ") for line in lines])

    safe_count = 0
    for number_row in numbers:
        diff = np.diff(number_row)
        is_safe = np.all((diff > 0) & (diff < 4)) or np.all((diff < 0) & (diff > -4))
        safe_count += is_safe

    print(safe_count)

