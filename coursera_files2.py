# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
summ = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    count += 1
    summ = summ + float(line[line.find(':')+1:].lstrip())
print "Average spam confidence:", summ / count
#print "Done"