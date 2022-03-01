print("a)")
a, b = input().split()
a = int(a)
b = int(b)
g = (i*i for i in range(a, b))
print(g)
for i in g:
	print(i, end = ' ')
print()
print("b)")
for i in range(a, b):
	print(i*i, end = ' ')