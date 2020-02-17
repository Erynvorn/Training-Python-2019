#! /usr/bin/env python3
# renameDates.py -Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# Create a regex that matches files with the American date format

datePattern = re.compile(r"""^(.*?)  # all text before the date
    ((0|1)?\d)-                      # one or two digits for the mont
    ((0|1|2|3|)?\d)-                 # one or two digits for the day
    ((19||20)\d\d)                   # four digits for the year
    (.*?)$                           # all text after the date
    """, re.VERBOSE)

#TODO : Loop over the files in the working directory

for amerFile in os.listdir('.'):
    mo = datePattern.search(amerFile)
   
    
#TODO : skip files without date
    if mo == None:
        continue
    # print(mo)
#TODO : get the different parts of the filename
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    #print(beforePart)
    #print(monthPart)
    #print(dayPart)
    #print(yearPart)
    #print(afterPart)
#TODO : form the European style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    #print(euroFilename)
#TODO : Get the full absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFile = os.path.join(absWorkingDir,amerFile)
    euroFilename = os.path.join(absWorkingDir,euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFile,euroFilename))
    #shutil.move(amerFile,euroFilename) #uncomment after testing
#TODO : Rename the files
