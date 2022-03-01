from math import tan, pi
print("Input number of sides: ", end = '')
n = int(input())
print("Input the length of sides: ", end = '')
a = int(input())
print("The area of polygon is: ", end = '')
s = n*a*a/(4*tan(pi/n))
print(s)