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

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float('infinity')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c, 0)

            
            if c in countT and window[c] == countT[c]:
                have +=1

            while have == need:
                #update the result
                if (r -l +1) < reslen: 
                    res = [l,r]
                    reslen = (r-l+1)

                # pop from the left
                window[s[l]] -=1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1 
                l+= 1

        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""



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