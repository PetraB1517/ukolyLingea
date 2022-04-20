import sys
import re

par = []
dataFile = []



l = len(sys.argv)
if l < 3 : 
    print("Bylo zadano malo parametru")
    sys.exit()


data = sys.argv[1]



for i in range (2, l):
    par.append(sys.argv[i])

with open(data) as input_file:
    for line in input_file:
        dataFile.append(line)
        

