"""
S;V;iPad
C;M;mouse pad
C;C;code swarm
S;C;OrangeHighlighter
"""
import re

# from numpy import dtype
my_str ='S;V;iPad'
if my_str.split(";")[0] == "S":
    print(True)
    temp = my_str.split(";")[2]

# print(temp)
# for i in my_str.split(';')[2]:
#     print(i)
# print(re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', ))
print(type(temp))
