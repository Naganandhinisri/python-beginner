def staircase(n):
    for row in range(1,n+1):
        for space in range(0,n-row):
            print(" ",end='')
        for ass in range(0,row):
            print("#",end='')
        print('\r')
    return n

if __name__ == '__main__':
    n = int(input())

    staircase(n)
