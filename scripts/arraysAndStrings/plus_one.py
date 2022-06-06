from pandas import concat


class Solution:
    def plusOne_solution_two(self, digits) -> bool:
        for i in range(len(digits)- 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i]+=1
                return digits
        return [1] +digits


    def plusOne(self, digits) -> bool:
        my_string = ''
        for i in digits:
            my_string+=str(i)
        my_num = int(my_string)
        my_num+=1
        my_num = str(my_num)
        final_num = []
        for i in my_num:
            final_num.append(int(i))
        return final_num


my_nums  =[9,9,9,9,9]
print(Solution().plusOne_solution_two(digits= my_nums))
