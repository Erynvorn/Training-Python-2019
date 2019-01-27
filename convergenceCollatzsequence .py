#Convergence Collatz sequence
count=0
maxn=1
for i in range(2,1001):
    numb = i
    while numb != 1:
        count += 1
        if numb % 2 == 0:
            numb = numb // 2
        else:
            numb = numb * 3 + 1
    #maxn=max(maxn,count)
    print(i, ' ', count)
    count = 0
print(maxn)
