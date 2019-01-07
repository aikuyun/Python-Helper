

"""继承"""


class Parent:
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')


class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')

    def __add__(self, other):
        return self.parentAttr + other.parentAttr


if __name__ == '__main__':
    c = Child()  # 实例化子类
    c.childMethod()  # 调用子类的方法

    c.parentMethod()  # 调用父类方法
    setattr(c, "parentAttr", 200) # 设置父类属性值
    print(getattr(c, "parentAttr")) # 获取父类属性值

    # python中没有重载，只有运算符重载
    c2 = Child()
    # print c + c2
    # print c.__add__(c2)

