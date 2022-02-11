numbers = [int(i) for i in input().split()]
copynumbers = numbers[:]
bool = True
i = 0
while i < len(numbers) - 1:
    if copynumbers[i] == 0:
        i -= 1
        if copynumbers[i] == 0 and i == 0:
            bool = False
            break
        else:
            continue
    else:
        copynumbers[i] = 0
        i += numbers[i]
if bool:
    print('1')
else:
    print('0')