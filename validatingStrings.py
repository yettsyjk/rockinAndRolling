import math
import os
import random
import re
import sys

# String considered valid if all characters of the string appear the same number of times
# valid if removing 1 character  at 1 index in the string 
# given string s, determine if it is validIfo so return YES otherwise retunr no

def isValid(s):
    # Returns expected STRING
    char_dict = {}
    # constraints 1<= |s| <= 10^5
    # create loop for how many times string happened
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    # constraints each character s[i] E ASCII[a-z]
    min_count = char_dict[char]
    max_count = char_dict[char]
    count_dict = {}
    # sample input aabbcd sample output  NO
    for char, value in char_dict.items():
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    # update max and min count
        if value < min_count:
            min_count = value
        if value > max_count:
            max_count = value
    if len(count_dict) == 1:
        return 'YES'
    elif len(count_dict) == 2:
        if count_dict[max_count] == 1 and max_count -min_count == 1:
            return 'YES'
        elif count_dict[min_count] == 1 and min_count == 1:
            return 'YES' 
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)

    fptr.write(result + '\n')
    fptr.close()
