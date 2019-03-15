# -*- coding:UTF-8 -*-
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n += 1
    if n == 10:
        break