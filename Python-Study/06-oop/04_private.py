"""私有变量和方法"""


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__plus()
        print(self.__secretCount)

    def count2(self):
        return self.__secretCount

    # 私有方法
    def __plus(self):
        self.__secretCount += 1
        self.publicCount += 2


if __name__ == '__main__':
    counter = JustCounter()
    counter.count()
    # 在类的对象生成后,调用含有类私有属性的函数时就可以使用到私有属性.
    counter.count()

    # 第二次同样可以.
    print(counter.publicCount)

    counter.count2()
