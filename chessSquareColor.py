def square_color(file, rank):
    print(file,rank)
    if (file in 'aceg' and rank % 2 == 1) or (file in 'bdfh' and rank % 2 == 0):
        return 'black' 
    else:
        return 'white'

