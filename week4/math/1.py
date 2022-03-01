from math import pi
def to_convert(degree):
	x = degree * pi / 180
	return x
print("input degree: ", end = '')
degree = float(input())
print("output radian: ", end = '')
print(to_convert(degree))