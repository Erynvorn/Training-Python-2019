#! /usr/bin/env python3


# mapIT2.py Launches a map in the browser using an address from
# the command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv)>1:
    #get address from command line
    address = ' '.join(sys.argv[1:])
    #print(sys.argv)
    #print(sys.argv[0])

    #Todo : get address from clipboard
    
else:
    #get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
