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
            reverse_complement = ''
            line = line.strip()
            line = line.upper()
            index = len(line) - 1
            while index >= 0:
                if line[index] == 'A':
                    reverse_complement += 'T'
                elif line[index] == 'T':
                    reverse_complement += 'A'
                elif line[index] == 'C':
                    reverse_complement += 'G'
                elif line[index] == 'G':
                    reverse_complement += 'C'
                else:
                    pass
                index -= 1
            output_file.write(reverse_complement + '\n')
sys.exit()