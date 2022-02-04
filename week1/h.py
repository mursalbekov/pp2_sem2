s = input()
s = str(s)
n = input()
n = str(n)
l =  len(s)
cnt = 0
for i in range (0, l):
    if (n == s[i]):
        cnt += 1
for i in range (0, l):
    if (n == s[i]):
        print(i, end = ' ')
        break

if (cnt > 1):
    for i in reversed(range (l)):
        if (n == s[i]):
            print(i)
            break