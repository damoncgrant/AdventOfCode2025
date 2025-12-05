fresh = 0

def getBounds(pair: tuple, bank) -> tuple:
    lower = pair[0]
    upper = pair[1]

    for i in range(len(bank)):
        if lower > bank[i][0] and lower < bank[i][1]:
            lower = bank[i][0]
        if upper < bank[i][1] and upper > bank[i][0]:
            upper = bank[i][1]
    
    return (lower, upper)

def checkRange(pair: tuple, bank) -> bool:
    uniqueLower, uniqueUpper = True, True
    for i in bank:
        if pair[0] == i[0]:
            uniqueLower = False
        if pair[1] == i[1]:
            uniqueUpper = False
        
    return uniqueUpper and uniqueLower



with open("example.txt", "r") as file:
    numIn = file.readlines()
    bank = []
    ingredients = []
    for i in range(len(numIn)):
        numIn[i] = numIn[i].strip()
        print(numIn[i])
        f = int(numIn[i][:numIn[i].index('-')])
        s = int(numIn[i][numIn[i].index('-') + 1:])

        bank.append((f, s))

    for i in range(len(bank)):
        pair = getBounds(bank[i], bank)
        if pair not in ingredients:
            ingredients.append(pair)

    # ingredientCopy = ingredients.copy()

    # for i in range(len(ingredients)):
    #     if not checkRange(ingredients[i], ingredients):
    #         ingredientCopy.remove(ingredients[i])
    
    print(ingredients)

    


                

            
            

print(fresh)