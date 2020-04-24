def snail(arr):
    ret = []   # return list
    
    if arr == [[]]:   # if list is empty
        return []
    
    if len(arr) == 1:          #if list has one element
        ret.append(arr[0][0])
        return ret
        
    return snail_recursive(arr,ret)    #call recursion

"""
recursion function has three steps.
collect first line and last column to return list
trim the array from these data
inverse the remaining matrix to be ready for the next recursion

"""

def snail_recursive(arr, ret):

    l = len(arr)            # collect data 1st line and last column
    for i in range(l):
        ret.append(arr[0][i])
    for i in range(1,l):
        ret.append(arr[i][l-1])
    
    arr = trim(arr)           # call trim
    arr = rotateArray(arr)    # call rotate
    
    
    if len(arr) == 1:            # test for exit recursion when arr size = 1
        ret.append(arr[0][0])
        return ret               # if = 1 = finish !
    else:  
        return snail_recursive(arr,ret)  # if not do it again
    
def rotateArray(arr):   # dirty rotate a matrix 
    brr = []
    crr = []
    drr = []
    l = len(arr)
    for i in range(l):
        for j in range(l):
            brr.append(arr[l-i-1][l-j-1])
    for i in range(l):
        for j in range(l):
            crr.append(brr[i*l+j])
        drr.append(crr)
        crr =[]
    return drr
    
def trim(arr):                # manual trimming of collected items
    brr = []
    l = len(arr)
    del arr[0]
    for i in range(l-1):
        del arr[i][l-1]
    return arr
