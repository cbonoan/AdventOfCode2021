import sys

def getHorizontal(commands):
    res = 0
    for c in commands:
        if(c[0] ==  "forward"):
            res += int(c[1])
    return res

def getDepth(commands):
    res = 0
    for c in commands:
        if(c[0] == 'down'):
            res += int(c[1])
        elif(c[0] == 'up'):
            res -= int(c[1])
    
    return res

def getPosition(commands):
    horiz = 0
    depth = 0 
    aim = 0
    for c in commands:
        if(c[0] == "forward"):
            horiz += int(c[1])
            if(aim > 0):
                depth += aim*int(c[1])
        elif(c[0] == "down"):
            aim += int(c[1])
        elif(c[0] == "up"):
            aim -= int(c[1])

    return(horiz*depth)  

if __name__ == '__main__':
    inputFile = f"{sys.argv[1]}"

    with open(inputFile) as f:
        commands = f.readlines()
        commands = [command.rstrip().split() for command in commands]

    horizontalPos = getHorizontal(commands)
    depth = getDepth(commands)
    print("*************PART 1**************")
    print(horizontalPos*depth)

    print("\n*************PART 2**************")
    res = getPosition(commands)
    print(res)