from itertools import permutations 


input = open("input.txt").read()
callibrations = []

def baseN(base,n):
    if n == 0:
        return 0
    digits = []
    while n:
        n , r = divmod(n,base)
        digits.append(str(r))
    return ''.join(reversed(digits))
    

def processInput():
    for line in input.split("\n"):
        result = line.split(":")
        numbers = result[1].strip()
        numbers = [int(x) for x in numbers.split(" ")]
        numbers.insert(0, int(result[0]))
        callibrations.append(numbers)
    #print(callibrations)

def part1():
    combinations = []
    total = 0
    maxLength = 0
    longestNeeded = len(max(callibrations, key=len)) - 1
    binary = 0
    while binary < 2**longestNeeded:
        for i in range(0,longestNeeded -len(bin(binary)[2:])):
            combinations.append(i*"0"+bin(binary)[2:])
        binary += 1
    #print(combinations)
    for line in callibrations:
        gotCallibration = False
        for operationString in combinations:
            #print(operationString,len(operationString), line, len(line) - 2)
            if len(operationString) == len(line) - 2 and not gotCallibration:
                runningTotal = line[1]
                #print(line, runningTotal, i)
                for i in range(len(operationString)):
                    if operationString[i] == "0":
                        runningTotal *= line[i+2]
                    else:
                        runningTotal += line[i+2]
                if runningTotal == line[0]:
                    total += runningTotal
                    gotCallibration = True
    return total
                    
def part2():
    combinations = []
    longestNeeded = len(max(callibrations, key=len)) - 1
    total = 0
    num = 0
    while num < 3**longestNeeded:
        for i in range(0,longestNeeded - len(str(baseN(3,num)))):
            combinations.append(i*"0"+str(baseN(3,num)))
        num += 1
    for line in callibrations:
        gotCallibration = False
        for operationString in combinations:
            #print(operationString,len(operationString), line, len(line) - 2)
            if len(operationString) == len(line) - 2 and not gotCallibration:
                runningTotal = line[1]
                #print(line, runningTotal, i)
                for i in range(len(operationString)):
                    if operationString[i] == "0":
                        runningTotal *= line[i+2]
                    elif operationString[i] == "1":
                        runningTotal += line[i+2]
                    else:
                        runningTotal = int(str(runningTotal) + str(line[i+2]))
                if runningTotal == line[0]:
                    total += runningTotal
                    gotCallibration = True
    return total

processInput()
print("Part 1: " , part1())
print("Part 2: " , part2())