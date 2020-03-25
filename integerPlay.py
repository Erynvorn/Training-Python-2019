import math
i = 1469036001

def numeralRotate(input):
    last = input % 10
    lon = math.log(input,10)
    lon = round(lon-0.5,0)
    ret = (input - last )/10 + math.pow(10,lon)*(last)
    return ret

while True:
    i += 1
    #print(i)
    j = numeralRotate(i)
    if i * 2 == j :
        print(str(i) + '\n' + str(j))
        break
              

# 526  --> 652

#rnge 1-10, 11-100 10001-100000  math.pow = constant may speed up the calc

#idea to speed up





