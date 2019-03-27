array = [1, 3, 7, 4, 5, 6]
for i in range(0,len(array)-1):
    for j in range(i,len(array)):
        addition = array[i]+array[j]
        if addition == 10 and i != j:
            print(array[i], array[j])

