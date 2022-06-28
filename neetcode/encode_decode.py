def encode(s):
    res = ''
    for i in range(len(s)):
        res += str(len(s[i]))+'#'+s[i]
    return res

def decode(s):
    res, i = [], 0

    while i < len(s):
        j = i
        while s[j]!= '#':
            j+=1
        length = int(s[i:j])

        res.append(s[j+1: j+1+length])
        i= j+1+length


    # for i in range(len(s)):
    #     if s[i].isdigit():
    #         res.append(s[i+1+1: i+1+1+int(s[i])])

    return res

l1 = ["0"]

encoded_str = encode(l1)

print(decode(encoded_str))

