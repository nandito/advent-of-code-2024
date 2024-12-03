import numpy as np
def solve_part1(lines):
    
    parsed_nums = np.fromregex(lines, r"mul\((\d+),(\d+)\)", [('a', int), ('b', int)]) 
    prods = parsed_nums['a'] * parsed_nums['b']
    print(prods.sum())
