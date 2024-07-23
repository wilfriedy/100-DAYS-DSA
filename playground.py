mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

k = 3
total = [(sum(s), i) for i, s in enumerate(mat)]

total.sort(key= lambda x : x[0])
# for i in range(k):
#     print(total[i][1])

print([i[1] for i in total[:k]])