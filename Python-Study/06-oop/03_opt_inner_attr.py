"""
内置类属性
"""


class InnerCls:

    '姓名'
    name = ""

    def __init__(self, name):
        self.name = name

        print("InnerCls.__doc__:", InnerCls.__doc__)
        print("InnerCls.__name__:", InnerCls.__name__)
        print("InnerCls.__module__:", InnerCls.__module__)
        print("InnerCls.__bases__:", InnerCls.__bases__)
        print("InnerCls.__dict__:", InnerCls.__dict__)


if __name__ == '__main__':
    innerCls = InnerCls("abc")