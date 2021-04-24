# 3. Calculate the Length of a DNA Sequence
#
#
# We will test your code using the following commands:
#
# python studentcode.py ATATATATATATA
# python studentcode.py CGACGAGCAAAGCAAAAAGGGAAA
#
# Your code should produce the following output:
#
# 13
# 24

#! /usr/bin/env python3

import sys
seq = sys.argv[1]
# seq = input("Input : ")

index = 0
for nucleotide in seq:
    index += 1
print(index)