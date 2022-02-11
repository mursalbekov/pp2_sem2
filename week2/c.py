n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
for i in range(0, n):
	for j in range(0, n):
		if(i * j == 0):
			a[i][0] = i

for i in range(0, n):
	for j in range(0, n):
		if(i * j == 0):
			a[0][j] = j

for i in range(0, n):
	for j in range(0, n):
		if(i == j):
			a[i][j] = i*j

for i in range(0, n):
	for j in range(0, n):
		[print(a[i][j], end = ' ')]
	print()