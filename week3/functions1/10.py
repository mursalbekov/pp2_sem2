def uniq(s):
	l = []
	for i in s:
		if i not in l:
			l.append(i)
	return l
s = list()
s = input()
print(uniq(s))