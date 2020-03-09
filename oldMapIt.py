#! /usr/bin/env python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard
#command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    print(len(sys.argv))
    print(sys.argv)
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    #get address from clipboard
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/'+ address)

