n = int(input())
a = (i for i in reversed(range(0, n)))
print(a)
for i in a:
	print(i, end = ' ')
