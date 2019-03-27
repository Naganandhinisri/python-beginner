# def divisibleSumPairs():
n = 6
k = 3
ar = [1,3,2,6,1,2]
count = 0
for i in range(0,n):
    for j in range(i+1,n):
        if (ar[i]+ar[j]) % k == 0:
            count = count+1
print(count)

# print(divisibleSumPairs())

# if __name__ == '__main__':
#
#     nk = input().split()
#
#     n = int(nk[0])
#
#     k = int(nk[1])
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = divisibleSumPairs(n, k, ar)
#     print(result)
