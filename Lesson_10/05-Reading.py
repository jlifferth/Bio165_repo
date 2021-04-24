#! /usr/bin/env python3

import sys

file_path = str(sys.argv[1])

with open(file_path) as my_file:
    in_file_variants = []
    for line in my_file:
        if line[0] == '#': # all lines beginning with # are meta-data lines or header, these should be printed
            print(line.strip(), end= '\n')
        if line[0] != '#': # all lines without # are variant lines, these are the lines that should be searched
            in_file_variants.append(line)
    for variant_line in in_file_variants:
        fields = variant_line.split('\t')
        if len(fields) >= 7:
            if 'PASS' in fields[6]:
                print(variant_line.strip(), end= '\n')