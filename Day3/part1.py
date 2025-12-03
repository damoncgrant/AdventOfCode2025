total = 0

with open("input.txt", "r") as file:
    banks = file.readlines()
    for bank in range(len(banks)):
        banks[bank] = list(banks[bank].strip())
        
        for i in range(len(banks[bank])):
            banks[bank][i] = int(banks[bank][i])
        
        maxLeft = [0] * len(banks[bank])
        maxRight = [0] * len(banks[bank])

        for i in range(len(banks[bank])):
            if i == 0:
                maxLeft[i] = banks[bank][i]
            else:
                maxLeft[i] = max(maxLeft[i-1], banks[bank][i])
        for i in range(len(banks[bank])-1, -1, -1):
            if i == len(banks[bank]) - 1:
                maxRight[i] = banks[bank][i]
            else:
                maxRight[i] = max(maxRight[i+1], banks[bank][i])
        
        maxOfMax = maxLeft.index(max(maxLeft))
        if maxOfMax == len(maxLeft) - 1:
            num = int(f"{maxLeft[-2]}{maxRight[-1]}")
        else:
            num = int(f"{maxLeft[maxOfMax]}{maxRight[maxOfMax + 1]}")
        
        total += num

print(total)
            
