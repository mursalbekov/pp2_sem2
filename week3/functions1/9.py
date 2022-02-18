import math
def sphere(r):
	s = 4/3 * 3.14 * pow(r, 3)
	return s
r = int(input())
print(sphere(r))