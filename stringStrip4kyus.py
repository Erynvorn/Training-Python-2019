def solution(string,markers):
    print(string, markers)
    if len(string) > 0:
        for i in markers:
            count = 0
            for j in string: 
                if i == j: 
                    count = count + 1
            for k in range(count):
                print('k '+ str(k))
                print('Yes')
                print(i)
                pos = string.find(i)
                print(pos)
                if pos == -1:
                    break
                else:
                    pos1 = string.find('\n', pos+1)
                    print(pos1)
                    if pos1 == -1 and len(string) == 1:
                        string = ''
                        return string
                    elif pos1 == -1 and len(string) == 2:
                        return string[0]
                    elif pos1 == 1:
                        string = string[1:len(string)].rstrip()+'\n'
                    elif string[pos-1]=='\n' and pos1 != -1:
                        string = string = string[0:pos].rstrip()+'\n'+string[pos1:len(string)]
                    elif string[pos-1] != '\n' and pos1 != -1:
                        string = string = string[0:pos].rstrip()+string[pos1:len(string)]
                    elif string[pos-1] == '\n' and pos1 == -1:  # no more \n
                        string = string[0:pos].rstrip()+'\n'
                    elif string[pos-1] != '\n' and pos1 == -1:
                        string = string[0:pos].rstrip()
                    else:
                        True
                    
    print(string)
    return string


      """
Code probably buggy at this stage
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.


Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas""""
    
