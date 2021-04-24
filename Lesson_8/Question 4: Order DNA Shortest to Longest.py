#!/usr/bin/env python3

import sys

var1 = sys.argv[1]
var2 = sys.argv[2]
var3 = sys.argv[3]

var1L = len(var1)
var2L = len(var2)
var3L = len(var3)


if var1L < var2L < var3L:
	print(var1 + "," + var2 + "," + var3)

elif var1L < var3L < var2L:
	print(var1 + "," + var3 + "," + var2)

elif var2L < var1L < var3L:
	print(var2 + "," + var1 + "," + var3)

elif var2L < var3L < var1L:
	print(var2 + "," + var3 + "," + var1)

elif var3L < var1L < var2L:
	print(var3 + "," + var1 + "," + var2)

elif var3L < var2L < var1L:
	print(var3 + "," + var2 + "," + var1)
