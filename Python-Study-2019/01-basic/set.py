# set 是一个无序的集合，可以做交集和并集运算。


def test():
    s = set([1, 2, 3, 4])
    s2 = set([2, 3])
    print(s)
    # 添加元素 add()
    s.add(5)
    print(s)
    # 删除元素 remove()
    s.remove(5)
    print(s)
    # 交集
    print(s & s2)
    # 并集
    print(s | s2)


if __name__ == "__main__":
    test()
