import numpy as np
from io import StringIO

import re

def solve_part2(line):
    line_read = line.read()
    line_read = line_read.replace("\n", "")
    inner_blocks_regex = r"don't\(\).*?do\(\)"
    cleaned_line = re.sub(inner_blocks_regex, "", line_read)
    last_blocks_regex = r"don't\(\).*"
    cleaned_line = re.sub(last_blocks_regex, "", cleaned_line)
    parsed_nums = np.fromregex(StringIO(cleaned_line), r"mul\((\d+),(\d+)\)", [('a', int), ('b', int)]) 
    prods = parsed_nums['a'] * parsed_nums['b']
    print(prods.sum())
