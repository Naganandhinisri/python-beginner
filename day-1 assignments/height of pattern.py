rows = input("enter the number of rows")
rows = int(rows)
for i in range(0,rows):
    for j in range(0,i+1):
        print(" * " , end = ' ')
    print("\r")

print("height=number of rows",rows)