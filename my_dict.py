my_dict = {
    "value1" : 225,
    "value2" : False,
    "value3" : "variable"
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key, my_dict[key]