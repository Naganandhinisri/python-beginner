arr = [1, 1, 0, -1, -1]
length = len(arr)
positive_count = 0
negative_count = 0
zero_count = 0
for number in arr:
    if number == 0:
        zero_count +=1
    elif number >0:
        positive_count +=1
    else :
        negative_count +=1


positive_fraction_number = positive_count/length
negative_fraction_number = negative_count/length
zero_fraction_number = zero_count/length


print(positive_fraction_number)
print(negative_fraction_number)
print(zero_fraction_number)