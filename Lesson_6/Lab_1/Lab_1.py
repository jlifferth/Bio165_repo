#!/usr/bin/env python3

import sys

seq1 = sys.argv[1]
seq2 = sys.argv[2]
seq3 = sys.argv[3]

# 1 validate user input
# return error message if any seq is only whitespace

seq1_replace = seq1.replace(' ', '')
seq2_replace = seq2.replace(' ', '')
seq3_replace = seq3.replace(' ', '')

if seq1 == '' or seq1_replace == '':
    print("ERROR: You must enter a DNA sequence")
    sys.exit()

elif seq2 == '' or seq2_replace == '':
    print("ERROR: You must enter a DNA sequence")
    sys.exit()

elif seq3 == '' or seq3_replace == '':
    print("ERROR: You must enter a DNA sequence")
    sys.exit()

# return error message if invalid characters present
allowed_chars = 'AGCTagct /t'

for seq in (seq1, seq2, seq3):
    for char in seq:
        if char not in allowed_chars:
            print("ERROR: Invalid DNA sequence")
            sys.exit()


# 2 Calculate and display the length of each sequence

seq1L = len(seq1) - seq1.count(" ")
seq2L = len(seq2) - seq2.count(" ")
seq3L = len(seq3) - seq3.count(" ")

print("Sequence 1: " + str(seq1L))
print("Sequence 2: " + str(seq2L))
print("Sequence 3: " + str(seq3L))

# 3 Concatenate sequences

seq123 = seq1 + seq2 + seq3

seq123a = seq123.replace(" ", "")

print(seq123a)

# 4 Calculate GC content

seq123a_length = len(seq123a)

seq123a_lower = seq123a.lower()

g_count = seq123a_lower.count("g")
c_count = seq123a_lower.count("c")

gc_count = g_count + c_count

gc_percentage = (gc_count / seq123a_length) * 100

print(gc_percentage)