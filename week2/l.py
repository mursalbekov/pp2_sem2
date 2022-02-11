s = str(input())
cnt = 0
cnt1 = 0
if(len(s)%2==1):
  print("No")
  break
for i in range(0, len(s)):
  if(s[i] == "(" or s[i] == "[" or s[i] == "{"):
    cnt = cnt + 1
  if(s[i] == ")" or s[i] == "}" or s[i] == "]"):
    cnt1 = cnt1 + 1

if(cnt1 != cnt):
  print("No")
  break