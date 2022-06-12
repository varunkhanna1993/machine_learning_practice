
def vector_compres(arr):
    my_list = []
    l,r = 0,1
    count = 1
    if len(arr) == 1:
        my_list.append(arr[l])
        my_list.append(count)
        return my_list 

    while l < len(arr) -1:
        if r==len(arr):
            my_list.append(arr[l])
            my_list.append(count)
            # count +=1
            l = r
            r+=1
        elif arr[l] != arr[r]:
            my_list.append(arr[l])
            my_list.append(count)
            count = 1
            l = r
            r+=1
        else:
            count+=1
            r +=1
        
    return my_list

# my_arr = [1,1,1,1,5,5,2,2,3,3,9,9,2,2,2,2]
my_arr = [1,1,1]
# print(len(my_arr))
print(vector_compres(my_arr))
#expected output = [1,3,5,2,3,3,9,1,3,5]