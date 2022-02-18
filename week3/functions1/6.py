def reverse_string():
	string = input()
	rev = string.split()
	rev.reverse()
	for i in rev:
		print(i, end = ' ')
reverse_string()