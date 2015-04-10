fname = raw_input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
dic_result = dict()
mail_list = list()
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        mail_list.append(line.split()[1])
for email in mail_list:
    dic_result[email] = dic_result.get(email, 0) + 1
print dic_result

biggestword = None
count = None
for key, value in dic_result.items():
    if biggestword is None or value > count:
        biggestword = key
        count = value
print biggestword, count
