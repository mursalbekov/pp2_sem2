a,f = input().split()
a = int(a)
f = int(f)
k = 0
for i in range(2, a // 2 + 1):
    if (a % i == 0): 
        k = k+1
if (k == 0 and a < 500 and f % 2 == 0):
    if (a < 500):
        if (f % 2 == 0):
            print("Good job!")
else:
    print("Try next time!")