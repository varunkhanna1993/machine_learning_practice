"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

class Solution:
    def threeSum(self, nums):
        triplets = []
        for object_i in range(len(nums)):
            for object_j in range(len(nums)):
                for object_k in range(len(nums)):
                    if object_i != object_j and object_j != object_k and object_i != object_k and ((nums[object_i]+ nums[object_j] + nums[object_k] ) == 0):
                        triplets.append([object_i, object_j, object_k])
        triplets = set([tuple(i) for i in triplets])


        return list(triplets)


if __name__ == '__main__':
    a = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(a.threeSum(nums))