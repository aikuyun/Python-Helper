def test():
    print(4 // 3.1)
    print(5 ** 2)
    print(2 != 3)

    # 与：如果两个都为1，则为 1 ，否则为 0
    print(2 & 3)

    # 或：如果有一个为1 ，则为1，否则为 0

    print(2 | 3)

    list1 = ["a", "c", 2, 3]

    print(4 in list1)

    print("a" in list1)

    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]

    # 比较内容
    print(a is b)

    # 比较地址
    print(a == b)


if __name__ == "__main__":
    test()
