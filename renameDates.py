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
#TODO : skip files without date
#TODO : get the different parts of the filename
#TODO : form the European style filename
#TODO : Get the full absolute file paths
#TODO : Rename the files
