spam = ['apple','banana','tofu','cats']

def prds(ll):
    ret=''
    for i in range(len(ll)-2):
        print(i)
        ret+=ll[i]+', '
    ret+=ll[-2]+' and '+ll[-1]
    print( ret)
prds(spam)
