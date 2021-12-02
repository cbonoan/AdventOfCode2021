import sys

def getMeasurementIncreases(depths):
    ## PART 1 ##
    # prevDepth = int(depths[0])
    # res = 0
    # for i in range(1, len(depths)):
    #     curDepth = int(depths[i])
    #     if(curDepth > prevDepth):
    #         res += 1
    #     prevDepth = curDepth

    # return res

    ## PART 2 - THREE MESAUREMENT SLIDING WINDOW ##
    prevSum = sum([int(depths[i]) for i in range(3)])
    res = 0
    for i in range(1, len(depths)):
        curSum = 0
        for j in range(i, i+3):
            try:
                curSum += int(depths[j])
            except IndexError as e:
                return res
        if(curSum > prevSum):
            res += 1
        prevSum = curSum
    
    return res

if __name__ == '__main__':
    filePath = f"{sys.argv[1]}"

    with open(filePath) as f:
        contents = f.readlines()

    # Day 1
    increases = getMeasurementIncreases(contents)
    print(increases)