# G = 442785743657365328
# # num = 123
# lst = magic(G)
# print(lst)
# P = [2,3,3]
#
# def gridSearch(G, P):
#     for i in range(0, len(G)):
#         for j in range(0,len(P)):
#             if G[i] == P[j]:
#                 print( 'YES')
#             else:
#                 print( 'NO')
#
#
# gridSearch(G,P)
# a = 123456
# b = str(a)
# c = []
# for digit in b:
#     c.append (int(digit))
# print(c)
#
# pattern = 1236
# string_pattern = str(pattern)
# c_pattern = []
# for element in string_pattern:
#     c_pattern.append (int(element))
#
# print (c_pattern)
# for i in range(10):
#     if c_pattern[i] == c[i]:
#         print('yes')
#     else:
#         print('no') for j in range(c):
#         for i in range(r):
#             if P[i][j] in G[i][j]
#             return 'true'


fruits = ["apple", "orange", "pears"]
substr = ["a","p"]
index_str = []
for j in range(0,len(substr)):
    for i in range(j,len(fruits)):
        if substr[j] in fruits[i]:
            index_str.append(fruits[i])
print(index_str)

