class Solution:
    # def minimum_substring(self, string_1, string_2) -> bool:
    #     s_len, t_len = len(string_1), len(string_2)
    #     min_substring_len = t_len # since we need all characters in t

    #     #sliding window in the string
    #     l, r = 0,min_substring_len

    #     if s_len < t_len:
    #         return ''
    #     while min_substring_len < len(s) - 1:
    #          #sliding window in the string
    #         l, r = 0,min_substring_len 
    #         substring = s[l:r] 
    #         if t in substring:
    #             return substring


    #     return s_len, t_len
    def minimum_substring(self, s, t) -> bool:
        if t == "":
            return ""
        countT, window = {}, {}
        
        #create a hash map of the values in t 
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        #to track how many you have got and how many you need
        have, need = 0, len(countT)
        
        #resulting l and right pointers to be updated and the reslen
        res, reslen = [-1,-1], float('infinity')
        
        # left pointer
        l = 0

        # run a for loop in the entire length of the string s 
        for r in range(len(s)):
            
            # first character in the string is put as c
            c = s[r]
            
            # add the character in the hash map for the window 
            window[c] = 1+ window.get(c, 0)

            # if the value is already what we need and the count is equal to in the window
            if c in countT and window[c] == countT[c]:
                have +=1 # then update what we have as 1
        return window, countT, have, need
        #     # till the time what we have and what we need are exactly equal
        #     while have == need:
        #         #update the result
        #         if (r -l +1) < reslen: 
        #             res = [l,r]
        #             reslen = (r-l+1)

        #         # pop from the left
        #         window[s[l]] -=1
                
        #         # check if the pop changed what we have, if actually then reduce what we have by 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -=1 
        #         # move the left pointer by 1 towards right so that we get the shortest string
        #         l+= 1

        # l, r = res
        # return s[l:r+1] if reslen != float("infinity") else ""



#input
s,t = "ADOBECODEBANC", "ABC"
"""
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""
print(Solution().minimum_substring(s,t))

# print(['A', "B", "C"] in ["B", "A", "C"])

# c = {"A": 1, "B": 12}

# # print(c.get("C",0))