#! /usr/bin/env python3

import sys

seq = sys.argv[1]
pos = sys.argv[2]

seq = seq.upper()

exon1_end = int(pos[0])
exon2_start = int(pos[2]) - 1

intron = seq[exon1_end:exon2_start]

exon1_exon2 = seq[:exon1_end] + seq[exon2_start:]

print(exon1_exon2)




#print(intron)

#print(exon1_end, exon2_start)


