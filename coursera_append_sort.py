fname = raw_input("Enter file name: ")
if fname == '':
    fname = "romeo.txt"
fh = open(fname)
lst = list()

for line in fh:
    #elements = line.split()
    #print elements
    for i in line.split():
        #print i
        if i in lst: continue
        else:
            lst.append(i)
lst.sort()
print lst
