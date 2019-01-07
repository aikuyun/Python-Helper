
def test():
    str1 = "str"
    print("双引号"+str1)

    str2 = 'str'
    print("单引号"+str2)

    # 保留原来的格式
    str3 = """
        select * from 
        table1 where id = 1
        and name in ("a","b")
    """

    print("三引号"+str3)

    # 替换

    print(str1.replace("s", "t"))

    # 切分,返回数组

    print(str2.split("t"))

    # 查找，返回下标
    print(str2.find("t"))

    # 字符串传参，使用 key-vale 格式，不用考虑顺序，推荐使用
    print("my name is '{name}' and i am from '{country}'".format(name="tsl", country="china"))

    # 截取范围

    str4 = "Iloveyou"
    print(str4[1])
    print(str4[1:3])
    print(str4[:2])
    print(str4[2:])
    print(str4[-2:5])


if __name__ == "__main__":
    test()
