# -*- coding:UTF-8 -*-
import os

# fpath = os.getcwd() + r'/write_test.py'
fpath = os.getcwd() + r'/test.txt'

f1 = open(fpath, 'w')
f1.write('Hello world1\n')
# f2 = open(fpath, 'w')
# f2.write('Hello world2\n')
f1.close()
f1 = open(fpath, 'w')
f1.write('Hello world3\n')

f1.close()
# f2.close()

with open(fpath, 'r') as f3:
    text = f3.read()
    print(text)


os.environ.get()
import shutil
