# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : klp


# 函数
# print(abs(-100))
#
# print(bool(''))
# print(bool('1'))
# print(bool(0))
# a = abs
# print(a(-99))


# 自定义函数
def enroll(name, age):
    print("name: ", name)
    print("age :", age)


enroll('张三', 20)


# 默认参数  -- 注意默认参数如果为可变参数 如list会出问题..
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(8))
print(power(8, 3))


# 可变参数
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum


print(calc(1, 2, 3))
l = [1, 2, 3]
print(calc(*l))  # *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


# 关键字参数
def person(name, age, **kb):
    print(name, age, kb)


person('zs', 22)
person("李四", 20, sex='男')
d = {"city": 'beijing', 'job': "coding ..."}
person('klp', 25, **d)  # 调用已有的dict


# 命名关键字参数

def p(name, age, *, city, job):
    print(name, age, city, job)


p('zs', 20, city='bj', job='coding')


def p(name, age, *, city='BJ', job):  # 命名关键参数 默认值
    print(name, age, city, job)


p('aa', 33, job='hh')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def stu(name, age, *args, sch, sex='NV'):
    print(name, age, args, sch, sex)


stu('aa', 12, 1, 2, 3, sch='aaa')

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
