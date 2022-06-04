class Solution:
    # nums = [1,2,7,9,8,4,1]
    # out -> [1,2,8,1,4,7,9]
    
    # find pivot
    # reverse
    # swap with the next greatest number
    
    def swap(self, nums, ind1, ind2):
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
    
    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg+=1
            end-=1
            
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)== 1:
            return
        if len(nums) ==2:
            return self.swap(nums, 0, 1)
        dec = len(nums)-2
        while dec >= 0 and nums[dec] >= nums[dec+1]:
            dec-=1
        self.reverse(nums, dec+1, len(nums)-1)
        # print(nums)
        if dec == -1:
            return
        next_num = dec+1
        print(nums)
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num+=1
        # print(next_num)
        self.swap(nums, next_num, dec)
        print(nums)

        

my_list = [1,2,3]

Solution().nextPermutation(nums = my_list)
        