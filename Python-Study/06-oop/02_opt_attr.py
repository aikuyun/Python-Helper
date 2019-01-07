"""
对象属性的操作
对象的属性可以动态添加
若删除（改修后的）属性 ,则还原成默认的属性值
"""


class Employee:
    name = ""
    salary = 5.0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def test(self):
        print("TTT")

    @classmethod
    def a(cls):
        print(1)

# 调用静态方法


Employee.a()


if __name__ == '__main__':

    emp = Employee("tsl", 999999)
    emp.gender = 1

    print("新增属性：", emp.gender)

    print("修改前：", emp.name)
    emp.name = 'dandandan'
    print("修改后：", emp.name)

    del emp.gender
    # print "删除后：", emp.gender

    print("#############")
    print("hasattr判断是否有此属性：", hasattr(emp, 'salary'))

    print("getattr获取name属性：", getattr(emp, "name"))

    setattr(emp, "salary", 1)
    print("setattr属性salary：", getattr(emp, "salary"))

    del emp.salary

    print("删除后：", emp.salary)
