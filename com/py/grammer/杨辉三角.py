# -*- coding : utf-8 -*-
# !/usr/bin/env python


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


def triangles2():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]


for i in triangles():
    if len(i) < 10:
        print(i)
    else:
        break
'''杨辉三角
'''
print('--------------------------------------------------------------------')

for i in triangles2():
    if len(i) < 10:
        print(i)
    else:
        break
