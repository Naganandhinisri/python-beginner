array = [73, 67, 38, 33]
for i in range(0,len(array)):
    if array[i] >= 38:
        if array[i]%5 ==  3:
            array[i] +=2


        elif array[i] % 5 == 4:
            array[i] +=1

    print(array[i])

