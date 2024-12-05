input = open("input.txt").read()

ordering = []
orderingDic = {}
lists = []

def pairIn(a,b, list):
    return a in list and b in list

def middle(list):
    return list[len(list)//2]

def processInputPart1():
    lines = input.split("\n")
    for line in lines:
        if "|" in line:
            pair = line.split("|")
            ordering.append((int(pair[0]),int(pair[1])))
        if "," in line:
            lists.append([int(x) for x in line.split(",")])

def processInputPart2():
    lines = input.split("\n")
    for line in lines:
        if "|" in line:
            pair = line.split("|")
            if not int(pair[1]) in orderingDic:
                orderingDic[int(pair[1])]=[]
            orderingDic[int(pair[1])].append(int(pair[0]))

def part1():
    total = 0
    for list in lists:
        valid = True
        for pair in ordering:
            if pairIn(pair[0],pair[1],list):
                if list.index(pair[1]) < list.index(pair[0]):
                    valid = False
        if valid:
            total += middle(list)
    return total


def part2():
    total = 0
    for pageList in lists:
        valid = True
        listCopy = list(pageList)
        for itemIndex in range(len(pageList)):
            item = listCopy[itemIndex]
            if item in orderingDic:
                for rule in orderingDic[item]:
                    if rule in pageList and pageList.index(rule) > pageList.index(item):
                        valid = False
                        isCorrect = False
                        while not isCorrect:
                            currentItemIndex = pageList.index(item)
                            pageList[currentItemIndex], pageList[currentItemIndex + 1] = pageList[currentItemIndex +1], pageList[currentItemIndex]
                            if pageList.index(rule) < pageList.index(item):
                                isCorrect = True
        if not valid:
            total += middle(pageList)
                



    return total


processInputPart1()
print("Part 1: " , part1())
processInputPart2()
print("Part 2: " , part2())