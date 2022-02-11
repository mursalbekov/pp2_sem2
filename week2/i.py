n = int(input())
l1 = list()
l2 = list()
for i in range(0, n):
	l = input().split()
	if(len(l) == 2):
		l2.append(l[1])
	else:
		l1.append(l[0])
for i in range(len(l1)):
	print(l2[i], end = ' ')