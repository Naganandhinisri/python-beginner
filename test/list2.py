list_ = [1, 1, 1, 2, 3]
n = len(list_)
for i in range(0, n):
    if list_[0] == list_[1]:
        del list_[0]
        print(list_)

