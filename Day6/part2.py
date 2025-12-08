total = 0

def multiply(nums):
    if nums == []:
        return 1
    if not nums[0].isdigit():
        return multiply(nums[1:])
    else:
        return int(nums[0]) * multiply(nums[1:])

def add(nums):
    if nums == []:
        return 0
    if not nums[0].isdigit():
        return add(nums[1:]) 
    else:
        return int(nums[0]) + add(nums[1:]) 

with open("input.txt", "r") as file:
    numIn = file.readlines()
    numIn = [list(i) for i in numIn]
    numCount = len(numIn) - 1   # exclude symbols
    symbolCount = numIn[-1].count("*") + numIn[-1].count("+")
    expressions = {}
    symbols = []


    for i in range(symbolCount):
        expressions[i] = {}
    
    for i in range(len(numIn[-1]) - 1, -1, -1):
        if numIn[-1][i] == "*" or numIn[-1][i] == "+":
                symbols.append(numIn[-1][i])

    for r in numIn:
        if "*" in r or "+" in r:
            break

        r.pop()

        exp = 0
        pos = 0
        validNum = True
        for i in range(len(r)-1, -1, -1):
            if not validNum:
                validNum = True
                continue

            if numIn[-1][i] in symbols:
                validNum = False
                if pos in expressions[exp].keys():
                    expressions[exp][pos] += r[i] if r[i].isdigit() else ""
                else:
                    expressions[exp][pos] = r[i] if r[i].isdigit() else ""
                pos = 0
                exp += 1

            else:
                if pos in expressions[exp].keys():
                    expressions[exp][pos] += r[i] if r[i].isdigit() else ""
                else:
                    expressions[exp][pos] = r[i] if r[i].isdigit() else ""
                pos += 1
            
    for s in range(len(symbols)):
        if symbols[s] == "*":
            total += multiply([num for num in expressions[s].values()])
        elif symbols[s] == "+":
            total += add([num for num in expressions[s].values()])

print(total)

    
    
    
    
