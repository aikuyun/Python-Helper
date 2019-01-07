
# Python 3 has only one integer type, int().
import math
from filecmp import cmp
from random import randrange, shuffle


def test():
    num1 = 5555555555
    print(type(num1))
    print(abs(-10))
    # 向上取整
    print(math.ceil(4.1))
    print(cmp(1, 2))
    print(math.exp(2))
    # 向下取整
    print(math.floor(4.1))

    # 取最大值
    print(max(1, 2, 3))

    # 取最小值
    print(min(1, 2, 3))

    # 取平方根
    print(math.sqrt(4))

    # 随机数,[start] stop [step]
    print(randrange(200))

    # 随机排序
    list1 = [1, 2, 3, 4, 5]
    print(shuffle(list1))


if __name__ == "__main__":
    test()
