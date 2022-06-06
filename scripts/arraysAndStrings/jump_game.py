class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums) -1
        for i in range(len(nums) -1, -1,-1):
            print(nums[i]+ i)
            if i +nums[i] >= goal:
                goal = i

        return True if goal == 0 else False



my_nums  =[2,3,1,1,4]
print(Solution().canJump(nums= my_nums))

# print(my_nums[0])