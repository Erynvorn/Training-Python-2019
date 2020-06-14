# decompose an integer in sum of distinct power of three 
#https://www.codewars.com/kata/simple-fun-number-290-sum-of-threes/python 6kyu

def sum_of_threes(n) :
    depth=[]
    count=0
    result=""
    sumthrees(n,depth,count)
    for i in depth :
        if i == "Impossible" :
            result = "Impossible"
            return result
    else:
        depth.reverse()
        l = len(depth)
        i=0
        while i<l-1 :
            depth[i]= "3^" + str(depth[i]) +"+"
            i +=1
        depth[l-1] = "3^" + str(depth[l-1])
        for i in depth : 
            result = result + i
        return result
    
    

def sumthrees(n,depth,count):
    if n == 1 : 
        depth.append(count)
        return  depth
    else: 
        if n % 3 == 0 :
            
            count += 1
            return sumthrees ( n/3, depth,count)
        elif n % 3 == 1 :
            depth.append(count)
            count += 1
            
            return sumthrees ((n-1)/3, depth,count)
        else:
            depth.append("Impossible")
            return depth
