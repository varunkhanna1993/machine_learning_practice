
# import math
# import os
# import random
# import re
# import sys



def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    min_sum = sum(arr[:n-1])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)
    # print(resMax, resMin)

test_case = [1,3,5,7,9]
test_case1 = [1,1,1,1,1]



# arr = list(map(int, input().rstrip().split()))

miniMaxSum(test_case)  
# if __name__ == '__main__':
#     test_case = [1,3,5,7,9]



#     # arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(test_case)
