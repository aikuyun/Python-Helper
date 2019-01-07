"""
创建类和类的实例化
"""


class User:
    user_name = ""
    password = ""
    age = 0
    address = ""
    salary = 0.0

    # 初始化函数或者构造函数
    def __init__(self, user_name, password, age, address, salary):
        self.user_name = user_name
        self.password = password
        self.age = age
        self.address = address
        self.salary = salary

    # 自定义函数
    def display_user(self):
        print("userName:", self.user_name, "password:", self.password, "age:", self.age, "address:", self.address,
              "salary:", self.salary)


# 主方法
if __name__ == '__main__':
    user = User("tsl", password="123455", age=10, address="shandong", salary=190000.78)
    print("薪水是：", user.salary)
    user.display_user()
