# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# Boys = {'Tim': 18,'Charlie':12,'Robert':25}
# Girls = {'Tiffany':22}
# studentX=Boys.copy()
# studentY=Girls.copy()
# print(studentX)
# print(studentY)


# Dicts = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# Dict.update({"Sarah":9})
# print (Dicts)
# print(Dicts.keys())


my_dict = {'nandhini':20,'sri':30}
girls = {'nandhini':20}
for elements in list(my_dict.keys()):
    if elements in list(girls.keys()):
        print ('true')
    else:
        print('false')
print(my_dict)
print(my_dict.items())
print(list(my_dict.items()))
print(list(my_dict))
