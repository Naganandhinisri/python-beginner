a =  60

while True:
    b = int(input("enter the number"))
    if  a==b:
        print("number is correct")
        break
    elif b>a:
         print("number is high ..reduce the number")
    elif b<a:
         print("number is low..increase the number")
    else:
        print("good luck")