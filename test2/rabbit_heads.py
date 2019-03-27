def count_animals():
    total_heads = 2
    total_legs = 4
    for total_hens in range(0, total_heads + 1):
        total_rabbit = total_heads - total_hens
        if (2 * total_hens) + (4 * total_rabbit) == total_legs:
            print(total_hens, total_rabbit)


count_animals()
