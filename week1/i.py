n = int(input())
for i in range(0, n):
    s = input()
    st = "@gmail.com"
    if (st in s):
        removed = s.replace("@gmail.com", "")
        print(removed)
    
