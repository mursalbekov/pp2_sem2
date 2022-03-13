import re
f = input()

x = re.search('^[a-z]+_[a-z]+$',f)
if x:
    print("Yes")
else :
    print("No")
print(x)
