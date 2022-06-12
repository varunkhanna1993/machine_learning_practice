
def matchingStrings(strings, queries):
    my_hash = {}
    res = []
    for i in strings:
        my_hash[i] = 1+my_hash.get(i,0)
    for j in queries:
        if j in my_hash.keys():
            res.append(my_hash[j])
        else:
            res.append(0)
    return res

my_strings = ['ab','ab','abc']
my_query = ['ab','abc', 'bc']

print(matchingStrings(strings = my_strings, queries= my_query))