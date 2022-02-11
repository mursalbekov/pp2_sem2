n = input().split()
xor = 0
l = list()
if(len(n) == 1):
	k = int(n[0])
	x = int(input())
	for i in range(k):
		m = x + 2*i
		l.append(m)
	for i in range(len(l)):
		y = int(l[i])
		xor = xor ^ y
else:
	k = int(n[0])
	x = int(n[1])
	for i in range(k):
		m = x + 2*i
		l.append(m)
	for i in range(len(l)):
		y = int(l[i])
		xor = xor ^ y

print(xor)