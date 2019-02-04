list = [4, 2, 1, 7, 3, 6]
def quicksort(list,lowIndex,highIndex):
    if (highIndex - lowIndex) > 0:
        p = partition(list,lowIndex,highIndex)
        quicksort(list,lowIndex ,p-1)
        quicksort(list, p+1, highIndex)


def partition(list, lowIndex, highIndex):
    divider = lowIndex
    pivot = highIndex

    for i in range (lowIndex, highIndex):
     if list < list(pivot):
        list[i],list[divider] = list[divider],list[i]
        divider += 1
    list[pivot], list[divider] = list[divider], list[pivot]
    return divider



quicksort(list, 0, 5)
print(list)
