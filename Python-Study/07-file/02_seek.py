# 打开一个文件
test = open("test02_1.txt", "r")
str = test.read(9);
print("读取的字符串是 : ", str)

# 查找当前位置
position = test.tell()
print("当前文件位置 : ", position)


test.seek(10, 0)
#mmmmmmm我爱你啊
str = test.read(9)
print("重新读取字符串 : ", str)

# 关闭打开的文件
test.close()