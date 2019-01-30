print("enter 'x' for exit")
string = input("enter the string")
if  string == 'x':
    print('exit')
else:
    char = input("enter the letter to be count from above string")
    value = string.count(char)
    print('total = ', value)