l = str()
l = input()
cnt = 0
for i in range(0, len(l)):
	if ('A' <= l[i] <= 'Z' or 'a' <= l[i] <= 'z' ):
		cnt += 1
print(cnt)