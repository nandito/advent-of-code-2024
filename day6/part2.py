import logging
import numpy as np

directions = [(-1, 0), (0, 1), (1, 0), (0, -1) ]

path = []
def walk_maze(maze, start, directionIdx, step_count):
    if len(path) > 19:
        print(maze)
        return
    logging.debug("PATH: " + str(path))
    row, col = start
    is_end = False
    is_loop = False
    direction = directions[directionIdx]
    next_position = maze[row + direction[0], col + direction[1]]
    while is_end is False:
        while next_position != "#" and next_position != "O":
            row += direction[0]
            col += direction[1]
            maze[row, col] = "X"
            next_row = row + direction[0]
            next_col = col + direction[1]

            if (next_row, next_col) in path:
                logging.debug("LOOP: " + str(path) + "\nrow,col: " + str((row,col)) + "\n-2: " + str(path[-2]) if len(path) > 1 else "")
                next_pos_index = path.index((next_row, next_col))
                logging.debug("next_pos_index: " + str(next_pos_index) + "path[next_pos_index-1]: " + str(path[next_pos_index-1]))
                if len(path) > 1 and (row, col) == path[next_pos_index-1]:
                    is_loop = True
                    break
            path.append((next_row, next_col))

            logging.debug("next_row: " + str(next_row) + " next_col: " + str(next_col))
            if next_row < 0 or next_row >= maze.shape[0] or next_col < 0 or next_col >= maze.shape[1]:
                logging.debug("next_row: " + str(next_row) + " next_col: " + str(next_col) + " is out of bounds")
                is_end = True
                break
            next_position = maze[next_row, next_col]
            # logging.debug("PATH: " + str(path))
            step_count += 1

            # if (next_row, next_col) in path:
            #     # (row, col) == path[-2]
            #     is_loop = True
            #     break
        next_direction_index = (directionIdx + 1) % 4
        logging.debug("step_count: " + str(step_count) + " row: " + str(row) + " col: " + str(col) + " next_direction_index: " + str(next_direction_index))
        if is_end is True:
            break
        if is_loop is True:
            break
        step_count, (row, col), is_end, maze = walk_maze(maze, (row, col), next_direction_index, step_count)
    return step_count, (row, col), is_end, maze

def solve_part2(lines):
    maze = np.array([list(line.strip()) for line in lines])
    logging.debug("maze:\n" + str(maze))

    start = np.where(maze == "^")
    logging.debug("start: " + str(start))

    step_count, position, is_end, updated_maze = walk_maze(maze, start,0, step_count=0)
    logging.debug("updated_maze:\n" + str(updated_maze))
    x_count = np.count_nonzero(updated_maze == "X")
    logging.debug("step_count: " + str(step_count))
    print(x_count)
