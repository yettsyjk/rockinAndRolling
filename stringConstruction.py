import math
import os
import random
import re
import sys

# Amanda has a string of lowercase letters that she wants to copy to new string
# function is expected to return an INTEGER
# function accepts STRINGs as a parameter
# input: 2 input: abcd input: abab
def stringConstruction(s):
    return len(set(s))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)

        fptr.write(str(result) + '\n')
    fptr.close()
