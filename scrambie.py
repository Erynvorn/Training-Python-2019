def scramble(s1, s2):
    try:
        for i in s2:
            j = s1.index(i)
            s1 = s1[:j]+s1[j+1:]
        return True
    except:
        return False
