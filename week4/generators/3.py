n = int(input())
a = (i for i in range (0, n))
print(a)
for i in a:
	if (i % 3 == 0 and i % 4 == 0):
		print(i, end = ' ')