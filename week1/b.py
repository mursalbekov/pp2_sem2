s = input()
s_size = len(s)
sum = 0
for i in range(0, s_size):
    sum = sum + ord(s[i])
if sum < 300:
    print("Oh, no!")
else:
    print("It is tasty!")

