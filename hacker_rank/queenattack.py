n = 100000
r_q = 4187
c_q = 5068
# obstacles = []
# obstacles = [[1, 2], [1, 3], [1, 1], [3, 4], [4, 1], [5, 2], [4, 3], [5, 3]]
obstacles = []


def minByRow(list):
    return min(list, key=lambda obstacle: obstacle[0])


def minByColumn(list):
    return min(list, key=lambda obstacle: obstacle[1])


def maxByRow(list):
    return max(list, key=lambda obstacle: obstacle[0])


def maxByColumn(list):
    return max(list, key=lambda obstacle: obstacle[1])


def diffByRow(obstacle, r_q):
    return abs(r_q - obstacle[0]) - 1


def diffByColumn(obstacle, c_q):
    return abs(c_q - obstacle[1]) - 1

def isDiagonal(obstacle, r_q, c_q):
    return abs(obstacle[0] - r_q) == abs(obstacle[1] - c_q)


def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles_in_upward_dir = list(filter(lambda obstacle: obstacle[1] == c_q and obstacle[0] > r_q, obstacles))
    obstacles_in_downward_dir = list(filter(lambda obstacle: obstacle[1] == c_q and obstacle[0] < r_q, obstacles))
    obstacles_in_left_dir = list(filter(lambda obstacle: obstacle[1] < c_q and obstacle[0] == r_q, obstacles))
    obstacles_in_right_dir = list(filter(lambda obstacle: obstacle[1] > c_q and obstacle[0] == r_q, obstacles))
    obstacles_in_bottomright_dir = list(
        filter(lambda obstacle: obstacle[1] > c_q and obstacle[0] < r_q and isDiagonal(obstacle, r_q, c_q),
               obstacles))
    obstacles_in_topleft_dir = list(
        filter(lambda obstacle: obstacle[1] < c_q and obstacle[0] > r_q and isDiagonal(obstacle, r_q, c_q),
               obstacles))
    obstacles_in_topright_dir = list(
        filter(lambda obstacle: obstacle[1] > c_q and obstacle[0] > r_q and isDiagonal(obstacle, r_q, c_q),
               obstacles))
    obstacles_in_bottomleft_dir = list(
        filter(lambda obstacle: obstacle[1] < c_q and obstacle[0] < r_q and isDiagonal(obstacle, r_q, c_q),
               obstacles))
    closest_in_upward_dir = minByRow(obstacles_in_upward_dir) if len(obstacles_in_upward_dir) > 0 else None
    closest_in_downward_dir = maxByRow(obstacles_in_downward_dir) if len(obstacles_in_downward_dir) > 0 else None
    closest_in_left_dir = maxByColumn(obstacles_in_left_dir) if len(obstacles_in_left_dir) > 0 else None
    closest_in_right_dir = minByColumn(obstacles_in_right_dir) if len(obstacles_in_right_dir) > 0 else None
    closest_in_bottomright_dir = maxByRow(obstacles_in_bottomright_dir) if len(obstacles_in_bottomright_dir) > 0 else None
    closest_in_top_left_dir = minByRow(obstacles_in_topleft_dir) if len(obstacles_in_topleft_dir) > 0 else None
    closest_in_topright_dir = minByColumn(obstacles_in_topright_dir) if len(obstacles_in_topright_dir) > 0 else None
    closest_in_bottomleft_dir = maxByRow(obstacles_in_bottomleft_dir) if len(obstacles_in_bottomleft_dir) > 0 else None
    count = 0
    if closest_in_upward_dir is not None:
        count += diffByRow(closest_in_upward_dir, r_q)
    else:
        count += (n - r_q)
    if closest_in_downward_dir is not None:
        count += diffByRow(closest_in_downward_dir, r_q)
    else:
        count += (r_q - 1)
    if closest_in_right_dir is not None:
        count += diffByColumn(closest_in_right_dir, c_q)
    else:
        count += (n - c_q)
    if closest_in_left_dir is not None:
        count += diffByColumn(closest_in_left_dir, c_q)
    else:
        count += (c_q - 1)
    if closest_in_bottomright_dir is not None:
        count += diffByRow(closest_in_bottomright_dir, r_q)
    else:
        lastRow = r_q - (n - c_q)
        count += (r_q - lastRow)
    if closest_in_top_left_dir is not None:
        count += diffByRow(closest_in_top_left_dir, r_q)
    else:
        lastCol = c_q - (n - r_q)
        count += (c_q - lastCol)
    if closest_in_topright_dir is not None:
        count += diffByRow(closest_in_topright_dir, r_q)
    else:
        lastCol = c_q + (n - r_q)
        count += (lastCol - c_q)
    if closest_in_bottomleft_dir is not None:
        count += diffByRow(closest_in_bottomleft_dir, r_q)
    else:
        lastRow = r_q - (c_q - 1)
        count += (r_q - lastRow)
    return count

#
# def queensAttack(n, k, r_q, c_q, obstacles):
#     count = 0
#     matrix = []
#     for row in range(0, n):
#         rows = []
#         for column in range(0, n):
#             rows.append(0)
#         matrix.append(rows)
#     for obstacle in obstacles:
#         row = obstacle[0] - 1
#         column = obstacle[1] - 1
#         matrix[row][column] = 1
#
#     # print("Upwards:")
#     for row in range(r_q + 1, n + 1):
#         value = matrix[row - 1][c_q - 1]
#         if value == 0:
#             count += 1
#             # print(row, c_q)
#         else:
#             break
#
#     # print("Downwards:")
#     for row in range(r_q - 1, 0, -1):
#         value = matrix[row - 1][c_q - 1]
#         if value == 0:
#             count += 1
#             # print(row, c_q)
#         else:
#             break
#
#     # print("To Left:")
#     for column in range(c_q - 1, 0, -1):
#         value = matrix[r_q - 1][column - 1]
#         if value == 0:
#             count += 1
#             # print(r_q, column)
#         else:
#             break
#
#     # print("To right:")
#     for column in range(c_q + 1, n + 1):
#         value = matrix[r_q - 1][column - 1]
#         if value == 0:
#             count += 1
#             # print(r_q, column)
#         else:
#             break
#
#     # print("Towards bottom right:")
#     for row, column in zip(range(r_q - 1, 0, -1), range(c_q + 1, n + 1)):
#         value = matrix[row - 1][column - 1]
#         if value == 0:
#             count += 1
#             # print(row, column)
#         else:
#             break
#
#     # print("Towards top left:")
#     for row, column in zip(range(r_q + 1, n + 1), range(c_q - 1, 0, -1)):
#         value = matrix[row - 1][column - 1]
#         if value == 0:
#             count += 1
#             # print(row, column)
#         else:
#             break
#
#     # print("Towards top right:")
#     for row, column in zip(range(r_q + 1, n + 1), range(c_q + 1, n + 1)):
#         value = matrix[row - 1][column - 1]
#         if value == 0:
#             count += 1
#             # print(row, column)
#         else:
#             break
#
#     # print("Towards bottom left:")
#     for row, column in zip(range(r_q - 1, 0, -1), range(c_q - 1, 0, -1)):
#         value = matrix[row - 1][column - 1]
#         if value == 0:
#             count += 1
#             # print(row, column)
#         else:
#             break
#     # print(count)
#
#     return count


print(queensAttack(n, -1, r_q, c_q, obstacles))
# print(queensAttack(n, -1, r_q, c_q, obstacles))
