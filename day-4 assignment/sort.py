list = [28, 26, 93, 17, 77, 31,44]
n = len(list)

def insertion_sort(list):
    for i in range(1, n):
        currentvalue = list[i]
        position = i
        while position > 0 and list[position-1] <list[i]:
            list[position] = list[position-1]
            position = position-1
        list[position] = currentvalue

insertion_sort(list)
print(list)