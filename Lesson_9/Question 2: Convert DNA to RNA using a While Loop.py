# 2. Convert DNA to RNA using a While Loop
#

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
index = 0
while index < len(seq):
    if seq[index] in nucleotides:
        DNA += seq[index]
        index += 1
    else:
        index += 1

index_2 = 0
RNA = ""
while index_2 < len(DNA):
    if DNA[index_2] == "T":
        RNA += "U"
        index_2 += 1
    else:
        RNA += DNA[index_2]
        index_2 += 1
print(RNA)