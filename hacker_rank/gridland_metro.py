n = 5
m = 4
tracks = [[1, 2, 3], [3, 1, 4], [4, 1, 1]]

def gridlandMetro(n, m, k, tracks):
    matrix = []
    for row_number in range(0, n):
        row = []
        for column in range(0, m):
            row.append(0)
        # row = [0, 0, 0, 0]
        matrix.append(row)
    for track in tracks:
        row = track[0] - 1
        startingCol = track[1]
        endingCol = track[2]
        for column in range(startingCol - 1, endingCol):
            matrix[row][column] = 1
    count = 0
    for row in matrix:
        for element in row:
            if element == 0:
                count +=1
    return (count)



if __name__ == '__main__':

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)
    print(result)
