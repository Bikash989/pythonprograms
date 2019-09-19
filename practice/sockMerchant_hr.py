#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = dict()
    for val in ar:
        if val not in d:
            d[val] = 1
        else:
            d[val] = d[val]+1
    count = 0
    for val in d.items():   #val is tuple 
        count += val[1] // 2
    return count


if __name__ == '__main__':
    
    n = int(input())

    ar = list(map(int, input().rstrip().split()))
   
    result = sockMerchant(n, ar)
    print(result)
