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
        
    for i in range(len(title)):
        if title[i] == None:
            title[i] = ""
            
    for i in range(len(con)):
        for j in range(len(con[i])):
            if con[i][j] == None:
                con[i][j] = ""
        
    
    
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
        #print(content)
    
    elif header == True and index == False: 
        for i in range(len(title)):
            head.append('<th>'+str(title[i])+'</th>')
        head.insert(0,'<thead><tr>')
        head.append('</tr></thead>')
        for i in range(len(con)):
            content.append('<tr>')
          #  content.append('<td>'+str(i+1)+'</td>')  No index
            for j in range(len(con[i])):
                content.append('<td>'+str(con[i][j])+'</td>')
            content.append('</tr>')
        content.insert(0,'<tbody>')
        content.append('</tbody>')
        #print(content)
        
        
    elif header == False and index == True: 
        
        for i in range(len(con)):
            content.append('<tr>')
            content.append('<td>'+str(i+1)+'</td>')  # No index
            for j in range(len(con[i])):
                content.append('<td>'+str(con[i][j])+'</td>')
            content.append('</tr>')
        content.insert(0,'<tbody>')
        content.append('</tbody>')
        #print(content)
    
    elif header == False and index == False: 
        print('case 1')
        print(data)
        print(con)
        for i in range(len(con)):
            content.append('<tr>')
            for j in range(len(con[i])):
                content.append('<td>'+str(con[i][j])+'</td>')
            content.append('</tr>')
        content.insert(0,'<tbody>')
        content.append('</tbody>')
    
        
    


        
    ret.insert(0,''.join(head))
    ret.append(''.join(content))
    ret.insert(0,'<table>')
    ret.append('</table>')
    return ''.join(ret)
