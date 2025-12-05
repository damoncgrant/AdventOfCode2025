fresh = 0

with open("input.txt", "r") as file:
    numIn = file.readlines()
    bank = []
    ingredients = []
    for i in range(len(numIn)):
        numIn[i] = numIn[i].strip()
        if '-' in numIn[i]:
            f = int(numIn[i][:numIn[i].index('-')])
            s = int(numIn[i][numIn[i].index('-') + 1:])
            bank.append((f, s))
        elif numIn[i] == "":
            continue
        else:
            for j in bank:
                if int(numIn[i]) >= j[0] and int(numIn[i]) <= j[1]:
                    fresh += 1
                    break

print(fresh)