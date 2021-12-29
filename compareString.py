import math
import os
import random
import re
import sys

#complete twoStrings function
#the expected function to return a STRING
# parameters STRING s1 and STRING s2

def twoStrings(s1, s2):
    #Returns either YES or NO
    # constraints s1 and s2 consist of characters in the range of ASCII
    # constraints 1 <= p <= 10
    # constraints 1 <= |s1|, |s2| <= 10^5
    return 'YES' if set(s1) & set(s2) else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())

for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1, s2)
    fptr.write(result + '\n')
fptr.close()
