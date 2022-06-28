class Solution:
    def productExceptSelf(self, nums):
        res = [1]*(len(nums))
        prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # print(prefix)
        postfix = 1
        for i in range(len(nums) -1 , -1 , -1):
            res[i]*=postfix
            postfix*=nums[i]
        # # print(postfix)
        
        return res
        

 
my_nums = [1,2,3,4]
# my_nums = [-1,1,0,-3,3]

print(Solution().productExceptSelf(nums = my_nums))       