input = open("input.txt").read()

antennas = {}
bounds = []
#lower than 356

def inBounds(bounds, coordinates):
    return 0 <= coordinates[0] < bounds[0] and 0 <= coordinates[1] < bounds[1]

def processInput():
    for y,line in enumerate(input.split("\n")):
        for x,char in enumerate(line):
            if char != ".":
                if char in antennas:
                    antennas[char].append((x,y))
                else:
                    antennas[char] = [(x,y)]
    bounds.append(x + 1)
    bounds.append(y + 1)

def part1():
    antinodes = set()

    for _, coordinates in antennas.items():
        for coord1 in coordinates:
            for coord2 in coordinates:
                difference = (coord1[0]-coord2[0], coord1[1]-coord2[1])
                possibleAntinodes = [
                    (coord1[0] - difference[0],coord1[1] - difference[1]),
                    (coord2[0] - difference[0],coord2[1] - difference[1]),
                ]
                for possibleAntinode in possibleAntinodes:
                    if possibleAntinode != coord1 and possibleAntinode != coord2:
                        if inBounds(bounds, possibleAntinode):
                            antinodes.add(possibleAntinode)
    return len(antinodes)


def part2():
    antinodes = set()

    for _, coordinates in antennas.items():
        for coord1 in coordinates:
            for coord2 in coordinates:
                if coord1 != coord2:
                    difference = (coord1[0]-coord2[0], coord1[1]-coord2[1])
                    possibleAntinode = coord1
                    while inBounds(bounds, possibleAntinode):
                         antinodes.add(possibleAntinode)
                         possibleAntinode = (possibleAntinode[0]- difference[0], possibleAntinode[1]- difference[1])
    return len(antinodes)

processInput()
print("Part 1: " , part1())
print("Part 2: " , part2())