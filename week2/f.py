n = int(input())
s = {}
max = 0
for i in range(n):
        l, r = input().split()
        r = int(r)
        if not(l in s):
            s[l] = r
        else:
            s[l] += r
        if s[l] > max:
            max = s[l]

for n, i in sorted(s.items()):
    if i < max:
        has_to = max - i
        print('{} has to receive {} tenge'.format(n, has_to))
    elif i == max:
        print(f'{n} is lucky!')