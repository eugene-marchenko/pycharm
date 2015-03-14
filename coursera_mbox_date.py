fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
dic_result = dict()
list = list()

for line in fh:
    if line.startswith('From:'):
        #print line
        continue

    elif line.startswith('From'):
        #continue
        #print line
        list.append(line.split()[5].split(':')[0])
        #dic_result[line] = dic_result.get(line, 0) + 1

for i in list:
    dic_result[i] = dic_result.get(i, 0) + 1



print dic_result.items()
for x, y in sorted( [ (k, v) for k, v in dic_result.items()] ):
    print x, y
