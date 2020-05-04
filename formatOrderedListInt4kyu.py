import math

def solution(args):
    print(args)
    print(len(args))
    ret = []
    last = math.inf
    first = -last
    if len(args) == 0:
        return ''
    elif len(args) == 1:
        return str(args[0])
    elif len(args) == 2:
        return str(args[0])+str(args[1])
    else:
        streak = 0
        for i in range(len(args)-2):
            print(str(i)+ 'streak' + str(streak))
            if args[i] == args[i+1] - 1 and args[i] == args[i+2] - 2:
                streak = 1
                last = args[i+2]
                if first == -math.inf :
                    first = args[i]
                print('first'+str(first))
                print('last'+str(last))    
                if i == len(args) -3:
                    ret.append(str(first)+'-'+str(last))
            else:
                if  i == len(args) -3 and streak == 0:
                    ret.append(str(args[i]))
                    ret.append(str(args[i+1]))
                    ret.append(str(args[i+2]))
                    
                elif i == len(args) -3 and streak == 1:
                    ret.append(str(args[i]))
                    ret.append(str(args[i+1]))
                    ret.append(str(args[i+2]))
                    
                elif i == len(args) -3 and streak == 2:
                    ret.append(str(args[i+1]))
                    ret.append(str(args[i+2]))
                    
                elif i == len(args) -3 and streak == 3:
                    ret.append(str(args[i+2]))
                    
                
                
                elif streak == 1:   #end of streak
                    ret.append(str(first)+'-'+str(last))
                    print(ret)
                    streak = 2
                    last = math.inf
                    first = - last
                elif streak == 2:  #wait 2 turn to add again
                    streak = 3
                elif streak == 3 or streak == 0:  #wait one last turn and add
                    streak = 0
                    ret.append(str(args[i]))
                    print(ret)
            
    return ','.join(ret)

"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""
    
