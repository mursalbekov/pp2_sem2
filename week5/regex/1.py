import re
f = input()

x = re.search('^a(b*)',f)
if x:
    print("Yes")
else :
    print("No")