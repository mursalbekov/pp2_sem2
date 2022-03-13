import re
f = input()
x = re.findall("[A-Z][^A-Z]*", f)
for i in x:
 print(i, end = ' ')