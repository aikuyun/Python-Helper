
class Student:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 单个对象转dict
def convert_to_dict(obj):
    dict = {}
    dict.update(obj.__dict__)
    return dict


# 把对象列表转换为字典列表
def convert_to_dicts(objs):
    dict_arr = []
    for obj in objs:
        dict = convert_to_dict(obj)
        dict_arr.append(dict)
    return dict_arr


# 把对象(支持单个对象、list、set)转换成字典
def class_conver_to_dicts(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    dict_arr = []
    if is_list or is_set:
        return convert_to_dicts(obj)

    return convert_to_dict(obj)


# 将dict转化成obj
def dict_conver_to_obj(d):
    if isinstance(d, list):
        d = [dict_conver_to_obj(x) for x in d]
    if not isinstance(d, dict):
        return d

    class C(object):
        pass
    o = C()
    for k in d:
        o.__dict__[k] = dict_conver_to_obj(d[k])
    return o

stu = Student("老张", 18)

print(convert_to_dict(stu))
stu2 = Student("老吴", 20)
print(convert_to_dicts([stu, stu2]))

print(class_conver_to_dicts([stu, stu]))

# set是无序不重复集合
set_coll = set()
set_coll.add(stu)
set_coll.add(stu)
print(class_conver_to_dicts(set_coll))

#
d = {'a': 1, 'b': {'c': 2}, 'd': ['hi', {'foo': 'bar'}]}
obj = dict_conver_to_obj(d)
print(obj.d)