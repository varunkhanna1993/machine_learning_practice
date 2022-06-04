"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""




class Solution:
    def threeSum(self, nums):
        # for the result
        res = []
        # sort the input array 
        nums.sort()
        for index, value in enumerate(nums):
            if value > 0 and value == nums[index -1]:
                continue
            if index == 0 or nums[index - 1] != nums[index]:
                l,r = index+1, len(nums)-1
                while l < r:
                    threeSum = nums[l] +nums[r]+nums[index]
                    if threeSum > 0:
                        r-=1
                    elif threeSum < 0:
                        l+=1
                    else:
                        res.append([nums[index], nums[l], nums[r]])
                        l+= 1
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
        return res



if __name__ == '__main__':
    a = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(a.threeSum(nums))