n = 5
m = 5
matrix = []
matrix = [[11,2,4], [4,5,6], [10, 8, -12]]

i = 1
# for rows in range(0, 5):
#     matrix.append([])
#     for column in range(1, 6):
#         matrix[rows].append(i)
#         i += 1
print(matrix)
n = len(matrix)
sum_first_diagonal = sum(matrix[j][j] for j in range(n))
print(sum_first_diagonal)
sum_second_diagonal = sum(matrix[row][n-row-1] for row in range(n)) #notes
print(sum_second_diagonal)
print(abs(sum_first_diagonal - sum_second_diagonal))