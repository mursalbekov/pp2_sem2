n = int(input())
cnt = 0
l = list()
m = list()
for i in range(0, n):
	s = str(input())
	l.append(s)
length = 0
for i in reversed(range(len(l))):
    if l[i] in l[:i]:
        del l[i]
for i in range(0, len(l)):
	y = str(l[i])
	for j in range(0, len(y)):
		if('a' <= y[j] <= 'z'):
			cnt += 1
			break
	for j in range(0, len(y)):
		if('A' <= y[j] <= 'Z'):
			cnt += 1
			break		    
	for j in range(0, len(y)):
		if('0' <= y[j] <= '9'):
			cnt += 1
			break
	if(cnt == 3):
		length = length + 1
		m.append(l[i])

	cnt = 0;
print(length)
for i in sorted(m):
	print(i)



