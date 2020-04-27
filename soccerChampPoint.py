def points(games):
    ret = 0
    for i  in range(len(games)):
        if games[i][0]>games[i][2]:
            ret += 3
        elif games[i][0] == games[i][2]:
            ret += 1
    return ret
