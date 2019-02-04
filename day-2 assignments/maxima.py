def find_maximum(list_):
    maximum = list_[0]
    for number in list_:
        if number>= maximum:
            maximum = number
    return maximum

def get_input():
    list_ = []
    size_ = int(input("Enter the size of the list"))
    for i in range(0, size_):
        number = int(input())
        list_.append(number)
    return list_

print(find_maximum(get_input()))
