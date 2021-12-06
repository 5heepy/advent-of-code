def part_one(input):
    horizontalPosition = 0
    depth = 0

    for command in input:
        parts = command.split()
        direction = parts[0]
        unit = int(parts[1])

        if direction == "forward":
            horizontalPosition += unit
        elif direction == "up":
            depth -= unit
        else:
            depth += unit 


    print("Part one: {}".format(horizontalPosition * depth))


def part_two(input):
    horizontalPosition = 0
    depth = 0
    aim = 0

    for command in input:
        parts = command.split()
        direction = parts[0]
        unit = int(parts[1])

        if direction == "forward":
            horizontalPosition += unit
            depth += aim * unit
        elif direction == "up":
            aim -= unit
        else:
            aim += unit 


    print("Part two: {}".format(horizontalPosition * depth))


def main():
    input = open("input", "r")
    part_one(input)

    input.seek(0, 0)
    part_two(input)


if __name__ == "__main__":
    main()