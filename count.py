def count(sequence, item):
    # print sequence
    # print item
    # print sequence.count(item)

    counts = 0
    new_string = ''

    for i in sequence:
        # print i
        # print y
        new_string = new_string + str(i)
        # print sequence[i]
        # if i == item:
        #    counts += 1
        if item == i:
            counts += 1
    return counts


print(count([4, 2, 1, 1, 1, 1, 1], 1))
