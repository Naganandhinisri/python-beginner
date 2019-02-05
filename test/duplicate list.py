list = [1, 1, 1, 2, 3]
n = len(list)
for i in range(0,n):
    if list[0] == list[1]:
        del list[0]
        print(list)
