"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""




class Solution:
    def threeSum_solution_two(self, nums):
        # for the result
        res = []
        # sort the input array 
        nums.sort()
        #    e.g. nums = [-4,-1,-1,0,1,2]
        for index, value in enumerate(nums):
            if value > 0 and value == nums[index -1]:
                continue
            if index == 0 or nums[index - 1] != nums[index]:
                seen = set()
                j = index + 1
                while j < len(nums):
                    complement = -(nums[index] +nums[j])
                    if complement in seen:
                        res.append([nums[index], nums[j], complement])
                        while j+1 < len(nums) and nums[j] == nums[j+1]:
                            j+=1
                    seen.add(nums[j])
                    print(seen)
                    j+=1
        return res
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
    nums = [-4,-1,-1,0,1,2]
    print(a.threeSum_solution_two(nums))