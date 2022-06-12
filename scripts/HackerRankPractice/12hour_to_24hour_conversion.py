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
    # Write your code here
    # print(s[-2::1])
    if s[-2::1] == 'PM' and s[0:2:1] != str(12):
        s = str(12+int(s[0:2:1])) + s[2:-2]
    elif s[-2::1] == 'PM' and s[0:2:1] == str(12):
        s = s[:-2]
    elif s[-2::1] == 'PM':
        s = str(12+int(s[0:2:1])) + s[2:-2]
    elif  s[-2::1] == 'AM' and s[0:2:1] == str(12):
        s = '00'+s[2:-2]
    else: 
        s = s[:-2]

    print(s)


test_cases = ["12:00:00PM", "12:00:00AM", "01:00:00PM","01:00:00AM"  ]

# print(test_cases[0][0:2:1])

timeConversion(test_cases[1])
# s = test_cases[0]

# if s[-2::1] == 'PM' and s[0:2:1] != str(12):
#     s = str(12+int(s[0:2:1])) + s[2:-2]
# elif s[-2::1] == 'PM' and s[0:2:1] == str(12):
#     print(s)
#     s = s[:-2]
# print(s)