
# 元组的特点是：定长、内容不可变、类型多样


def test():
    # 如果想要定义有一个元素的 tuple, 要加上逗号
    tuple1 = (1,)
    print(tuple1)

    # "可变" 的 tuple
    t = ('a', 'b', ['A', 'B'])

    print(t[2])

    t[2].append('C')

    print(t[2])

    # tuple 的元素指向是不可变的，但是指向的内容如果是一个 list , list是可变的。


if __name__ == "__main__":
    test()