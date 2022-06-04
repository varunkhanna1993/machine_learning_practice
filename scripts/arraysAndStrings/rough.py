my_list = [6,5,4,3,2,1]
beg = 0
end = len(my_list)
while beg < end:
    my_list[beg], my_list[end] = my_list[end], my_list[beg]
    beg+=1
    end-=1
print(my_list)

# print(my_list[end:beg:-1])