list = [1,0,0,0,2,6,3,-4,-5]
pos_count = 0
neg_count = 0
zero = 0
for num in list:
    if num == 0:
       zero +=1
    elif num<0:
       neg_count += 1
    else:
       pos_count += 1
print("zero number",zero)
print("negative number", neg_count)
print("positive number", pos_count)