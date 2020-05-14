import math

def solution(force1, force2, theta) :
    rad = math.radians(theta)
    F = ((force1 + force2*math.cos(rad))**2+(force2*math.sin(rad))**2)**0.5
    #R = math.degrees(math.asin(force2*math.sin(rad)/(force1+force2*math.cos(rad))))
    R = math.degrees(math.acos((force1+force2*math.cos(rad))/F))
    if theta > 180 : 
        R = - R
    return [ F , R ]
    # Your code goes here


    #calculate the resultant force


    from math import cos, radians, sin, atan2, degrees, hypot

def solution(f1, f2, theta):
    r = radians(theta)
    x = f1 + f2 * cos(r)
    y = f2 * sin(r)
    return hypot(x, y), degrees(atan2(y, x))
