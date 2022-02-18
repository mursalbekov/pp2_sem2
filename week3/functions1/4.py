def prime(numbers):
	l = []
	for i in (numbers):
		cnt = 0
		for j in range(2, i):
			if i % j == 0:
				cnt = cnt + 1
		if (cnt == 0):
			l.append(i)
	return l
numbers = [int (n) for n in input().split()]
print(prime(numbers))