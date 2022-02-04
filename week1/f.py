n = int(input())
for i in range(0, n):
    k = int(input())
    if(k <= 10):
        print("Go to work!")
    if(k > 10 and k <= 25):
        print("You are weak")
    if(k > 25 and k <= 45):
        print("Okay, fine")
    if(k > 45):
        print("Burn! Burn! Burn Young!")
