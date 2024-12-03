input = open("input.txt").read()

reports = []

def processInput():
    seperated = input.split("\n")
    for line in seperated:
        reports.append([int(x) for x in line.split(" ")])

def isSafe(report):
    isSafe = True
    increasing = report[0] - report[1] < 0
    for i in range(len(report) - 1):
        dif = report[i] - report[i+1]
        if dif == 0 or abs(dif) > 3:
            isSafe = False
        if dif > 0 and increasing:
            isSafe = False
        if dif < 0 and not increasing:
            isSafe = False
    return isSafe

def part1():
    safe = 0
    for report in reports:
        if isSafe(report):
            safe += 1
    return safe

def part2():
    safe = 0
    for report in reports:
        for i in range(len(report)):
            copy = report.copy()
            del copy[i]
            if isSafe(copy):
                safe += 1
                break
    return safe

processInput()
print("Part 1: " , part1())
print("Part 2: " , part2())