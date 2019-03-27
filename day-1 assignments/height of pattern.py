rows = int(input("enter the number of rows"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*", end='')
    print("")

print("height=number of rows",rows)

# rows = input("enter the number of rows")
# height = rows
# print("{}{}".format(i, j)for j in range(1, i+1) for i in range(0, rows))

