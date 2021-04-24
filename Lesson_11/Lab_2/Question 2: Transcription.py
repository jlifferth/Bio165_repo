#! /usr/bin/env python3

import sys
import re

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

with open(input_file_name) as input_file, open(output_file_name, 'w') as output_file:
    for line in input_file:
        if line[0] == '>':
            output_file.write(line)
        else:
            line = line.upper()
            search = 'T'
            replace = 'U'
            rna = re.sub(search, replace, line)
            output_file.write(rna)
sys.exit()
