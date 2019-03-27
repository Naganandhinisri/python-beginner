n = 2
m = 2
array_n = [2, 6]
array_m = [24, 36]
multiples_n = [array_n[1]]
factors = []
for j in range(1, n):
    for i in range(0, m):
        multiples = (array_n[0]+i) * array_n[j]
        multiples_n.append(multiples)
    print(multiples_n)
for i in range(0, len(multiples_n)):
    if (array_m[0] % multiples_n[i]) == 0:
        factors.append(multiples_n[i])
print(len(factors))
