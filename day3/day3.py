import sys

def getDiagnostic(r):
    gamma = []
    epsilon = []
    for i in range(len(r[0])):
        oneCount  = 0
        zeroCount = 0
        for j in range(len(r)):
            if(r[j][i]) == '1':
                oneCount += 1
            else:
                zeroCount += 1
        if(oneCount > zeroCount):
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    return gamma*epsilon

def getOxyGenRating(r):
    i = 0
    while(len(r) > 1):
        oneCount  = 0
        zeroCount = 0
        for j in range(len(r)):
            if(r[j][i]) == '1':
                oneCount += 1
            else:
                zeroCount += 1
        tmpReport = []
        if(oneCount >= zeroCount):
            for j in range(len(r)):
                if(r[j][i] == '1'):
                    tmpReport.append(r[j])
        else:
            for j in range(len(r)):
                if(r[j][i] == '0'):
                    tmpReport.append(r[j])
        r = tmpReport
        i += 1

    return int(''.join(r),2)

def getC02(r):
    i = 0
    while(len(r) > 1):
        oneCount  = 0
        zeroCount = 0
        for j in range(len(r)):
            if(r[j][i]) == '1':
                oneCount += 1
            else:
                zeroCount += 1
        tmpReport = []
        if(oneCount < zeroCount):
            for j in range(len(r)):
                if(r[j][i] == '1'):
                    tmpReport.append(r[j])
        else:
            for j in range(len(r)):
                if(r[j][i] == '0'):
                    tmpReport.append(r[j])
        r = tmpReport
        i += 1
    
    return int(''.join(r),2)

if __name__ == '__main__':
    inputFile = f"{sys.argv[1]}"

    with open(inputFile) as f:
        report = f.readlines()
        report = [line.rstrip() for line in report]
    
    # print("PART1")
    # print(getDiagnostic(report))

    oxygenGenRating = getOxyGenRating(report)
    C02Rating = getC02(report)
    print(oxygenGenRating * C02Rating)