import random

arr = []
arr1 = []
for i in range (10000):
    arr.append(i)
print(arr)

for j in arr:
    count = 0

    for k in range (j):
        if j % (k+1) == 0:
            count = count + 1
    if count == 2:
        arr1.append(j)
print(arr1)

