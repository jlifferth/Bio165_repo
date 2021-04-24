#! /usr/bin/env python3

import sys

seq1 = sys.argv[1]
seq2 = sys.argv[2]
seq3 = sys.argv[3]

#remove spaces

seq1 = seq1.replace(" ","")
seq2 = seq2.replace(" ","")
seq3 = seq3.replace(" ","")

seq1 = seq1.upper()
seq2 = seq2.upper()
seq3 = seq3.upper()

list_1 = [seq1, seq2, seq3]

list_1.sort()

print(list_1)

#print(seq1, seq2, seq3)
