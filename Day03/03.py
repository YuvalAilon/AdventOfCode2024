input = open("input.txt").read()

def mul(input):
    total = 0
    instructions = input.split("mul(")
    for instruction in instructions:
        significant = instruction.split(")")[0]
        numberPair = significant.split(",")
        if len(numberPair) == 2 and numberPair[0].isdigit() and numberPair[1].isdigit():
            total += int(numberPair[0]) * int(numberPair[1])
    return total

def part1():
    return mul(input)


def part2():
    total = 0
    instructions = input.split("do()")
    enabled = []
    for instruction in instructions:
        enabled = instruction.split("don't()")[0]
        total += mul(enabled)
    return total

print("Part 1: " , part1())
print("Part 2: " , part2())