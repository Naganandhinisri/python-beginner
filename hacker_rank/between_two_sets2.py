def getTotalX(a, b):
    if n>1:
        multiples_n = [a[1]]
        factors = []
        count = 0
        for j in range(1, n):
            for i in range(0, m):
                multiples = (a[0] + i) * a[j]
                multiples_n.append(multiples)
            print(multiples_n)
        for i in range(0, len(multiples_n)):
            if (b[0] % multiples_n[i]) == 0:
                factors.append(multiples_n[i])
                count += 1
        return count
    else:
        multiples_n = []
        factors = []
        count = 0
        for j in range(0,n):
            for i in range(0,m):
                multiples = (a[0] + i) * a[j]
                multiples_n.append(multiples)
            print(multiples_n)
            for i in range(0, len(multiples_n)):
                if (b[0] % multiples_n[i]) == 0:
                    factors.append(multiples_n[i])
                    count += 1
            return count


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(total)