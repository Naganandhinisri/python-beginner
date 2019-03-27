def factorial():
    n = 6
    fact = 1
    for number in range(1,n+1):
        fact = fact * number

    digit = fact
    print(str(digit))
    # array = []
    # for i in str(digit):
    #     array.append(int(i))
    array = [int(i) for i in str(digit)]
    return(sum(array))

print(factorial())