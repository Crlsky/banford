import os
import chardet
import math
# first digit of int  int(str(file.readline())[:1])



def findFileCharset(filepath):
    file = open(filepath, "rb")
    result = chardet.detect(file.readline())
    charset=result['encoding']
    return charset

def countNumbersForBenford(file, path):
    numbers = [0,0,0,0,0,0,0,0,0,0]
    filepath = path + '/' + file
    with open(filepath, encoding=findFileCharset(filepath)) as f:
        while True:
            line = f.readline()
            if not line or line == '\n':
                break
            number = int(str(line)[:1])
            if number == 0:
                numbers[0] += 1
            if number == 1:
                numbers[1] += 1
            if number == 2:
                numbers[2] += 1
            if number == 3:
                numbers[3] += 1
            if number == 4:
                numbers[4] += 1
            if number == 5:
                numbers[5] += 1
            if number == 6:
                numbers[6] += 1
            if number == 7:
                numbers[7] += 1
            if number == 8:
                numbers[8] += 1
            if number == 9:
                numbers[9] += 1
    return numbers

def numberOfLines(array):
    total = 0
    for x in array:
        total += x
    return total

def percentOfNumber(number,nol):
    return round(number*100/nol)

def benford(i):
    return round(math.log(1+(1/i),10)*100)

def similarity(a,b):
    if b == 0:
        return 0
    return a/b

def benfordDistrib(percent, benfordPercent, digit, tolerance):
    if(percent < benfordPercent+tolerance and percent > benfordPercent-tolerance):
        return 1
    else:
        return 0
    
def listFiles(path):
    result = dict()
    files = os.listdir(path)
    for f in files:
        sumBenford = 0
        iteration = 0
        arrayOfnumbers = countNumbersForBenford(f, path)
        nol = numberOfLines(arrayOfnumbers)
        fileName = f.split(".")[0]
        for v in arrayOfnumbers:
            iteration += 1
            if iteration > 9 :
                continue
            percentNumber = percentOfNumber(arrayOfnumbers[iteration], nol)
            benfordPercent = benford(iteration)
            sumBenford += benfordDistrib(percentNumber, benfordPercent, iteration, 4)
            
            #print(benfordPercent, percentNumber)
        result[fileName]=round(sumBenford/9,2)

    result = dict(sorted(result.items(), key=lambda item: item[1]))
    print(result)


listFiles('./data')

