import re
f = input()
x = re.sub("[ ,. ]",':',f)
print(x)