"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
"""Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]"""

from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs):
        result = defaultdict(list)
        print(result)
        for s in strs:
            count =[0]*26
            for c in s:
                count[ord(c)-ord("a")] +=1
        
            result[tuple(count)].append(s)
        return result.values()
            # while right < len(strs) -1:
            #     right+=1
        
        # pass

strs = ["eat","tea","tan","ate","nat","bat"]
# print(len(strs))
print(Solution().groupAnagrams(strs))
# print(ord('z')-ord('a'))
"""
for loop for the left pointer
    empty list and put word where left pointer is pointing --> list1 
    create empty dictionary and put in all chars where the left pointer is pointing in a dictionary
or while right pointer has not reach end of list
right pointer +1
loop through the chars of the right pointer 
if right > len(strs) -1:
    append list1 to result
elif
the character not in dictionary right +1 and break
else if all the characters present 
append the word at to the list1
right+1
"""
        