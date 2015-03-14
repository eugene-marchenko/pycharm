grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def grades_sum(scores):
    sum = 0
    for i in scores:
        sum = sum + i
    return sum

def grades_average(grades):
    return grades_sum(grades)/float(len(grades))


print grades_sum(grades)
print grades_average(grades)