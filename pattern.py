n = 5
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=' ')
    print('\r')

print("")
print("")
print("")

for i in range(0, n):
    for j in range(i + 1, n + 1):
        print("*", end=' ')
    print('\r')

print('')
print('')
print('')

for row in range(1, n + 1):
    for space in range(1, n - row + 1):
        print(" ", end='')
    for star in range(1, row + 1):
        print("*", end='')
    print("\r")

print('')
print('')
print('')

for row in range(0, n+1):
    for space in range(0, n-row):
        print(" ", end='')

    for star in range(0, row):
        print("*" ," ", end='')
    print("\r")
i = 1
for row in range(0,n+1):
    for number in range(0,row):
        print(i," ",end='')
        i +=1
    print('\r')