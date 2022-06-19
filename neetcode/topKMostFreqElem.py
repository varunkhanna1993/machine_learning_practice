class Solution:
    def topKFrequent(self, nums, k: int):
        # my_hash = {}
        # for i in nums:
        #     my_hash[i] = 1+ my_hash.get(i, 0)
        # list_ = {k: v for k, v in sorted(my_hash.items(), key=lambda item: item[1], reverse = True)[:k]}
        
        # # for i in range(len(list_)):
        # #     res.append(list_[i][0])


        # return list(list_.keys())

        #another solution
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1+count.get(i,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for c in range(len(freq)-1, 0,-1):
            for n in freq[c]:
               res.append(n)
               if len(res) == k:
                return res 
        return freq


# my_nums = [-1,-1] # k = 2
my_nums = [4,1,-1,2,-1,2,3]

print(Solution().topKFrequent(nums = my_nums, k = 2))
        