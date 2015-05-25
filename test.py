def censor(text):
    for i, c in enumerate(text):
        #print i
        print(i, c)
    print(text[2])

print(censor([1, 2, 3, 1, 4, 5, 1, 5, 6, 1, 8]))

print("\" hello terry!")

print("I do not like ", end="")
print("newlines")

list = [1, 2, 3, 7]
print(list)
list.reverse()
print(list)
print(max(list))
print(list)