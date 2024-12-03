import numpy as np
def solve_part2(lines):
    # Parse numbers from the line
    numbers = np.array([np.fromstring(line.strip(), dtype=int, sep=" ") for line in lines])

    safe_count = 0
    for number_row in numbers:
        diff = np.diff(number_row)
        is_safe = np.all((diff > 0) & (diff < 4)) or np.all((diff < 0) & (diff > -4))
        if is_safe:
            safe_count += is_safe
        else:
            # Check if the row is safe if we remove one element
            for i in range(len(number_row)):
                new_row = np.delete(number_row, i)
                new_diff = np.diff(new_row)
                is_safe = np.all((new_diff > 0) & (new_diff < 4)) or np.all((new_diff < 0) & (new_diff > -4))
                if is_safe:
                    safe_count += is_safe
                    break

            

    print(safe_count)

