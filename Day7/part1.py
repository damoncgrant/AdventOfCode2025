splits = set()

def splitBeam(matrix, index):
    if index[0] == len(matrix) - 1:
        return
    if matrix[index[0] + 1][index[1]] == '^':
        if (index[0] + 1, index[1]) not in splits:
            splits.add((index[0] + 1, index[1]))
            splitBeam(matrix, (index[0] + 1, index[1] - 1))
            splitBeam(matrix, (index[0] + 1, index[1] + 1))
    else:
        splitBeam(matrix, (index[0] + 1, index[1]))


with open("input.txt", "r") as file:
    matrix = file.readlines()
    matrix = [list(s.strip()) for s in matrix]

    start = matrix[0].index('S')
    
    splitBeam(matrix, (0, start))

    print(len(splits))