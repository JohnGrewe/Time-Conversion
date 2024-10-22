#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    military_time = ""
    if s[-2:] == "PM":
        if s[:2] == "12":
            military_time = s[:-2]
        else:
            military_time = str(int(s[:2])+12) + s[2:-2]
    elif s[-2:] == "AM":
        if s[:2] == "12":
            military_time = "00" + s[2:-2]
        else: military_time = s[:-2]
    return military_time

    # Write your code here
    

if __name__ == '__main__':
    output_path = 'YOUR_OUTPUT_PATH'
    #fptr = open(output_path, 'w')
    with open(output_path, 'w') as fptr:

        s = input()

        result = timeConversion(s)

        fptr.write(result + '\n')

        #fptr.close()
