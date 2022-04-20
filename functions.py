import sys
import re

def findLineWithPar(data,par):
    isIn = []
    for line in data:
        isIn.append(isWordInLine(line,par))
    return isIn

def isWordInLine (line, par):
    line=line.split()
    for item in line:
        string = item.casefold()
        string =re.sub(r'[\W]', '', string)

        if string in par:
            return 1
    return -1

def printLine(isIn, data):
    l = len(data)
    for i in range (0,l):
        if isIn[i]==1:
            print(data[i], file=sys.stdout)
        elif isIn[i]== -1:
            print(i+1,data[i], file=sys.stderr)