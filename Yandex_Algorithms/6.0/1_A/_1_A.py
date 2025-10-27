import re

dist = []

#f = open('test.txt', 'r')

i = 0
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())
#for line in f:
    #dist.append(int(line))
    #if i == 0:
    #    x1 = int(line)
    #    i+=1
    #elif i == 1:
    #    y1 = int(line)
    #    i+=1
    #elif i == 2:
    #    x2 = int(line)
    #    i+=1
    #elif i == 3:
    #    y2 = int(line)
    #    i+=1
    #elif i == 4:
    #    x = int(line)
    #    i+=1
    #elif i == 5:
    #    y = int(line)
    #    i+=1

    ##match i:
    ##    case 0:
    ##        x1 = int(line)
    ##        i+=1
    ##    case 1:
    ##        y1 = int(line)
    ##        i+=1
    ##    case 2:
    ##        x2 = int(line)
    ##        i+=1
    ##    case 3:
    ##        y2 = int(line)
    ##    case 4:
    ##        x = int(line)
    ##        i+=1
    ##    case 5:
    ##        y = int(line)
    ##        i+=1

#print(x1,y1,x2,y2,x,y)

#”NW”, ”NE”, ”SW”, ”SE”.
if x<x1:
    if y>y2:
        print("NW")
    elif y>y1:
        print("W")
    else:
        print("SW")
elif x < x2:
    if y>y2:
        print("N")
    else:
        print("S")
else:
    if y>y2:
        print("NE")
    elif y > y1:
        print("E")
    else:
        print("SE")