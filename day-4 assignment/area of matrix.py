def fill_positions(matrix_, symbol, positions):
    for position in positions:
        matrix_[position[0]][position[1]] += symbol


def common_area(matrix_, symbols):
    count = 0
    area_unit = 1
    for row in range(0, len(matrix_)):
        for column in range(0, len(matrix_[row])):
            if matrix_[row][column].strip() == symbols:
                count += 1

    return count * area_unit


number_of_rows = 3 #int(input("Enter the rows"))
number_of_columns = 3 #int(input("Enter the columns"))
matrix = [[" " for i in range(0, number_of_columns)] for y in range(0, number_of_rows)]

fill_positions(matrix, "*", [(1, 2), (0, 0)])
fill_positions(matrix, "#", [(1, 2), (0, 1)])
print(common_area(matrix, "*#"))
