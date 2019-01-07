
def open_file(mod = 'r'):
    test = open("test02_1.txt", mod)
    print("文件名: ", test.name)
    print("是否已关闭 : ", test.closed)
    print("访问模式 : ", test.mode)
    return test

# with open("test02_1.txt", "r") as test:
#     print"文件名: ", test.name
#     print"是否已关闭 : ", test.closed
#     print"访问模式 : ", test.mode
#     print"末尾是否强制加空格 : ", test.softspace
#     print "===================="


def read():
    filee = open_file("r")
    # 全部读出
    # print "文件内容：", filee.read()
    # 一行一行读取

    line = filee.readline()
    while line:

        print(line)
        line = filee.readline()

    filee.close()


def write():
    # w: 有覆盖，没有创建
    # wb: 二进制打开，有覆盖，没有创建
    # a: 有追加，没有创建
    # filee = open_file("w")

    filee = open_file("a")
    # filee = open_file("a+")
    # r+追加到前面
    # filee = open_file("r+")


    filee.close()


if __name__ == '__main__':
    open_file()
    # write()
    # print "###################"
    # read()


