def two_sum_ii(nums, target):
    # this function assumes that the list is sorted
    low, high = 0, len(nums)-1
    while low < high:
        # adding nums in first index and then the last index
        num = nums[low] + nums[high]
        #returns index if found a match
        if num == target:
            return (low+1, high+1)
        # if the value to find i.e. num is less than target then we move one step forward
        elif num < target:
            low += 1
        # if the num value is greater than the target then we move one step backward in the last index
        else:
            high -= 1
    return False
    
    
nums = [99,2,7,11,15]
nums.sort()
print(nums)
print(two_sum_ii(nums = nums,target= 6))