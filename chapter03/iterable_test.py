# -*- coding:UTF-8 -*-
def findMinAndMax(L):
    if len(L) < 2:
        return tuple(L)
    else:
        min, max = L[:2]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return min, max


print(findMinAndMax([1, 2, 3, 4, 5]))
