# G = [[1,2,4],[3,4,5],[6,7,8]]
# P = [[3,4,5],[6,7,8]]
# r = 3
# c = 3
# def gridSearch(G, P):
#     for j in range(c):
#         for i in range(r):
#             if P[i][j] in G[i][j]:
#                 print('yes')
# gridSearch(G,P)

a = [123,456,789]
b = [123,454,789]
for ele_a,ele_b in zip(a,b):
     if ele_a == ele_b:
         print('true')
     else:
         print('false')

#
# a_string = [list(str(element)) for element in a]
# print(a_string)
# b_string = [list(str(element)) for element in b]
# print(b_string)
#
# for ele_a,ele_b in zip(a_string,b_string):
#      if ele_a == ele_b:
#          print('true')
#      else:
#          print('false')
