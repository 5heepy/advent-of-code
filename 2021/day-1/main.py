def part_one(input):
    previousMeasurement = int(input.readline());
    
    depthIncreasedCount = 0
    for measurement in input.readlines():
        if (int(measurement) > previousMeasurement):
            depthIncreasedCount += 1
        
        previousMeasurement = int(measurement)
    
    print("Part one: Depth increased {} times.".format(depthIncreasedCount))


def part_two(input):
    measurements = list(map(int, input.readlines()))

    groupedMeasurements = []
    for i in range(len(measurements) - 2):
        groupedMeasurement = sum(measurements[i:i + 3])
        groupedMeasurements.append(groupedMeasurement)
        i += 1

    previousMeasurement = groupedMeasurements.pop(0);
    
    depthIncreasedCount = 0
    for measurement in groupedMeasurements:
        if (int(measurement) > previousMeasurement):
            depthIncreasedCount += 1
        
        previousMeasurement = int(measurement)
    
    print("Part two: Depth increased {} times.".format(depthIncreasedCount))


def main():
    input = open("input", "r")
    part_one(input)

    input.seek(0, 0)
    part_two(input)

    input.close();


if __name__ == "__main__":
    main()