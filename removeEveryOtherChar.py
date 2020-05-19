def remove_every_other(my_list):
    i = 0
    ret = []
    while my_list != []:
        if i % 2 == 0:
            ret.append(my_list.pop(0))
        else:
            my_list.pop(0)
        i+=1
    return ret
    pass


def remove_every_other(my_list):
    return my_list[::2]
