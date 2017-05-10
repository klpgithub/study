# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : klp
import os
from typing import Iterable

L = []
n = 1
while n < 100:
    L.append(n)
    n = n + 2
print(len(L))

# 切片
print(L)
print(L[3:5])  # L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3 如果第一个索引是0，还可以省略
# 快速复制一个list
print(L[:])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
s = 'asdfghjk'
print(s[0:3])  # 相当于java中的substring 字符串截取操作在python中用切片

# 迭代
d = {'a': 1, 'b': 2, 'c': '3'}
for x in d:
    print(x)

print(isinstance('abcd', Iterable))

'''
    最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
    Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
'''
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y, z in [(1, 1, 1), (2, 2, 1), (3, 3, 3)]:  # 简直变态...
    print(x, y, z)

# 列表生成式

print(list(range(0, 10)))
print([x * x for x in range(0, 10)])  # 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

print([x * x for x in range(0, 10) if x % 2 != 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'CDE'])

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
print([d for d in os.listdir('.')])

# 列表生成式也可以使用两个变量来生成list
d = {'a': '1', 'b': '2', 'c': '3'}
print([k + '=' + v for k, v in d.items()])

# 把一个list中所有的字符串变成小写
L = ['HELLO', 'PYTHON', 'KLP']

print([s.lower() for s in L])

# 生成器
