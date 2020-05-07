def fillable(stock, merch, n):
    if merch in stock:
        return stock[merch] >= n
    else:
        return False
    # Your code goes here.

    #check dictoniary content

def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n
