"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
Eg
Input: matrix = [[1,2], [4,5]]
Ouput: [[5,1], [4,2]]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""


"""
So basically the first output of each list starting from right most list becomes the first element in the new list
then the first element in the next list becomes the second and so on.

but we need to modify it in place. how do we do that?

"""
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix) - 1

        while l< r:
            for i in range(r-l):
                top, bottom = l, r

                # save the top left value 
                topLeft = matrix[top][l+i]

                # move bottom left into top left
                matrix[top][l+i] = matrix[bottom-i][l]

                # move bottom right into bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # move top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #move the top left into top right
                matrix[top+i][r] =topLeft

            l+=1
            r-=1
            
        return my_matrix



my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotate(my_matrix))