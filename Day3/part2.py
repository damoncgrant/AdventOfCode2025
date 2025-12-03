total = 0

with open("example.txt", "r") as file:
    banks = file.readlines()
    for bank in range(len(banks)):
        banks[bank] = list(banks[bank].strip())
        
        for i in range(len(banks[bank])):
            banks[bank][i] = int(banks[bank][i])
        
        stack = []
        num = ""
        counter = 12

        for i in range(len(banks[bank])):
            if counter == 0:
                num += stack.join("")
            if stack == [] and counter > 0:
                stack.append(banks[bank][i])
                counter -= 1
                continue

            



print(total)
            
