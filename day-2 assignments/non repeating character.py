string = input("enter the string")
number = len(string)
def non_repeatation():
    for i in range(0,number):
        if i == 0:
            if string[i] != string[i+1]:
                print(string[i])
                break

        elif i == number+1:
            if string[i] != string[i-1]:
                print(string[i])
                break

        else:
            if string[i] != string[i+1] and string[i] != string[i-1]:
                print(string[i])


non_repeatation()

