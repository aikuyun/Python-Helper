
# dict 查询速度快，字典

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
#
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。


def test():
    d = {"li": 23, "dan": 21}
    print(d['li'])

    d['tao']  # 如果 key 不存在，就会报错。

    # 如果判断 key是否存在呢？
    # 1.使用 key in d 2.或者使用 get() ，没有则但会 none ,也可以自己指定 value
    # 当 key 不存在是，会返回 -1，使我们自己指定的。
    print(d.get('tao', -1))

    # 删除 pop(key)

    print(d.pop('li'))

    # dict内部存放的顺序和key放入的顺序是没有关系的。dict的key必须是不可变对象。

    # 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key


if __name__ == "__main__":
    test()
