import numpy as np
import logging

def get_diagonals(array, row, col, max_steps=4):
    nrows, ncols = array.shape
    
    # Helper function to extract diagonals
    def extract_diagonal(r_step, c_step):
        diagonal = []
        for step in range(0, max_steps):
            new_row, new_col = row + step * r_step, col + step * c_step
            if 0 <= new_row < nrows and 0 <= new_col < ncols:
                diagonal.append(array[new_row, new_col])
            else:
                break
        return diagonal
    
    # Get diagonals in four directions
    top_left = extract_diagonal(-1, -1)  # Up-left
    top_right = extract_diagonal(-1, 1)  # Up-right
    bottom_left = extract_diagonal(1, -1)  # Down-left
    bottom_right = extract_diagonal(1, 1)  # Down-right

    return {
        "top_left": top_left,
        "top_right": top_right,
        "bottom_left": bottom_left,
        "bottom_right": bottom_right
    }

def solve_part1(lines):
    word_matrix = np.array([list(line.strip()) for line in lines])

    logging.debug(word_matrix)
    
    xmas_counter = 0
    
    logging.debug("Rows")
    for row in word_matrix:
        logging.debug("".join(row) + " " + str("".join(row).count("XMAS")))
        xmas_counter += "".join(row).count("XMAS")

    logging.debug("Fliplr")
    for row in np.fliplr(word_matrix):
        logging.debug("".join(row) + " " + str("".join(row).count("XMAS")))
        xmas_counter += "".join(row).count("XMAS")
    
    logging.debug("Transpose")
    for col in word_matrix.T:
        logging.debug("".join(col) + " " + str("".join(col).count("XMAS")))
        xmas_counter += "".join(col).count("XMAS")

    logging.debug("Fliplr transpose")
    for col in np.fliplr(word_matrix.T):
        logging.debug("".join(col) + " " + str("".join(col).count("XMAS")))
        xmas_counter += "".join(col).count("XMAS")

    logging.debug("Diagonals")
    for row in range(word_matrix.shape[0]):
        for col in range(word_matrix.shape[1]):
            diagonals = get_diagonals(word_matrix, row, col)
            for diagonal in diagonals.values():
                logging.debug("".join(diagonal) + " " + str("".join(diagonal).count("XMAS")))
                xmas_counter += "".join(diagonal).count("XMAS")

    print(xmas_counter)
