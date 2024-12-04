import argparse

from part1 import solve_part1
# from part2 import solve_part2

parser = argparse.ArgumentParser(
    description="Advent of Code 2024 - Day 4",
    epilog="https://adventofcode.com/2024/day/4",
)
parser.add_argument(
    "-i",
    "--input_file",
    metavar="FILE",
    type=str,
    help="The input file containing the puzzle input",
    required=True,
)
parser.add_argument(
    "-p",
    "--part",
    choices=["1", "2"],
    help="The part of the puzzle to solve",
    required=True,
)

args = parser.parse_args()

with open(args.input_file) as f:
    if args.part == "1":
        solve_part1(f)
    # elif args.part == "2":
    #     solve_part2(f)
    else:
        print("Invalid part specified")
        exit(1)
