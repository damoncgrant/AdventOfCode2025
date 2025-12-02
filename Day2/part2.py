invalid = 0

def checkValid(num: int) -> bool:
    length = len(str(num))

    for i in range(1, int(length/2) + 1):
        if length % i != 0: continue
        l, r = 0, i - 1
        compare = str(num)[l:r + 1]
        possibleMatches = int(length / i) - 1
        matches = 0

        l += i
        r += i
        while r < length:
            if str(num)[l:r+1] == compare:
                matches += 1
            l += i
            r += i

        if matches == possibleMatches:
            return False

    return True

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
