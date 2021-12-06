from collections import OrderedDict

def part_one(input):
    lines = input.readlines()
    zeros = OrderedDict(
        [(i,0) for i in range(len(lines[0]) - 1)]
    )
    
    for number in lines:
        for i in range(len(number)):
            if (number[i] == "0"):
                count = zeros.get(i)
                count += 1
                zeros[i] = count
    
    gamma = ""
    epsilon = ""
    for key, value in zeros.items():
        if value > len(lines) - value:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    factor = int(gamma, 2) * int(epsilon, 2)

    print("Part one: {}".format(factor))



def part_two(input):
    pass


def main():
    input = open("input", "r")
    part_one(input)

    input.seek(0, 0)
    part_two(input)

    input.close();


if __name__ == "__main__":
    main()