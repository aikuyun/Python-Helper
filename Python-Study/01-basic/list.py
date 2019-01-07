
# list 是一种有序的集合。可以随时添加和删除里面的元素
# list 是一个可变的


def test():
    list1 = [1, 2, 3, 4]
    # len() 统计元素的个数
    print(len(list1))
    # 索引从 0 开始
    print(list1[0])

    # 删除末尾的元素可以使用 pop()
    print(list1.pop())

    # 添加元素到 list 的末尾
    list1.append(22)
    print(list1)

    # 插入元素到具体的位置
    list1.insert(1, 44)
    print(list1)


if __name__ == "__main__":
    test()
