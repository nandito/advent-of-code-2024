import numpy as np

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
    
    xmas_counter = 0

    # print(word_matrix)
    
    for i in range(len(word_matrix)):
        for j in range(len(word_matrix[i])):
            if word_matrix[i][j] == 'X':
                # print("X found at", i, j)
                horizontal_right_by_four = word_matrix[i, j:j+4]
                if "".join(horizontal_right_by_four) == "XMAS":
                    # print("Found XMAS in horizontal right")
                    xmas_counter += 1

                horizontal_left_by_four = word_matrix[i, j:j-4:-1]
                if "".join(horizontal_left_by_four) == "XMAS":
                    # print("Found XMAS in horizontal left")
                    xmas_counter += 1

                vertical_down_by_four = word_matrix[i:i+4, j]
                if "".join(vertical_down_by_four) == "XMAS":
                    # print("Found XMAS in vertical down")

                    xmas_counter += 1
                vertical_up_by_four = word_matrix[i:i-4:-1, j]
                if "".join(vertical_up_by_four) == "XMAS":
                    # print("Found XMAS in vertical up")
                    xmas_counter += 1

                diagonals = get_diagonals(word_matrix, i, j)
                if "".join(diagonals["top_left"]) == "XMAS":
                    # print("Found XMAS in top left diagonal")
                    xmas_counter += 1
                if "".join(diagonals["top_right"]) == "XMAS":
                    # print("Found XMAS in top right diagonal")
                    xmas_counter += 1
                if "".join(diagonals["bottom_left"]) == "XMAS":
                    # print("Found XMAS in bottom left diagonal")
                    xmas_counter += 1
                if "".join(diagonals["bottom_right"]) == "XMAS":
                    # print("Found XMAS in bottom right diagonal")
                    xmas_counter += 1

    print(xmas_counter)

