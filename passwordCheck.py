import re

def password(string):
    cap = re.compile(r'[A-Z]+')
    low = re.compile(r'[a-z]+')
    nym = re.compile(r'[0-9]+')
    l = len(string)
    
    return l > 7 and cap.search(string) != None and low.search(string) != None and nym.search(string) != None
    
  
