def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)

    #how to sum the first quadrant? if its 4*4 then top 2*2 if its 2*2 then 1*1
    q = int(n/2)
    print(q, n//2)
    sum_ = 0
    for i in range(n//2):
        for j in range(n//2):
            sum_+= max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    # how to maximize this sum by only flipping rows or columns 
    return sum_
    
    
    # print(sum_)


matrix = [[112, 42, 83, 119], 
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]]

# matrix = [[1,2],[3,4]]
print(len(matrix))

print(flippingMatrix(matrix))

# max of r0c0, r0c3, r3,c0, r3,c3
#max of r0c1,roc2,r3c1,r3c1
#max of r1c1,r1c2,r2c2,r2c3
# max of r1c0,r2c0,r1c3, r2c3