m1 = [[2,3,4],[5,6,7]]
m2 = [[1,2,3],[4,5,6]]
res = [[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        res[i][j] = m1[i][j] + m2[i][j]
for x in res:
    print(x)