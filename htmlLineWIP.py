"""
'<table><tbody><tr><td>1</td><td>1</td><td>2</td><td>3</td><td>2</td><td>4</td><td>5</td><td>6</td><td>3</td><td>7</td><td>8</td><td>9</td></tr></tbody></table>' should equal
'<table><tbody><tr><td>1</td><td>1</td><td>2</td><td>3</td></tr><tr><td>2</td><td>4</td><td>5</td><td>6</td></tr><tr><td>3</td><td>7</td><td>8</td><td>9</td></tr></tbody></table>'

'<table><tbody><tr><td>1</td><td>1</td><td>2</td><td>3</td><td>2</td><td>4</td><td>5</td><td>6</td><td>3</td><td>7</td><td>8</td><td>9</td></tr></tbody></table>' should equal
'<table><tbody><tr><td>1</td><td>1</td><td>2</td><td>3</td></tr><tr><td>2</td><td>4</td><td>5</td><td>6</td></tr><tr><td>3</td><t

d>7</td><td>8</td><td>9</td></tr></tbody></table>'
"""

def to_table(data, header=False, index=False):
    ret = []
    head = []
    content = []
    title = []
    con = []
    
    if header == True:
        title = data[0]
        con = data[1:len(data)]
    else:
        con = data
        
    
    
    if header == True and index == True:
        print("header and index")
        for i in range(len(title)):
            head.append('<th>'+str(title[i])+'</th>')
        head.insert(0,'<thead><tr><th></th>')
        head.append('</tr></thead>')
        for i in range(len(con)):
            content.append('<tr>')
            content.append('<td>'+str(i+1)+'</td>')
            for j in range(len(con[i])):
                content.append('<td>'+str(con[i][j])+'</td>')
            content.append('</tr>')
        content.insert(0,'<tbody>')
        content.append('</tbody>')
        print(content)
    
    elif header == True and index == False: 
        for i in range(len(title)):
            head.append('<th>'+str(title[i])+'</th>')
        head.insert(0,'<thead><tr><th></th>')
        head.append('</tr></thead>')
        for i in range(len(con)):
            content.append('<tr>')
          #  content.append('<td>'+str(i+1)+'</td>')  No index
            for j in range(len(con[i])):
                content.append('<td>'+str(con[i][j])+'</td>')
            content.append('</tr>')
        content.insert(0,'<tbody>')
        content.append('</tbody>')
        print(content)
        
        
    elif header == False and index == True: 
        
        for i in range(len(con)):
            content.append('<tr>')
            content.append('<td>'+str(i+1)+'</td>')  # No index
            for j in range(len(con[i])):
                content.append('<td>'+str(con[i][j])+'</td>')
            content.append('</tr>')
        content.insert(0,'<tbody>')
        content.append('</tbody>')
        print(content)
    
    elif header == False and index == False: 
        print('case 1')
        for i in range(len(con)):
            for j in range(len(con[i])):
                content.append('<td>'+str(con[i][j])+'</td>')
            content.insert(0,'<tbody><tr>')
            content.append('</tr></tbody>')
    
        #insert header structure here with
        # <thead><tr> tr  looping th /th closing </tr></thead>

    
    #open close tbody
        
    


        
    ret.insert(0,''.join(head))
    ret.append(''.join(content))
    ret.insert(0,'<table>')
    ret.append('</table>')
    return ''.join(ret)
