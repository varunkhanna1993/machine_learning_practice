

my_list = [1, 0, 40, 13, 55, 93, 54, 87, 65, 35, 22, 1, 14, 86,
            20, 79, 66, 56, 18, 52, 75, 63, 74, 80, 23, 49, 
            76, 28, 84, 78, 45, 24, 59, 27, 1, 12, 95, 82,
            91, 33, 9, 89, 50, 60, 51, 70, 92, 94, 58, 11,
            42, 88, 99, 7, 46, 57, 40, 98, 96, 32, 34, 77, 8, 
            31, 29, 21, 99, 99, 38, 85, 25, 71, 3, 62, 5, 67, 
            43, 44, 6, 17, 81, 68, 30, 53, 41, 10, 15, 16, 2, 
            73, 61, 90, 64, 72, 39, 48, 83, 19, 26, 4]
# my_list = [55,23,53,21,78,1,6,4]
print(len(my_list))
def countingSort(arr):
    # Write your code here
    my_list = []
    frequency = [0]* (max(arr)+1)
    for i in arr:
        frequency[i]+=1

    for i in range(len(frequency)):
        if frequency[i]!= 0:
            my_list.append(i)
        

    return frequency
print(countingSort(my_list))