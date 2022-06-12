
def marsExploration(s):
    # l, r = 0, 3
    count = 0
    correct = int(len(mars_message)/3)*"SOS"
    for i in range(len(s)):
        if s[i]!= correct[i]:
            count+=1

    return count

mars_message = 'SSSSSSSSSSSS'
print(marsExploration(mars_message))

# print(int(len(mars_message)/3)*"SOS")