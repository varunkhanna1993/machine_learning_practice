

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 38 or 5-grades[i]%5 > 2:
            pass
        else:
            grades[i]=  grades[i]+5-grades[i]%5
    return grades




grades = [2,37,38] #85
# 57 > do not round 
# 29 less than 40 so do not round 
print(gradingStudents(grades = grades ))