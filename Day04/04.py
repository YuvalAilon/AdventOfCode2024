input = open("input.txt").read()

def processInput():
    return 0

def xmasCount(s):
    return s.count("XMAS") + s.count("SAMX")

def isValidMas(a,b,c,d):
    #   a#b
    #   #A#
    #   c#d
    ad = a + d
    bc = b + c
    return (ad == "MS" or ad == "SM") and (bc == "MS" or bc == "SM")

def getOrEmptyString(x, y, arr):
    if x < 0 or y < 0:
        return ""
    try:
        return arr[x][y]
    except:
        return ""

def part1():
    wordCount = 0
    wordCount += xmasCount(input)
    arrays = input.split("\n")

    for i in range(len(arrays[0])):
        temp = ""
        for j in range(len(arrays)):
            temp += arrays[j][i]
        wordCount += xmasCount(temp)

    maxIncrement = len(arrays)

    for i in range(maxIncrement * -1 , maxIncrement):
        forwardDiagonal = ""
        backDiagonal = ""
        
        for j in range(len(arrays[0])):
            forwardDiagonal += getOrEmptyString(j,j+i, arrays)
            backDiagonal += getOrEmptyString(len(arrays[0])-j-1,j+i, arrays)   
        wordCount += xmasCount(forwardDiagonal) + xmasCount(backDiagonal)

    
    return wordCount
        

def part2():
    wordCount = 0
    arrays = input.split("\n")
    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            if arrays[i][j] == "A":
                wordCount += int(isValidMas(
                    getOrEmptyString(i-1,j-1,arrays),
                    getOrEmptyString(i-1,j+1,arrays),
                    getOrEmptyString(i+1,j-1,arrays),
                    getOrEmptyString(i+1,j+1,arrays)
                ))
    return wordCount

processInput()
print("Part 1: " , part1())
print("Part 2: " , part2())