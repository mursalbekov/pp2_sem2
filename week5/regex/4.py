import re
f = input()

x = re.search('[A-Z]_[a-z]+$',f)
if x:
    print("Yes")
else :
    print("No")
print(x)
