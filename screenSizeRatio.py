def find_screen_height(width, ratio): 
    mid = ratio.find(':')
    wr = int(ratio[0:mid])
    hr = int(ratio[mid+1:len(ratio)])
    h = int(width * hr / wr)
    return str(width) + 'x' + str(h)

# ratio is '4:3' string
