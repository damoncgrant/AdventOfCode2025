total = 0
numbers = []
symbols = []

def multiply(nums):
    if nums == []:
        return 1
    return nums[0] * multiply(nums[1:])

def add(nums):
    if nums == []:
        return 0
    return nums[0] + add(nums[1:])

with open("input.txt", "r") as file:
    numIn = file.readlines()
    for i in range(len(numIn)):
        row = []
        numIn[i] = numIn[i].strip()

        block = ""
        for j in numIn[i]:
            if j == " "  and block != "":
                row.append(int(block))
                block = ""
            elif j == " " and block == "":
                continue
            elif j == "*" or j == "+":
                symbols.append(j)
            else:
                block += j

        if block.isdigit():
            row.append(int(block))
        if row != []:   
            numbers.append(row)
    
    for s in range(len(symbols)):
        using = []
        if symbols[s] == "*":
            total += multiply([num[s] for num in numbers])
        elif symbols[s] == "+":
            total += add([num[s] for num in numbers])

print(total)

    
    
    
    
