#! /usr/bin/env python3

#basic python starter

import requests, math, re, webbrowser, sys, pyperclip, logging

logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.DEBUG)
#there are five level of degug: DEBUG, INFO, WARNING, ERROR, CRITICAL

logging.debug('Start of program')

import math

def area(d, l): 
    if d <= l :
        return "Not a rectangle"
    else :
        return round(l * math.sqrt(d*d-l*l),2)
    # your code here
    #a2 + b2 = c2
    #b = sqrt d2-l2

logging.debug('End of program')


print(area(5,3))
