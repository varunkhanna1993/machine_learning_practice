
def loo_cv(arr):
    score =0
    sum_ = 0
    mean_arr = [sum(arr)/len(arr)]*(len(arr)-1)

    for i in range(len(arr)):
        drop_one = arr[:i] + arr[i+1:]
        print(drop_one)
        # mean_drop_one = [sum(drop_one)/len(drop_one)]* len(drop_one)
        # print(mean_drop_one)
        for j in range(len(drop_one)):
            sum_ += abs(drop_one[j] - mean_arr[j])
        print(sum_)
        # print(sum_, len(drop_one))
        score += (sum_)
        
        # print(score)
    print(score/len(arr))

my_arr = [1,2,3]
# expected output = 1.0
loo_cv(my_arr)

# from random import seed
# from random import randrange
 
# # Split a dataset into k folds
# def cross_validation_split(dataset, folds=3):
# 	dataset_split = list()
# 	dataset_copy = list(dataset)
# 	fold_size = int(len(dataset) / folds)
# 	for i in range(folds):
# 		fold = list()
# 		while len(fold) < fold_size:
# 			index = randrange(len(dataset_copy))
# 			fold.append(dataset_copy.pop(index))
# 		dataset_split.append(fold)
# 	return dataset_split
 
# # test cross validation split
# seed(1)
# dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# folds = cross_validation_split(dataset, 4)
# print(folds)