#! /usr/bin/env python3


# portfolioShare.py Launches a series of tab with Shares
# the command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv)>1:
    #get share name from command line
    share = ' '.join(sys.argv[1:])
    webbrowser.open('https://www.wsj.com/market-data/quotes/' + share)
   
else:
    for share in ['T','VZ','CTL','AAPL', 'DIS','fx/BTCUSD']:
        webbrowser.open('https://www.wsj.com/market-data/quotes/' + share)  
    
