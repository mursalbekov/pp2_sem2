def recursion(s, l, i, x, sum):
    if(i < l):
        if (s[i] == "1"):
            x = 1*2**i
            sum = sum + x
    else:
        print(sum)
        return 0
    recursion(s, l, i + 1, x, sum)
       
s = str(input())[::-1]
l = len(s)
x = int()
sum = 0
i = 0
recursion(s, l, i, x, sum)  