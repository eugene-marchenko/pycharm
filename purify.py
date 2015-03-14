def purify(numbers):

    new_list = [i for i in numbers if i % 2 == 0]
    return new_list


print purify([1,2,3,4,5,6,7,8])