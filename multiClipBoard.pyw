#! /usr/bin/env python3

#mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe multiClipBoard.pyw save <keyword> - Saves clipboard to keyword
# Usage: py.exe multiClipBoard.pyw <keyword> - Loads clipboard to keyword
# Usage: py.exe multiClipBoard.pyw list - SLoads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# todo : save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # todo : List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperlip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()


