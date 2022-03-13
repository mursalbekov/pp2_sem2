import re
f = input()
x = re.findall("[A-Z][^A-Z]*", f)
print(x)