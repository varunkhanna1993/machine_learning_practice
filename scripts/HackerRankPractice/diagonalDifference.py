
my_matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifferences(matrix):
    left_right = 0
    right_left = 0   
    l, r = 0, len(my_matrix) -1
    while l< len(my_matrix):
            right_left += my_matrix[l][r]
            left_right += my_matrix[l][l]
            l+=1
            r-=1
    return abs(right_left - left_right)

print(diagonalDifferences(my_matrix))
# print(range(len(my_matrix)-1))