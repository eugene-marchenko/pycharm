def isPal(x):
    assert type(x) == list
    temp = x[:]
    temp.reverse()
    if temp == x:
        return True
    else:
        return False

def silly(n):
    assert type(n) == int and n > 0
    result = []
    for i in range(n):
        elem = raw_input("Enter something: ")
        result.append(elem)
    if isPal(result):
        print 'Is a palindrome'
    else:
        print 'Is not a palindrome'

def test_prog():
    arr = ["a", "b", "c"]
    result = isPal(arr)
    print "should be False: ", result
    arr = ["a", "b", "a"]
    result = isPal(arr)
    print "should be True: ", result

test_prog()