password = 0
dial = 50

with open('input.txt', 'r') as file:
    numIn = file.readlines()
    for i in range(len(numIn)):
        numIn[i] = numIn[i].strip()
        direction = numIn[i][0]
        value = int(numIn[i][1:])
        if direction == 'R':
            dial += value
            while dial > 99:
                dial -= 100
        else:
            dial -= value
            while dial < 0:
                dial += 100
        if dial == 0:
            password += 1

print(password)