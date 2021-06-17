import os
import chardet    
# first digit of int  int(str(file.readline())[:1])



def findFileCharset(filepath):
    file = open(filepath, "rb")
    result = chardet.detect(file.readline())
    charset=result['encoding']
    return charset

def countNumbersForBenford(file, path):
    numbers = [0,0,0,0,0,0,0,0,0,0]
    total = 0
    filepath = path + '/' + file
    with open(filepath, encoding=findFileCharset(filepath)) as f:
        while True:
            line = f.readline()
            if not line:
                break

            total += 1
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
        print(numbers)
    

def listFiles(path):
    files = os.listdir(path)
    for f in files:
        countNumbersForBenford(f, path)
        print(f)


listFiles('./data')

