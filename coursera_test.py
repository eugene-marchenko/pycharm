import re
x = 'From cwen@iupui.edu Thu Jan  3 16:23:48 2008'
print re.findall('@([^ ]*)', x)
print re.findall('[^ ](:)[^ ]', x)