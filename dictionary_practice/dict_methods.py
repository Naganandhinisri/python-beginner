my_dict = {'zumba': 220, 'sri': 30}
dict_keys = list(my_dict.keys())
dict_keys.sort()
for element in dict_keys:
    print(":".join((element, str(my_dict[element]))))


print("string:%s" %str(my_dict))


# user_input = input("enter key and value seperated by ::")
# key,value = user_input.split(':')
# print(key)

#
# the_list = {len(my_dic[i]):i for i in my_dic.keys()}
# print(the_list)


# ct = {}
# for key, dif_k in dictsample.iteritems():
#     for k, v in dif_k.iteritems():
#         dictcounter = k.count(k)
#         ct.update({key:dictcounter})