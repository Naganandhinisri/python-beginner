def cube_fibonacci():
    array = []
    n = 6
    number1 = 0
    number2 = 1
    count = 0
    while count < n+1:
        array.append(number1)
        add = number1 + number2
        number1 = number2
        number2 = add
        count += 1
    print(array)
    list_array = []
    for i in array:
        list_array.append(i*i*i)
    return sum(list_array)


print(cube_fibonacci())