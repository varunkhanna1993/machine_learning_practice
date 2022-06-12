getbinary = lambda x, n: format(x, 'b').zfill(n)

def flipping_bits(n):
    return 4294967295 - n
    
my_arr = 1


print(flipping_bits(my_arr))
