tuple = []
tuple = input()
cnt = 0
def testtrue(tuple):
	for i in range(0, len(tuple)):
		if(tuple[i] == True):
			cnt = cnt + 1
	if (cnt == len(tuple)):
		return True
	else:
		return False
print(testtrue())
