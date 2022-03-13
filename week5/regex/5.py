import re
f = input()

x = re.search('^a+[\w]+b+$',f)
if x:
    print("Yes")
else :
    print("No")

