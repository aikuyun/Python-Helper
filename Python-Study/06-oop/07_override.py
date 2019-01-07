# -*- coding:utf-8 -*-

"""方法重写"""

# 哺乳动物
class Mammals():
    hair = True

    def call(self):
        print("动物会叫。。。")

# 人
class Human(Mammals):

    def say(self):
        print("人会说话")

    # 重写父类方法
    def call(self):
        print("人是讲话的。。。")


if __name__ == '__main__':
    human = Human()
    human.call()

