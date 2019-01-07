## 类

class 关键字

```python
class Student(object):
    pass
```

创建实例是通过类名+()实现的：

```python
student = Student()
```

构造函数：
cd ..
```python

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
```