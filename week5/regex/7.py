import re
f = input()

x = re.sub("['_']",' ',f)
y = re.sub("\s", '' ,x.title())
print(y)