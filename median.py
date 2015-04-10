def median(numbers):
    numbers.sort()
    print numbers
    count = len(numbers)
    #print count
    if count % 2 != 0:
        return numbers[count/2]
    else:
        return (numbers[count/2] + numbers[count/2 - 1])/2.0




print median([5,1,7,3])