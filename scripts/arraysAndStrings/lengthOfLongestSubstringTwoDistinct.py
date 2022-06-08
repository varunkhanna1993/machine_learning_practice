class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
                
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = {}

        max_len = 0

        while right < n:
            # when the slidewindow contains less than 3 characters
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1
            
            if right - left > max_len:
                max_len = right - left 
            # max_len = max(max_len, right - left)

        return max_len      

        # my_hash = {}
        # left = 0
        # while left < len(s)-1:
            
        #     if len(my_hash) <= 2:
        #         left +=1
        #         my_hash[s[left]] = 1+my_hash.get(s[left], 0)
        #     # elif left == len(s)-1:
        #     #     return left
        #     else:
        #         my_hash = {}
        #         left+=1
        # return sum(my_hash.values())


s = "ccaabbbdddd"
# s = "eceba"
print(Solution().lengthOfLongestSubstringTwoDistinct(s))