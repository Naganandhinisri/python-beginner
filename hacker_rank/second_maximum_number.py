def second_maximum_number(list1):
    # list1 = set(list1)
    biggest = max(list1)
    list1.remove(biggest)
    second_largest_number = max(list1)
    while second_largest_number == biggest:
        list1.remove(second_largest_number)
        second_largest_number = max(list1)
    return second_largest_number



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(second_maximum_number(list(arr)))
