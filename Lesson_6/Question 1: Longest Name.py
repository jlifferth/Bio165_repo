#!/usr/bin/env python3

import sys

First = sys.argv[1]
Last = sys.argv[2]

len_First = len(First)
len_Last = len(Last)

if len_First > len_Last:
    print(First + " is longer than " + Last + ".")

elif len_First == len_Last:
    print(First + " is the same length as " + Last + ".")

else:
    print(Last + " is longer than " + First + ".")
