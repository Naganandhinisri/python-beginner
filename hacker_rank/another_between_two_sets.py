n = 2
m = 3
a = [2, 4]
b = [16, 32, 96]


# factors1 = []
# for j in b:
#     for i in range(1, j+1):
#         if j % i == 0:
#             factors1.append(i)
# print(factors1)


# def factorise(number):
#     factors = []
#     half = number / 2
#     for i in range(1, half):
#         if number % i == 0:
#             factors.append(i)
#             factors.append(number / i)
#     return factors
#
#
# b_set_factors = []
# for i in range(0, len(b)):
#     factors_of_i = factorise(b[i])
#     b_set_factors.append(factors_of_i)
#
# common_factors= []
# min_len = len(b_set_factors[0])
# for i in range(1, len(b_set_factors)):
#     len_of_ith_list = len(b_set_factors[i])
#     if len_of_ith_list < min_len:
#         min_len = len_of_ith_list
# 

factors = []
for i in range(1, 17):
    j = 0
    if ((b[0] % i == 0) and (b[j - 2] % i == 0) and (b[j - 1] % i == 0)):
        factors.append(i)
print(factors)

factors0 = []
for i in range(1, 2):
    if factors[0] % i == 0:
        factors0.append(i)
print(factors0)

factors1 = []
for i in range(1, 3):
    if factors[1] % i == 0:
        factors1.append(i)
print(factors1)

factors2 = []
for i in range(1, 5):
    if factors[2] % i == 0:
        factors2.append(i)
print(factors2)

factors3 = []
for i in range(1, 9):
    if factors[3] % i == 0:
        factors3.append(i)
print(factors3)

factors4 = []
for i in range(1, 17):
    if factors[4] % i == 0:
        factors4.append(i)
print(factors4)
