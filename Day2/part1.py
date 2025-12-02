invalid = 0

def checkValid(num: int) -> bool:
    length = len(str(num))
    if length % 2 != 0: return True

    num1 = str(num)[0:int(length/2)]
    num2 = str(num)[int(length/2):]

    return num1 != num2

with open('input.txt', 'r') as file:
    numIn = file.readlines()[0].split(',')
    for i in range(len(numIn)):
        numIn[i] = numIn[i].split('-')
        left = int(numIn[i][0])
        right = int(numIn[i][1])
        for j in range(left, right + 1):
            if not checkValid(j):
                invalid += j

print(invalid)
