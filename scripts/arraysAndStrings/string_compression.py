class Solution:
    def compress(self, chars) -> int:
        my_chars = {}
        my_list = []
        for i in chars:
            my_chars[i] = 1 + my_chars.get(i,0)
            
        for keys, values in my_chars.items():
            my_list.append(keys)
            if values >= 10:
                temp = [a for a in str(values)]
                for i in temp:
                    my_list.append(i)
            else:
                my_list.append(values)
            
        return my_list
test_a = ["a","a","b","b","c","c","c", "a", "a"]
test_b = ["a"]
chars = ["a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(Solution().compress(chars = test_a))


# print([a for a in str(1345)])
