X = [[12,7,3],[4 ,5,6],[7 ,8,9]]

Y = [[5,8,1], [6,7,3], [4,5,9]]

result = [[0,0,0],[0,0,0],[0,0,0]]
print(len(X))
for i in range(0,len(X)):
    for j in range(len(X)):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)

