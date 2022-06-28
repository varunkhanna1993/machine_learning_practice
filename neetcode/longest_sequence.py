def longestSequence(nums):
    numset = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in numset:
            length = 0
            while (n+length) in numset:
                length+=1
                longest = max(length, longest)

    return longest

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestSequence(nums))