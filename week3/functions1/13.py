import random 
 
 
def game(): 
    n = random.randrange(1, 20) 
    print("Hello! What is your name?") 
    s = str(input()) 
    print() 
    print("Well, " + s +", I am thinking of a number between 1 and 20.") 
 
    cnt = 0 
    while True: 
        print("Take a guess.") 
        l = int(input()) 
        if n == l: 
            print("Good job, KBTU! You guessed my number in " + str(cnt) +" guesses!") 
            break 
        else: 
            if l<n: 
                print() 
                print("Your guess is too low.") 
                cnt+= 1 
            else: 
                print() 
                print("Your guess is too much.") 
                cnt+= 1 