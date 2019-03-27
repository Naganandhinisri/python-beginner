def tidy_number(num):
    number = list(str(num))
    sorted_numbers = sorted(number)
    if number == sorted_numbers:
        return 'YES'
    else:
        return 'NO'


input1=1234
input2=1324
print(tidy_number(input1))
print(tidy_number(input2))

