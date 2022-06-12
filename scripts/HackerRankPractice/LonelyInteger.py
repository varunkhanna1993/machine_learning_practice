my_list = [1,1,2,4,2,3,3]

# print(list(mydict.keys())[list(mydict.values()).index(16)])  # Prints george

#or
def lonelyinteger(a):
    my_hash = {}
    for i in a:
        my_hash[i] = 1+my_hash.get(i, 0)
    for k,v in my_hash.items():
        if v == 1:
            return k
# Write your code here
print(lonelyinteger(my_list))