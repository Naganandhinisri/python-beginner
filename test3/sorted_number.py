def sort_numbers():
    number = "687"
    sorted_number = ''.join(sorted(number))
    rev_sorted_number = ''.join(reversed(number))

    if number == sorted_number:
        return 'Ascending Order'
    elif sorted_number == rev_sorted_number:
        return 'descending order'
    else:
        return 'neither'


print(sort_numbers())
