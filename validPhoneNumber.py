import re

def validPhoneNumber(phoneNumber):
    print(phoneNumber)
    tel = re.compile(r'^\((\d)(\d)(\d)\)(\s){1}(\d)(\d)(\d)-(\d)(\d)(\d)(\d)$')
    return tel.search(phoneNumber) is not None
