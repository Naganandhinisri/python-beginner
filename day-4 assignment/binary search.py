list = [28, 26, 93, 17, 77, 31,44]
n = len(list)

def binary_search(list):
    for i in range(1, n):
        searchelement = 93
        lowerIndex = 0
        higherIndex = n-1
        middleelement = (lowerIndex + higherIndex)/2
        if searchelement == middleelement:
            print("number is found")
            break
        elif searchelement < middleelement:
             higherIndex = middleelement-1
             print("number is found")
        else:
             lowerIndex = middleelement+1
             print("number is found")


print(binary_search(list))