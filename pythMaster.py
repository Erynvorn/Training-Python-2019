#! /usr/bin/env python3

#basic python starter

import requests, math, re, webbrowser, sys, pyperclip, logging

logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.DEBUG)
#there are five level of degug: DEBUG, INFO, WARNING, ERROR, CRITICAL

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of program(%s%%)' %(n))
    n += 2
    return n

loggin.debug('End of program')



