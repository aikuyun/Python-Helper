"""多继承"""

# 动物
class Animal:
    cell = True
    age = 10

    def dynamic(self):
        print("动物会动。。")


# 哺乳动物
class Mammals():
    hair = True

    def breastfeed(self):
        print("哺乳动物会哺乳。。。")



# 人
class Human(Mammals, Animal):

    def say(self):
        print("人会说话")


if __name__ == '__main__':
    human = Human()
    human.dynamic()
    human.say()
    human.breastfeed()


