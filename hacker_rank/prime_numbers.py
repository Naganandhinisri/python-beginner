lower_limit = 600
upper_limit = 700
for num in range(lower_limit, upper_limit + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
