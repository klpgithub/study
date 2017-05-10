# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : klp

# list
l = [1, 2, 3, 4, 5]
l.insert(0, 'a')
print(l.pop())
l[1] = 'b'
print(l)
print(len(l))

# tuple  不可变
t = (1, 2, 3, 4)
print(t[0])
tt = (1,)
print(tt)
ttt = (1)
print(ttt)
print(type(ttt))

# tuple里边的list是可变的...引用是不变的
t = (1, 2, ['a', 'b'])
t[2][0] = 'c'
print(t)

print(int('55555'))  # 类型转换
print(str(8888888))

# dict  --> map
d = {1: 1, 2: 2}
print(type(d))
d.pop(1)  # 删除一个元素
print(d)
print(2 in d)
print(d.get(4, 5))
d['a'] = '111'
print(d[2])

# set
s = {1, 2, 3, 4, 5}
print(type(s))
s = set([1, 2, 3, 4])
print(s.add(5))
s.remove(1)
print(s)
ss = {1, 2}
print(s & ss)
print(s | ss)


