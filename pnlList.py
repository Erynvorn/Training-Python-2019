def profitLoss(records):
    cost = 0
    sellPrice = 0
    for i in range(len(records)):
        cost += records[i][0] / (1+records[i][1]/100)
        sellPrice += records[i][0]
    return round(sellPrice - cost,2)
    # coding here
