def mystery_add(number):
    sum = 1
    for i  in range(1,number):
        if i<6:
            for k in range(1,number):
                sum *=2                   # num=4: sum=2^(n^2)
        else:                             #num=6: sum=2^(5*num)*5^1
            if i<10:                       #num=10: sum=2^(5*num)*(5*4)*(3^1)
                sum *=5
            else:
                sum *=3
    print(sum)
    return sum

mystery_add(5)
