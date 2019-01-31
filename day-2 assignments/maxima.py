a=[]
count = int(input("enter the counts: "))
for  i in range(1, count+1):
    number = int(input("enter the element:"))
    a.append(number)
a.sort()
print("maximum number is :", a[count-1])


