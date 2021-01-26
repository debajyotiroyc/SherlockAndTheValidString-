#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    d = dict()
    d = Counter(s)
    t = tuple(d.values())
    l = len(t)
    m1 = min(t)
    m2 = max(t)
    c1 = t.count(m1)
    c2 = t.count(m2)
    if c1 == l:
        return "YES"
    elif c1 == l - 1:

        if (m2 - m1) > 1:
            return "NO"
        else:
            return "YES"
    else:
        if c1 == 1 and c2 == l - 1:
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
