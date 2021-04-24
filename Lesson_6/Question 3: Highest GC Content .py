#!/usr/bin/env python3

import sys

code1 = sys.argv[1]
code2 = sys.argv[2]
code3 = sys.argv[3]

GC_code1 = code1.count("GC")
GC_code2 = code2.count("GC")
GC_code3 = code3.count("GC")

if GC_code1 > GC_code2 and GC_code1 > GC_code3:
	print(code1 + " has the highest GC content.")

elif GC_code2 > GC_code1 and GC_code2 > GC_code3:
	print(code2 + " has the highest GC content.")

elif GC_code3 > GC_code2 and GC_code3 > GC_code1:
	print(code3 + " has the highest GC content.")


