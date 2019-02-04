def create_dictionary():
    num = int(input("enter the number"))
    my_dic = {i: i*i for i in range(1, num+1)}
    print(my_dic)

create_dictionary()    