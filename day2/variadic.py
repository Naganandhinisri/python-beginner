def add_numbers(*args):
    add = 0
    for num in args:
        add = add + num
    return add


print(add_numbers(10,11,12))