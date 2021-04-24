# 1. Convert DNA to RNA using a For Loop
#

# We will test your code with the following commands:
#
# python studentcode.py "a t TT gG aT aa"
# python studentcode.py "cc cC tt TTt gaTc"
#
# The expected output from these commands is:
#
# AUUUGGAUAA
# CCCCUUUUUGAUC

#! /usr/bin/env python3

import sys
seq = sys.argv[1]
# seq = input("Input : ")
seq = seq.upper()
nucleotides = ['a','c','g','t','A','C','G','T']
DNA = ""
for element in seq:
    if element in nucleotides:
        DNA += element

RNA = ""
for nucleotide in DNA:
    if nucleotide == "T":
        RNA += "U"
    else:
        RNA += nucleotide
print(RNA)