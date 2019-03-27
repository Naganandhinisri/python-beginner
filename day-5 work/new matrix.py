no_of_rows = int(input("enter the rows"))
no_of_columns = int(input("enter the columns"))
a = [[0]*2]*3
print(a)

for i in range(0,no_of_rows):
    for j in range(0,no_of_columns):
        print(i,j)
        a[i][j] = j
