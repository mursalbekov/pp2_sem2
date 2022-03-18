from math import sqrt
import time 
print("Sample Input:")
n = int(input())
k = int(input())
j = sqrt(n)
time.sleep(k/1000)
print("Sample Output:")
print("Square root of " + str(n) + " after " + str(k) + " miliseconds " + "is", end = ' ')
print(j)
