# -*- coding:UTF-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = (i for i in L1 if isinstance(i, str))
print(L2)
