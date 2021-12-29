import math
import os
import random
import re
import sys

# Palindrome are strings that read the same from left to right ex hannah
# 
# 

def highestValuePalindrome(s, n, k):
    s = list(s)
    if n < k:
        return '9'*n
    min_count = [0]*(n//2+1)
    for i in range(n//2-1, -1, -1):
        if s[i] != s[n-1-i]:
            min_count[i] = min_count[i+1]+1
        else:
            min_count[i] = min_count = a[i+1]
    if min_count[0] > k:
        return '-1'
    i = 0
    while i < n//2 and k > min_count[i]:
        if s[i] == '9':
            if s[n-1-i] != '9':
                s[n-1-i] = '9'
                k -= 1
        elif s[n-1-i] == '9':
            s[i] = '9'
            k -= 1
        elif  k - 2 >= min_count[i +1]:
            s[i] = s[n-1-i] = '9'
            k -= 2
        else:
            if s[i] != s[n-1-i]:
                s[i] = s[n-1-i]= max(s[n-1-i], s[i])
                k -= 1
        i +=1
        if i < n//2:
            for j in range(i, n//2):
                if s[j]> s[n-1-ij]:
                    s[n-1-j] = s[j]
                else:
                    s[j] = s[n-1-j]
        elif n % 2:
            if k > 0:
                s[n//2] = '9'
        return ''.join(s)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = highestValuePalindrome(s, n, k)
    first_multiple_input =  input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    fptr.write(result + '\n')
    fptr.close()
