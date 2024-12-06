import logging
import numpy as np

directions = [(-1, 0), (0, 1), (1, 0), (0, -1) ]

def walk_maze(maze, start, directionIdx, step_count):
    row, col = start
    is_end = False
    direction = directions[directionIdx]
    next_position = maze[row + direction[0], col + direction[1]]
    while is_end is False:
        while next_position != "#":
            row += direction[0]
            col += direction[1]
            maze[row, col] = "X"
            next_row = row + direction[0]
            next_col = col + direction[1]
            logging.debug("next_row: " + str(next_row) + " next_col: " + str(next_col))
            if next_row < 0 or next_row >= maze.shape[0] or next_col < 0 or next_col >= maze.shape[1]:
                logging.debug("next_row: " + str(next_row) + " next_col: " + str(next_col) + " is out of bounds")
                is_end = True
                break
            next_position = maze[next_row, next_col]
            step_count += 1
        next_direction_index = (directionIdx + 1) % 4
        logging.debug("step_count: " + str(step_count) + " row: " + str(row) + " col: " + str(col) + " next_direction_index: " + str(next_direction_index))
        if is_end is True:
            break
        step_count, (row, col), is_end, maze = walk_maze(maze, (row, col), next_direction_index, step_count)
    return step_count, (row, col), is_end, maze

def solve_part1(lines):
    maze = np.array([list(line.strip()) for line in lines])
    logging.debug("maze:\n" + str(maze))

    start = np.where(maze == "^")
    logging.debug("start: " + str(start))

    step_count, position, is_end, updated_maze = walk_maze(maze, start,0, step_count=0)
    logging.debug("updated_maze:\n" + str(updated_maze))
    x_count = np.count_nonzero(updated_maze == "X")
    logging.debug("step_count: " + str(step_count))
    print(x_count)
