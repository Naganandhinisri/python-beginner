x1 = int(input("enter the x1 number"))
v1 = int(input("enter the v1 number"))
x2 = int(input("enter the x2 number"))
v2 = int(input("enter the v2 number"))


if (v2 < v1) and ((x2 - x1) % (v2-v1)) == 0:
    print('true')

else:
    print('false')
