list = [1,0,0,0,2,6,3,-4,-5]
pos_count,neg_count,zero_count=0,0,0
for num in list:
    if num >=0:
         pos_count += 1
    elif num ==0:
         zero_count == 0
    else:
         neg_count -= 1
print("positive number",pos_count)
print("negative number",neg_count)
print("zero number in list",zero_count)