input = open("input.txt").read()
guard = "^"
obstacle = "#"
empty = "."
partOfPath = "X"

def turn90Degrees(facing):
    if facing == (-1,0):
        return (0,1)
    elif facing == (0,1):
        return (1,0)
    elif facing == (1,0):
        return (0,-1)
    elif facing == (0,-1):
        return (-1,0)

def MoveGuardOne(x, y, facing, map, obstacleX = -1, obstacleY = -1):
    if 0 <= (y + facing[0]) < len(map) and 0 <= (x + facing[1]) < len(map[0]):
        if map[y + facing[0]][x + facing[1]] == obstacle or (x + facing[1] == obstacleX and y + facing[0] == obstacleY):
            return(True,x,y, turn90Degrees(facing))
        else:
            x = x + facing[1]
            y = y + facing[0]
            map[y][x] = partOfPath
        return (True, x, y, facing)
    else:
        return (False, x, y, facing)


def processInput():
    map = []
    lines = input.split("\n")
    currentY = 0
    for line in lines:
        lineList = list(line)
        if guard in line:
            y = currentY
            x = line.index(guard)
            lineList[line.index(guard)] = partOfPath
        map.append(lineList)
        currentY += 1
    return (x,y,map)
            

def part1():
    processedInput = processInput()
    x = processedInput[0]
    y = processedInput[1]
    map = processedInput[2]
    locationsVisited = {(x,y)}
    facing = (-1,0)
    validMove = (True,x,y)
    while validMove[0]:
        validMove = MoveGuardOne(x,y,facing,map)
        x = validMove[1]
        y = validMove[2]
        facing = validMove[3]
        locationsVisited.add((x,y))
    return len(locationsVisited)
    #lower than  5318
    

def part2():
    processedInput = processInput()
    x = processedInput[0]
    y = processedInput[1]
    map = processedInput[2]
    facing = (-1,0)
    possibleObstacleLocations = set()
    validMove = (True,x,y)
    while validMove[0]:
        validMove = MoveGuardOne(x,y,facing,map)
        x = validMove[1]
        y = validMove[2]
        facing = validMove[3]
        possibleObstacleLocations.add((x,y))
    loopingObstacleLocations = 0
    for (ObstacleX,ObstacleY) in possibleObstacleLocations:
        x = processedInput[0]
        y = processedInput[1]
        facing = (-1,0)
        validMove = (True,x,y)
        positions = {(x,y,facing)}
        while validMove[0]:
            validMove = MoveGuardOne(x,y,facing,map, ObstacleX, ObstacleY)
            x = validMove[1]
            y = validMove[2]
            facing = validMove[3]
            if validMove[0] == False:
                break
            if (x,y,facing) in positions:
                loopingObstacleLocations += 1
                break
            else:
                positions.add((x,y,facing))
    return loopingObstacleLocations


print("Part 1: " , part1())
print("Part 2: " , part2())