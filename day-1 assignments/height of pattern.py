rows = input("enter the number of rows")
rows = int(rows)
for i in range(0,rows):
    for j in range(0,i+1):
        print(" * " , end = ' ')
    print("\r")

print("height=number of rows",rows)

rows = input("enter the number of rows")
value = count(rows)
print("{}{}".format(i, j)for j in range(1, i+1) for i in range(0, rows))
