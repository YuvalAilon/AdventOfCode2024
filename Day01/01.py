input = open("input.txt").read()

l1 = []
l2 = []

def processInput():
    seperated = input.split("\n")
    for line in seperated:
        l1.append(int(line.split(" ")[0]))
        l2.append(int(line.split(" ")[-1]))




def part1():
    dist = 0
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        dist += abs(l1[i]-l2[i])
    return dist

def part2():
    similiarity = 0
    d = {}
    for item in l2:
        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1
    for item in l1:
        if item in d:
            similiarity += (d[item] * item)
    return similiarity


    return 0

processInput()
print("Part 1: " , part1())
print("Part 2: " , part2())