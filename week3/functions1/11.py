def check(p):
	s=p[::-1]
	if s==p:
		return True
	else:
		return False


p=str(input())
print(check(p))