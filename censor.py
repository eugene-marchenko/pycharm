# def censor(text, value):
#     lst = text.split()
#     lst_spaces = text.count(' ')
#     print lst_spaces
#     print lst
#     new_list = []
#     new_string = ''
#     for i in lst:
#         space = lst.index(i) + 1
#         print space
#         lst.insert(space, ' ')
#         print lst
#         if i == value:
#             value_len = len(value)
#             sign = '*' * value_len
#             new_list.append(sign)
#         else:
#             new_list.append(i)
#
#
#     for j in new_list:
#         new_string = new_string + j
#
#     return new_string


# def censor(text, word):
#     length = len(word)
#     text = text.split()
#     for index in range(0, len(text)):
#         if text[index] == word:
#             text[index] = "*" * length
#             text = " ".join(text)
#     return text

def censor(text, word):
    if word in text:
        return text.replace(word, "*" * len(word))

print censor('hey hey hey','hey')