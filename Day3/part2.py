total = 0

with open("input.txt", "r") as file:
    banks = file.readlines()
    for bank in range(len(banks)):
        banks[bank] = list(banks[bank].strip())
        
        for i in range(len(banks[bank])):
            banks[bank][i] = int(banks[bank][i])
        
        currentBank = banks[bank]
        stack = []
        remaining = 12

        for i in range(len(currentBank)):
            dist = len(currentBank) - i 
            
            if stack == []:
                stack.append(currentBank[i])
                remaining -= 1
                continue

            while currentBank[i] > stack[-1] and dist > remaining:
                stack.pop()
                remaining += 1

                if stack == []:
                    break

            if remaining > 0:
                stack.append(currentBank[i])
                remaining -= 1
            
        num = int("".join([str(i) for i in stack]))
        total += num
            
print(total)
            
