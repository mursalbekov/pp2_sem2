x = input().split()
x = set(x)
x = list(x)
x.sort()
print(len(x))
for i in range(0, len(x)):
	y = str(x[i])
	for j in range(0, len(y)):
		if('a' <= y[j] <= 'z'):
			print(y[j], end = '')
		if('A' <= y[j] <= 'Z'):
			print(y[j], end = '')
	print()