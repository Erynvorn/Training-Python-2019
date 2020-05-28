def validate_battlefield(field):
    tot = 0
    for i in range(10):
        tot += sum(field[i])
    if tot != 20:
         return False
    #anti collision
    # coins
    if field[0][0] + field[0][1] + field [1][0] == 3:
        return False
    if field[0][0] + field[1][1] == 2 :
        return False
    if field[9][9] + field[9][8] + field [8][9] == 3:
        return False
    if field[9][9] + field[8][8] == 2 :
        return False
    if field[9][0] + field[9][1] + field [8][0] == 3:
        return False
    if field[9][0] + field[8][1] == 2 :
        return False
    if field[0][9] + field[1][8] + field [0][8] == 3:
        return False
    if field[0][9] + field[1][8] == 2 :
        return False
    """
    #ligne cote
    for i in range(1,9):
        if field[0][i] + field[1][i-1] == 2:
            return False
        elif field[9][i] + field[9][i-1] == 2:
            return False
        elif field[i][0] + field[i-1][1] == 2:
            return False
        elif field[i][9] + field[i-1][8] == 2:
            return False
    """       
    for i in range(1,9):
        for j in range(1,9):
            if field[i][j] == 1:
                if field[i-1][j-1] + field[i+1][j-1]+ field[i-1][j+1]+ field[i+1][j+1] > 0:
                    return False
    
    #search  > four, the four, then 2 x three
    battelship , cruisers , destroyers, submarines = 0,0,0,0
    for i in range(10):
        for j in range(6):
            if field[j][i]+field[j+1][i] +field[j+2][i]+field[j+3][i] == 4:
                battelship += 1
    for i in range(10):
        for j in range(6):
            if field[i][j]+field[i][j+1]+field[i][j+2]+field[i][j+3] == 4:
                battelship += 1
    if battelship > 1:
        return False
    return True
