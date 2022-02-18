def hist(h):
	for i in h:
		for j in range (i):
			print('*', end ='')
		print()
print(hist([4, 9, 7]))