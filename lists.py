__author__ = 'ymarchanka'

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 3, 4, 5]
list4 = [1, 2, 3, 4, 5, 6]
list5 = [1, 2, 3]
list6 = [1, 2, 3, 4]


def compare(*args):
    i = 0
    while i < (len(args)-1):
        if args[0] != args[i+1]:
            print "compare", args[0], "and", args[i+1], "False"
        else:
            print "True"
        # print args[i]
        i += 1



    # for ind, lst in enumerate(args):
    #     print ind, lst
    # print

compare(list1, list2, list3, list4, list5, list6)