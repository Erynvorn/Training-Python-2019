import traceback
try:
    raise Exception('This is the error message')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The trackback info was save in errorInfo.txt.')
