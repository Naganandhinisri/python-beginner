while True:
   matrix = [[]]
   matrix = [[0 for j in range(3)] for i in range(3)]
   print (matrix)


   i = int(input("enter the number of rows"))
   j = int(input("enter the number of columns"))
   matrix[i][j] = "*"
   print(matrix)
