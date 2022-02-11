n = int(input())
dem = []
for i in range(n):
    a, b = [i for i in input().split()]
    dem.append(b)
c = int(input())
for i in range(c):
    h, e, k = [z for z in input().split()]
    k = int(k)
    while k > 0 and e in dem:
        dem.remove(e)
        k -= 1
print(f'Demons left: {len(dem)}')