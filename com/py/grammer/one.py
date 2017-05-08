# 函数定义/
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 定义一个什么事也不做的空函数
def nop():
    pass


if __name__ == '__main__':
    # sum = 0
    # for x in list(range(1000)) :
    #     sum = sum + x
    #
    # print(sum)

    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2

    print(sum)
    print(myabs(-20))
