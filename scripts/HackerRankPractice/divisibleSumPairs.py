
import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#
"""
Given an array of integers and a positive integer , 
determine the number of  pairs where  i < j and ar[i]  and ar[j]  +  is 
divisible by k.
"""

def divisibleSumPairs(n, k, ar):
    my_list= []
    # Write your code here
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if i < j and (ar[i]+ar[j])%k == 0:
                my_list.append([ar[i], ar[j]])

    return len(my_list)

my_arr = [1, 3, 2, 6, 1, 2]
k =3 
print(divisibleSumPairs(6,k=k,ar=my_arr))