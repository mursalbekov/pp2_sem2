import re
f = input()

x = re.search('a(b{2,3})',f)
if x:
    print("Yes")
else :
    print("No")