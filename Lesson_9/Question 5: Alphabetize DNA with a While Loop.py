# 5. Alphabetize DNA with a While Loop
#
# We will test your code with the following commands:
#
# python studentcode.py A a t C g AA gG c AG T TA a G aaaa
# python studentcode.py c AAaattTTccCCggGGaAcCtTgG g
#
# The expected output from your program is:
#
# ['A', 'A', 'A', 'AA', 'AAAA', 'AG', 'C', 'C', 'G', 'G', 'GG', 'T', 'T', 'TA']
# ['AAAATTTTCCCCGGGGAACCTTGG', 'C', 'G']

#! /usr/bin/env python3

import sys
system_seqs = sys.argv[1:]
# seq = input("Input : ")

sequences_index = 0
sequences = []
while sequences_index < len(system_seqs):
    sequences.append(system_seqs[sequences_index])
    sequences_index += 1
# print('sequences = ' + str(sequences))

sequences_upper = []
index = 0
while index < len(sequences):
    sequences[index] = sequences[index].replace('a', 'A')
    sequences[index] = sequences[index].replace('g', 'G')
    sequences[index] = sequences[index].replace('c', 'C')
    sequences[index] = sequences[index].replace('t', 'T')
    sequences_upper.append(sequences[index])
    index += 1
sequences_upper.sort()
print(str(sequences_upper))