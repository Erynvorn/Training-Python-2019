tableData = [['apples','oranges','cherries','banana'],
            ['Alice','Bob', ' Carol', 'David'],
            ['dogs','cats','moose','goose']]

print(tableData[0])
print(tableData[0][0])
print(len(tableData))
print(len(tableData[0]))
max =[]
for i in range(len(tableData)):
    max.append(0)
    for j in range(len(tableData[i])):
        if max[i] < len(tableData[i][j]):
            max[i] = len(tableData[i][j])
print(max)
ret = ''
retu=''
for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        ret = tableData[j][i]
        ret = ret.rjust(max[j]+1)
        retu+=ret
    retu += '\n'
  #  print('\n')
print(retu)


