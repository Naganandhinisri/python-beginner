rows = int(input("enter the number of rows"))

def function_symbol1():
    for i in range(0, rows+1):
        for j in range(0, i + 1):
            print(" * ", end=' ')
        print()

def function_symbol2():

    for i in range(rows,0,-1): #starting from 5 and decreasing 1 value upto zero
         for j in range(0, i ):
            print(" * ", end=' ')
         print()

function_symbol1()
function_symbol2()

