#! /usr/bin/env python3


# mapIT2.py Launches a map in the browser using an address from
# the command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv)>1:
    #get share name from command line
    share = ' '.join(sys.argv[1:])
    #print(sys.argv)
    #print(sys.argv[0])

    #Todo : get address from clipboard
    
else:
    #get address from clipboard
    share = pyperclip.paste()

webbrowser.open('https://www.wsj.com/market-data/quotes/' + share)



#https://www.wsj.com/market-data/quotes/AAPL

