input = open("input.txt").read()
fileSystem = []

def nearestFileID(fileSystem, index):
    currentFileID = fileSystem[index]
    currentIndex = index
    while currentFileID == -1:
        currentIndex -= 1
        currentFileID = fileSystem[currentIndex]
    return (currentFileID,currentIndex)

def checkSum(fileSystem):
    checkSum = 0
    for index, element in enumerate(fileSystem):
        if element != -1:
            checkSum += index * element
    return checkSum

def findFileLength(fileSystem, index, left):
    #assumes that index is the beggining/end of a file
    size = 0
    modifier = 1
    fileID = fileSystem[index]
    currentfileID = fileSystem[index]
    if left:
        modifier = -1
    while currentfileID == fileID and index >= 0 and index < len(fileSystem):
        index += modifier
        try:
            currentfileID = fileSystem[index]
        except:
            currentfileID = fileID - 1
        size += 1
    return size
    
    

def processInput():
    fileID = 0
    isFile = True
    for char in input:
        if isFile:
            for _ in range(int(char)):
                fileSystem.append(fileID)
            fileID += 1
        else:
            for _ in range(int(char)):
                fileSystem.append(-1)
        isFile = not isFile

def part1():
    checkSum = 0
    leftIndex = 0
    rightIndex = len(fileSystem) - 1
    while leftIndex <= rightIndex:
        if fileSystem[leftIndex] != -1:
            checkSum += (leftIndex * fileSystem[leftIndex])
        else:
            runNearestFileID = nearestFileID(fileSystem,rightIndex)
            checkSum += (runNearestFileID[0] * leftIndex)
            rightIndex = runNearestFileID[1] - 1
        leftIndex += 1
    return checkSum


def part2():
    files = list(fileSystem)
    largestFileID = max(files)
    currentFileID = largestFileID
    leftIndex = 0
    rightIndex = len(files) - 1
    while currentFileID >= 0:
        currentFileLength = findFileLength(files, rightIndex, True)
        if files[rightIndex] == currentFileID:
            while leftIndex < rightIndex:
                if files[leftIndex] == -1:
                    possibleSpaceLength = findFileLength(files, leftIndex, False)
                    if possibleSpaceLength >= currentFileLength:
                        files[leftIndex : leftIndex + currentFileLength] = [files[rightIndex]] * currentFileLength
                        files[rightIndex - currentFileLength + 1 : rightIndex + 1] = [-1] * currentFileLength
                        break
                leftIndex += findFileLength(files, leftIndex, False)
            leftIndex = 0
            currentFileID -= 1
        rightIndex -= currentFileLength
    return checkSum(files)




processInput()
print("Part 1: " , part1())
print("Part 2: " , part2())