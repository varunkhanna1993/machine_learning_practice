"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

"""Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
    # using hash maps 
    hash_map = {}

    for curr in range(len(nums)):
        value_to_find = target-nums[curr]
        if value_to_find not in hash_map:
            hash_map[nums[curr]] = curr
        else:
            return [nums.index(value_to_find), curr]


        # 
        # if value_to_find in nums and nums.index(value_to_find) != curr:
        #     return [curr, nums.index(value_to_find)]

        #solution through a while loop
        # while index < len(nums) -1:
        #     index +=1
        #     if value_to_find == nums[index]:
        #         result.append(x)
        #         result.append(index)

        #solution through double for loops
        # for j in range(x+1, len(nums)):
        #     if value_to_find == nums[j]:
        #         result.append(x)
        #         result.append(j)


nums = [3,2,4]
print(twoSum(nums, 6))