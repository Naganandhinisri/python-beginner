array1 = "2017,11,12"
array2 = "2017,11,19"
new1 = array1.split(',')
n=len(new1)
new2 = array2.split(',')
print(abs(int(new1[n-1])-int(new2[2])))