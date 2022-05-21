# Area = length of shorter vertical line * distance between lines
"""
1. left pointer
2. right pointer
3. use fixed left pointer and shift right pointer by one index until it 
reaches the end of the list. 
4. set maxArea = 0 first 
5. then caculate currentArea = minimum of the height of two vertices * length of the x axis 
6. check if current area is > than maxArea 
7. update maxArea 
8. pass if current area is less than maxArea
9. when right pointer reaches end then shift left pointer one and then start with right
pointer again.
"""
def brute_force(height):

    maxArea = 0
    for left_pointer in range(len(height)):
        for right_pointer in range(left_pointer+1, len(height)):
                # print(height[object_i], height[right_pointer])
                width = right_pointer-left_pointer
                currentArea = min(height[left_pointer], height[right_pointer])*(width)
                # maxArea = max(maxArea,currentArea) or 
                if currentArea>maxArea:
                    maxArea = currentArea

    return maxArea

def time_complexity_n(height):
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea
height = [1,8,6,2,5,4,8,3,7]
if __name__ == '__main__':
    print(brute_force(height=height) == 49)
    print(time_complexity_n(height= height) == 49)
    # print([1][0]*2)





