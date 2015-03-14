__author__ = 'ymarchanka'
#test = 'testo'
def reverse(test):
    new = ''
    k = len(test)
    i = 1
    while k != 0:
        #print test[len(test)-i]
        new = new + test[len(test)-i]
        k -= 1
        i += 1
    return new

print reverse('8dffhu874nf')