splits = set()

cache = {}

def splitBeam(matrix, index):
    if index[0] == len(matrix) - 1:
        return 1    # one timeline
    
    if index in cache:
        return cache[index]

    if matrix[index[0] + 1][index[1]] == '^':
        result = splitBeam(matrix, (index[0] + 1, index[1] - 1)) + splitBeam(matrix, (index[0] + 1, index[1] + 1))
    else:
        result = splitBeam(matrix, (index[0] + 1, index[1]))

    cache[index] = result
    return result

with open("input.txt", "r") as file:
    matrix = file.readlines()
    matrix = [list(s.strip()) for s in matrix]

    start = matrix[0].index('S')
    
    timelines = splitBeam(matrix, (0, start))

    print(timelines)