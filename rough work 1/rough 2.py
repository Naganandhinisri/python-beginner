a = str(input("enter the string"))
size = len(a)
for i in range(0,size-1):
    a = a[1:] + a[0]
    print(a)