import os

filename = 'test_files/test.txt'
if not os.path.exists(os.path.dirname(filename)):
    os.makedirs(os.path.dirname(filename))
with open(filename, "w") as f:
    f.write("FOOBAR")