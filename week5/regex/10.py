import re
 
f = input()
x = re.findall("[A-Z][a-z]*",f)
print("_".join(x).lower())
